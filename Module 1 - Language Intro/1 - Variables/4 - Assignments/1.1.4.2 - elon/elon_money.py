"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $33B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""


def compound_intrest(principle, rate, n):
    answer = principle * (1 + rate) ** n
    return answer

principle= 33000000000
ten_year_rate = 0.0396
twenty_year_rate = 0.0432
ten_years = 10
twenty_years = 20

ten_year_final = compound_intrest(principle, ten_year_rate, ten_years)
print("Elon's 10-year investment would be worth: " + str(ten_year_final))

ten_year_final = 33000000000 * (1 + 0.0396) ** 10
twenty_year_final = 33000000000 * (1 + 0.0432) ** 20

print("Elon's 10-year investment would be worth: " + str(ten_year_final))
print("Elon's 20-year investment would be worth: " + str(twenty_year_final))

# final answer for 10-year
ten_year_final = 48660509081.78675

# final answer for 20-year
twenty_year_final = 76889229275.98897
