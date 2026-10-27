import math
import numpy as np


def parse_tensile_file(path_to_file):
    file = open(path_to_file)

    gage_diameter = -1
    maximum_force = -1
    maximum_strain = -1

    begin_reading = False

    time = []
    displacement = []
    force = []
    strain = []

    for line in file:
        if line == '' or line == '\n':
            continue

        splits = line.strip().split(",")

        if begin_reading == False:
            if splits[0] == "Gage Diameter":
                cleaned = splits[2].replace('"', '')
                gage_diameter = float(cleaned)

            if splits[0] == "Maximum Force":
                cleaned = splits[2].replace('"', '')
                maximum_force = float(cleaned)

            if splits[0] == "Maximum Strain":
                cleaned = splits[2].replace('"', '')
                maximum_strain = float(cleaned)

        else:
            time.append(float(splits[0].replace('"', '')))
            displacement.append(float(splits[1].replace('"', '')))
            force.append(float(splits[2].replace('"', '')))
            strain.append(float(splits[3].replace('"', '')))

        if splits[0] == "(s)":
            begin_reading = True

    file.close()

    return (
        gage_diameter,
        np.asarray(time),
        np.asarray(displacement),
        np.asarray(force),
        np.asarray(strain)
    )


def calculate_stress(force, sample_diameter):
    # Cross-sectional area in mm^2
    cross_section_area = (math.pi * sample_diameter ** 2) / 4

    # Convert force from kN to N, then calculate stress in MPa
    stress = (force * 1000) / cross_section_area

    return stress


def calculate_max_strength_strain(strain, stress):
    ultimate_tensile_stress = max(stress)
    fracture_strain = max(strain)

    return ultimate_tensile_stress, fracture_strain


def calculate_elastic_modulus(strain, stress):
    # Find the stress value at 40% of peak stress
    secant_strain = 0.4 * max(stress)

    # Find the index closest to that value
    diffs = abs(stress - secant_strain)
    linear_index = np.argmin(diffs)

    # Select the linear region
    linear_stress = stress[:linear_index]
    linear_strain = strain[:linear_index]

    # Fit a straight line
    slope, intercept = np.polyfit(linear_strain, linear_stress, 1)

    return linear_index, slope, intercept


def calculate_percent_offset(slope, strain, stress):
    offset = 0.002

    offset_line = slope * (strain - offset)

    distance = abs(stress - offset_line)
    intercept_index = np.argmin(distance)

    return offset_line, intercept_index


def calculate_yield_strength(strain, stress, modulus):
    offset_line, intercept_index = calculate_percent_offset(
        modulus, strain, stress
    )

    if intercept_index == -1:
        return -1

    return stress[intercept_index]


class MaterialSample:
    def __init__(self):
        self.name = ""
        self.material_type = ""
        self.tensile_strength = -1
        self.fracture_strain = -1
        self.elastic_modulus = -1
        self.yield_strength = -1
