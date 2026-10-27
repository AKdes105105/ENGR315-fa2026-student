import sys


"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

# Parse through csv US county covid data
data = parse_nyt_data(file_path = 'data/covid/us-counties.csv')

# Create list of tuples for Harrisonburg and Rockingham County 
harrisonburg_data = []
rockingham_data = []

for row in data:
    if row[3] == "51660": # Harrisonburg, VA fips code
        harrisonburg_data.append(row)  

for row in data:
    if row[3] == "51165": # Rockingham, VA fips code
        rockingham_data.append(row) 


### Determine the first reported positive COVID case in Harrisonburg ###
for row in harrisonburg_data:
        print("The date of the first reported positive COVID case in Harrisonburg was on:", row[0])

        break

### Determine the first reported positive COVID case in Rockingham ###
for row in rockingham_data:
        print("The date of the first reported positive COVID case in Rockingham was on:", row[0])

        break

### Determine on what date was the greatest number of new cases reported in Harrisonburg ###

# Need to determine the gain in cases each day since the data provided is the total cases

new_cases_hburg = []

for i in range(1, len(harrisonburg_data)): #Starting range at one so the first day data in unaffected
    new_cases_hburg.append(harrisonburg_data[i][4] - harrisonburg_data[i-1][4]) #The difference in cases from the previous day

greatest_gain1 = max(new_cases_hburg) # Find max gain in cases in new_cases list
max_index1 = new_cases_hburg.index(greatest_gain1)  # Convert greatest gain to index that can be searched for in the harrisonburg_data

highest_new_cases_date_hburg = harrisonburg_data[max_index1 + 1][0] # Find the row in harrsionburg data that the greatest gain exists (max_index + 1 because loop starts at i = 1) and the data in that row

print("The date of the greatest number of new cases reported in Harrisonburg was:", highest_new_cases_date_hburg)

### Determine on what date was the greatest number of new cases reported in Rockingham County ###

# Need to determine the gain in cases each day since the data provided is the total cases

new_cases_rockh = []

for i in range(1, len(rockingham_data)):
    new_cases_rockh.append(rockingham_data[i][4] - rockingham_data[i-1][4]) #The difference in cases from the previous day

greatest_gain2 = max(new_cases_rockh) # Find max gain in cases in new_cases list
max_index2 = new_cases_rockh.index(greatest_gain2)  # Convert greatest gain to index that can be searched for in the rockingham_data

highest_new_cases_date_rockh = rockingham_data[max_index2 + 1][0] # Find the row in rockingham data that the greatest gain exists (max_index + 1 because loop starts at i = 1) and the data in that row

print("The date of the greatest number of new cases reported in Rockingham was:", highest_new_cases_date_rockh)

### Determine what was the worst seven-day period in Harrisonburg city for new COVID cases ###

seven_day_periods_hburg = []

for i in range(len(new_cases_hburg) - 6): #Search for i in new cases (stops before the final six starting positions)
     seven_day_periods_hburg.append(sum(new_cases_hburg[i:i+7])) #Sums the new cases for each seven day period and appends to seven_day_periods_hburg list

worst_seven_day_period_hburg = max(seven_day_periods_hburg) #Find the worst seven-day value
worst_seven_day_period_hburg_index = seven_day_periods_hburg.index(worst_seven_day_period_hburg) #Convert seven-day value into index

starting_date_hburg = harrisonburg_data[worst_seven_day_period_hburg_index + 1][0] #Search for worst seven-day index in harrisonburg_data and the corresponding date
end_date_hburg = harrisonburg_data[worst_seven_day_period_hburg_index + 7][0]

print("The worst seven-day period for new COVID cases in Harrisonburg was on:", starting_date_hburg,"-",end_date_hburg)

### Determine what was the worst seven-day period in Rockingham County for new COVID cases ###

seven_day_periods_rockh = []

for i in range(len(new_cases_rockh) - 6): #Search for i in new cases (stops before the final six starting positions)
     seven_day_periods_rockh.append(sum(new_cases_rockh[i:i+7])) #Sums the new cases for each seven day period and appends to seven_day_periods_rockh list

worst_seven_day_period_rockh = max(seven_day_periods_rockh) #Find the worst seven-day value
worst_seven_day_period_rockh_index = seven_day_periods_rockh.index(worst_seven_day_period_rockh) #Convert seven-day value into index

starting_date_rockh = rockingham_data[worst_seven_day_period_rockh_index + 1][0] #Search for worst seven-day index in rockingham and the corresponding date
end_date_rockh = rockingham_data[worst_seven_day_period_rockh_index + 7][0]

print("The worst seven-day period for new COVID cases in Rockingham was on:", starting_date_rockh,"-",end_date_rockh)

### Answers ###
#The date of the first reported positive COVID case in Harrisonburg was on: 2020-03-13
#The date of the first reported positive COVID case in Rockingham was on: 2020-03-22
#The date of the greatest number of new cases reported in Harrisonburg was on: 2022-01-10
#The date of the greatest number of new cases reported in Rockingham was on: 2022-01-17
#The worst seven-day period for new COVID cases in Harrisonburg was on: 2022-01-06 - 2022-01-12
#The worst seven-day period for new COVID cases in Rockingham was on: 2022-01-11 - 2022-01-17