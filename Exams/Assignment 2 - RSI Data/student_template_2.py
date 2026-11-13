"""
CULMINATING ASSIGNMENT 2: RSI

Create a program which will provide answers to the tasks posed in the assignment description.

For this assignment, you will start from scratch with this blank template.
It is your reponsibility to include all necessary program components in this file.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.

The relevant data file is named "all_participant_data_rsi.csv" and is located in data > drop-jump.

All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""
import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, norm, chisquare, t
import matplotlib.pyplot as plt

#Load RSI data for accelerometer and force plate data
df = pd.read_csv("../../data/drop-jump/all_participant_data_rsi.csv")

#Pull out force plate column
force_plate = df["force_plate_rsi"].to_numpy()

#Pull out accelermeter column
accelerometer = df["accelerometer_rsi"].to_numpy()

#Asssigned alpha value
alpha = 0.05

################################################################################################################
### Task 1: 
"""
For the new dataset of RSI values (all_participant_data_rsi.csv), conduct a paired t-test comparing 
all the force plate and accelerometer RSI values. Clearly report the t-value, p-value, null and alternative 
hypotheses, and decide whether the null hypothesis can be rejected or not. In your report: What can we conclude
about the two measurement methods?
"""
#Calculate the difference between force plate and accelerometer RSI values
difference = force_plate - accelerometer 

#Perform a paired t-test
t_value, p_value = ttest_1samp(difference, popmean=0, alternative="two-sided")

#Print results
print("T-Value =", t_value)
print("P-Value =", p_value)

#Check null hypothesis 
if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")


########################################################################################################################
### Task 2: 
"""
For the RSI values gathered using an accelerometer, fit a normal distribution and conduct a Chi2 Goodness of Fit Test. 
Clearly print out the chi2 stat, p-value, and an indication of whether it is a good fit or not. Plot a histogram of the 
accelerometer data with the normal distribution curve overlaid. In your report: what factors in the data cause this to 
be a good fit or not?
"""
#Find the mean and standard deviation of the accelerometer data
fitted_mean, fitted_std = norm.fit(accelerometer)

#Get the fitted probability distribution
x = np.linspace(min(accelerometer), max(accelerometer), 1000)
y = norm.pdf(x, loc=fitted_mean, scale=fitted_std)

#Plot the accelormeter data as a histogram
plt.hist(accelerometer, bins=15, density=True, label="Accelerometer RSI")

#Plot the fitted distribution over the plotted accelormeter data
plt.plot(x, y, label="Fitted Normal")
plt.xlabel("Accelerometer RSI")
plt.ylabel("Probability density")
plt.legend()
plt.show()

#Ensure expected count is at least 5

#Create bins from fitted meam and fitted standard deviation
bins = np.linspace(fitted_mean - 1.5 * fitted_std, fitted_mean + 1.5 * fitted_std, 7) #Adjusted to make expected counts above 5

#Add infinite on each end and joins them into one array
bins = np.r_[-np.inf, bins, np.inf]

#Place observations into bins
observed_counts, observed_edges = np.histogram(accelerometer, bins=bins, density=False)

#Using the difference between the bin edges provides the probability that a value is within a bin
expected_prob = np.diff(norm.cdf(bins, loc=fitted_mean, scale=fitted_std))

#Expected frequency for each bin
expected_counts = expected_prob * len(accelerometer)

#Print results
print("Observed Counts =", observed_counts)
print("Expected Counts =", expected_counts)

### Run chi-square test

#Conduct chi2 test 
#ddof=2 accounts for the mean and standard deviation
chi2_value, chi_p_value = chisquare(f_obs=observed_counts, f_exp=expected_counts, ddof=2)

#Print results
print("Chi-square statistic =", chi2_value)
print("P-value =", chi_p_value)

#Check the normal fit
if chi_p_value < alpha:
    print("Reject the normal fit.")
else:
    print("Fail to reject the normal fit.")

###############################################################################################################
### Task 3:

"""
From the force plate and accelerometer-based RSI data for all participants, create and print() a dataframe 
containing only the trials from Participant F. Calculate the 95% confidence intervals for Participant F's 
RSI for both the force plate and accelerometer measurements.
"""

# Create a dataframe for Participant F

#Create dataframe of all trials
trials = df["trial"]

#Determine which trials belong to Participant F
participant_f_df = df[df["trial"].str.contains("F_trial_")]

#Print dataframe for Participant F
print(participant_f_df)

#Calculate 95% confidence intervals for Participant F's RSI (accelerometer and force plate)

#Count Participant F's Trials
n = len(participant_f_df)

#Find degrees of freedom 
dof = n - 1 

#Looks up Z value for a two-sided 95% interval
zscore = t.ppf(1 - alpha / 2, df=dof) 

for column in ["force_plate_rsi", "accelerometer_rsi"]:
    data = participant_f_df[column]

    #Calculate average RSI and how much they vary
    mean_rsi = data.mean()
    sample_std = data.std()

    #Calculate standard error
    standard_error = sample_std / n **.5

    #Calculate lower and upper bounds of the confidence interval
    lower = mean_rsi - (zscore * standard_error)
    upper = mean_rsi + (zscore * standard_error)

    print(column,": 95% CI =", lower,"-", upper)





















