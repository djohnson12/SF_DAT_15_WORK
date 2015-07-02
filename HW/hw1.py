'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''


import pandas as pd
pd.options.display.max_rows = 150
import matplotlib.pyplot as plt
# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('/Users/Danielle/Desktop/GA/SF_DAT_15/hw/data/police-killings.csv')
killings.head()
killings.info()
killings.describe()

killings.rename(columns = {'lawenforcementagency':'agency', 'raceethnicity':'race'}, inplace = True)
# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race

# 2. Show the count of missing values in each column
killings.isnull().sum()

# 3. replace each null value in the dataframe with the string "Unknown"
    #there are no null values

# 4. How many killings were there so far in 2015?
killings[killings.year == 2015].groupby('year')['year'].count()

# 5. Of all killings, how many were male and how many female?
killings.groupby('gender')['gender'].count()

killings.gender[killings.gender == 'Female'].count()

# 6. How many killings were of unarmed people?
killings.armed[killings.armed == 'No'].count()

# 7. What percentage of all killings were unarmed?
unarmed_killings = killings.armed[killings.armed == 'No'].count()
total_killings = killings.name[killings.name != ''].count()
unarmed_percentage = (unarmed_killings*1.0) / (total_killings*1.0)
unarmed_percentage


# 8. What are the 5 states with the most killings?
killings_by_state = killings.groupby('state')['state'].count()
killings_by_state.sort(inplace = True)
killings_by_state.tail()
# 9. Show a value counts of deaths for each race
killings.groupby('race')['race'].count()


# 10. Display a histogram of ages of all killings
killings.age.hist()

# 11. Show 6 histograms of ages by race
killings.age.hist(by=killings.race, sharex=True)

# 12. What is the average age of death by race?
killings.groupby('race')['age'].mean()

# 13. Show a bar chart with counts of deaths every month
killings.groupby('month')['month'].count().plot(kind='bar')


###################
### Less Morbid ###
###################

majors = pd.read_csv('hw/data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)
majors.drop('Employed_full_time_year_round', axis = 1, inplace = True)
majors.drop('Major_code', axis = 1, inplace = True)

# 2. Show the cout of missing values in each column
majors.isnull().sum()
# 3. What are the top 10 highest paying majors?
majors.sort(columns='Median')[['Major', 'Median']].tail(10) # highest median
majors.sort(columns='Median')[['Major', 'P25th']].tail(10) # highest 25th percentile
majors.sort(columns='Median')[['Major', 'P75th']].tail(10) # highest 75th percentile



# 4. Plot the data from the last question in a bar chart, include proper title, and labels!
majors.sort(columns='Median')[['Major', 'Median']].tail(10).plot(kind='bar') # highest median

fig = plt.figure() #halphalphalp

# 5. What is the average median salary for each major category?
majors.groupby('Major_category')['Median'].mean()


# 6. Show only the top 5 paying major categories
majors.groupby('Major_category')[['Median','Major_category']].mean().sort(columns='Median').tail(5)
majors.groupby('Major_category')[['Median','Major_category']].mean().sort(columns='Median')

# 7. Plot a histogram of the distribution of median salaries
majors.Median.hist()

# 8. Plot a histogram of the distribution of median salaries by major category
majors.Median.hist(by=majors.Major_category, figsize=(40,26)) #meh, breaks where major category only has one median value
#stops plotting because interdisciplinary category has only one median value aka no discribution 

# 9. What are the top 10 most UNemployed majors?
majors.sort(columns='Unemployed')[['Major','Unemployed']].tail(10) #top 10 most unemployed by sheer volume
# What are the unemployment rates?
majors.sort(columns='Unemployed')[['Major','Unemployment_rate']].tail(10) # unemployment rate of 10 most unemployed by volume

# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
majors.groupby('Major_category')[['Major_category','Unemployed']].mean().sort(columns='Unemployed').tail(10)
# What are the unemployment rates?
majors.groupby('Major_category')[['Major_category','Unemployed','Unemployment_rate']].mean().sort(columns='Unemployed').tail(10) 

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042
majors['sample_employment_rate'] = majors['Employed'] / majors['Total']

# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"
majors['sample_unemployment_rate'] = majors['Unemployed'] / majors['Total']

