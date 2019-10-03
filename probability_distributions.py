import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

np.random.seed(123)

# theoretical = using scipy to answer questions
# experimental = using simulation to answer questions

# Do your work for this exercise in either a python script named probability_distributions.py 
# or a jupyter notebook named probability_distributions.ipynb.

# For the following problems, use python to simulate the problem and calculate an experimental 
# ability, then compare that to the theoretical probability.

# 1. A bank found that the average number of cars waiting during the noon hour at a drive-up 
# window follows a Poisson distribution with a mean of 2 cars. Make a chart of this 
# distribution and answer these questions concerning the probability of cars waiting 
# at the drive-up window.

fig, ax = plt.subplots(1, 1)
mu = 2
mean, var, skew, kurt = stats.poisson.stats(mu, moments='mvsk')
x = np.arange(stats.poisson.ppf(0.01, mu),
              stats.poisson.ppf(0.99, mu))
ax.plot(x, stats.poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
ax.vlines(x, 0, stats.poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)


s = np.random.poisson(2, 10000)
count, bins, ignored = plt.hist(s, 14, normed=True)
plt.show()

    # What is the probability that no cars drive up in the noon hour?

# theoretical
stats.poisson(2).pmf(0)

# experimental

np.random.poisson(2, 10000)

number_of_cars = pd.DataFrame(np.random.poisson(2, 10000))
(number_of_cars == 0).mean()

    # What is the probability that 3 or more cars come through the drive through?

# theoretical
stats.poisson(2).sf(2)

# experimental
(number_of_cars >= 3).mean()

    # How likely is it that the drive through gets at least 1 car?

# theoretical
stats.poisson(2).sf(0)

# experimental
(number_of_cars >= 1).mean()

# 2. Grades of State University graduates are normally distributed with a mean of 3.0 and a 
# standard deviation of .3. Calculate the following:

    # What grade point average is required to be in the top 5% of the graduating class?

# theoretical
grades_dist = stats.norm(3, .3)
grades_dist.ppf(.95)

# experimental with numpy
trials = 10_000
grades_array = np.random.normal(3, .3, trials)
np.quantile(grades_array, .95)

# experimental with pandas
pd.DataFrame(np.random.normal(3, .3, trials)).quantile(.95)

    # An eccentric alumnus left scholarship money for students in the third decile from the 
    # bottom of their class. Determine the range of the third decile. Would a student with a 
    # 2.8 grade point average qualify for this scholarship?

# theoretical
grades_dist.ppf(.7)
grades_dist.ppf(.8)

grades_dist.isf(.3)
grades_dist.isf(.2)

# experimental
np.quantile(grades_array, .7)
np.quantile(grades_array, .8)

pd.DataFrame(np.random.normal(3, .3, trials)).quantile(.7)
pd.DataFrame(np.random.normal(3, .3, trials)).quantile(.8)

# 3. A marketing website has an average click-through rate of 2%. One day they observe 4326 
# visitors and 97 click-throughs. How likely is it that this many people or more click through?

# theoretical
click_rate = .02
visitors = 4326
click_throughs = 97
97/4326
stats.poisson(.02*4326).sf(97) * 100

# experimental
(pd.DataFrame(np.random.poisson(4326*.02, 10000)) >= 97).mean()


# 4. You are working on some statistics homework consisting of 100 questions where all of 
    # the answers are a probability rounded to the hundreths place. Looking to save time, 
    # you put down random probabilities as the answer to each question.

answers = pd.DataFrame(np.round(np.random.sample(100), decimals=2))

    # What is the probability that at least one of your first 60 answers is correct?

# theoretical
stats.binom(60, .01).sf(0)
stats.binom(100, .01).sf(0)

# experimental
(np.random.binomial(60, .01, 10000) > 0).mean()
(np.random.binomial(100, .01, 10000) > 0).mean()

# 5. The codeup staff tends to get upset when the student break area is not cleaned up. 
# Suppose that there's a 3% chance that any one student cleans the break area when 
# they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 
# students visit the break area. How likely is it that the break area gets cleaned 
# up each day? How likely is it that it goes two days without getting cleaned up? All week?

# theoretical
students = round(.9*(22*3))
student_cleans = .03*students
stats.binom(students, .03).cdf(0) # each day
 1 - (stats.binom(students, .03).cdf(1)) # two days
1 - (stats.binom(students, .03).cdf(4)) # 5 days

# experimental
(np.random.binomial(students, .03, 10000) == 0).mean()
(np.random.binomial(students, .03, 10000) >= 2).mean()
(np.random.binomial(students, .03, 10000) >= 5).mean()

# 6. You want to get lunch at La Panaderia, but notice that the line is usually very 
# long at lunchtime. After several weeks of careful observation, you notice that 
# the average number of people in line when your lunch break starts is normally 
# distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes 
# for each person to order, and 10 minutes from ordering to getting your food, what 
# is the likelihood that you have at least 15 minutes left to eat your food before 
# you have to go back to class? Assume you have one hour for lunch, and ignore 
# travel time to and from La Panaderia.

# theoretical
stats.norm(40, 6).cdf(45)

# experimental
(np.random.normal(40, 6, 10000) < 45).mean()

# 7. Connect to the employees database and find the average salary of current employees, 
# along with the standard deviation. Model the distribution of employees salaries with 
# a normal distribution and answer the following questions:

from env import host, user, password
database_name = "employees"
url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

employees_query = "SELECT * from employees"
employees = pd.read_sql(employees_query, url)
employees.head()

salaries_query = "SELECT * from salaries where to_date = '9999-01-01'"
salaries = pd.read_sql(salaries_query, url)

type(salaries)
salaries_mean = salaries.salary.mean()
salaries_std = salaries.salary.std()

# theoretical
stats.norm(salaries_mean, salaries_std)


# experimental
salaries_np = np.random.normal(salaries_mean, salaries_std, 10000)
salaries_dataframe = pd.DataFrame(np.random.normal(salaries_mean, salaries_std, 10000))

    # What percent of employees earn less than 60,000?

# theoretical
stats.norm(salaries_mean, salaries_std).cdf(60000)

# experimental
(salaries_dataframe < 60000).mean()

    # What percent of employees earn more than 95,000?

# theoretical
stats.norm(salaries_mean, salaries_std).sf(95000)

# experimental
(salaries_dataframe > 95000).mean()

    # What percent of employees earn between 65,000 and 80,000?

# theoretical
stats.norm(salaries_mean, salaries_std).cdf(80000) - stats.norm(salaries_mean, salaries_std).cdf(65000)


# experimental
salaries_np.where(np.logical_and(a>60000, a<80000))
salaries_np

    # What do the top 5% of employees make?

# theoretical
stats.norm(salaries_mean, salaries_std).ppf(.95)
stats.norm(salaries_mean, salaries_std).ppf(.9999996825)

# experimental
salaries_dataframe.quantile(.95)

