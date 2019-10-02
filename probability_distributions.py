import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

np.random.seed(123)

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

    # What is the probability that no cars drive up in the noon hour?

stats.poisson(2).pmf(0)

    # What is the probability that 3 or more cars come through the drive through?

stats.poisson(2).sf(3)

    # How likely is it that the drive through gets at least 1 car?

stats.poisson(2).sf(1)

# 2. Grades of State University graduates are normally distributed with a mean of 3.0 and a 
# standard deviation of .3. Calculate the following:

    # What grade point average is required to be in the top 5% of the graduating class?

trials = 10_000
grades_dist = stats.norm(3, .3)
grades_dist.ppf(.95)

    # An eccentric alumnus left scholarship money for students in the third decile from the 
    # bottom of their class. Determine the range of the third decile. Would a student with a 
    # 2.8 grade point average qualify for this scholarship?

grades_dist.isf(.8)
grades_dist.isf(.7)


# 3. A marketing website has an average click-through rate of 2%. One day they observe 4326 
# visitors and 97 click-throughs. How likely is it that this many people or more click through?
click_rate * click_throughs
click_rate = .02
visitors = 4326
click_throughs = 97
97/4326
stats.poisson().pmf()

# 4. You are working on some statistics homework consisting of 100 questions where all of 
    # the answers are a probability rounded to the hundreths place. Looking to save time, 
    # you put down random probabilities as the answer to each question.

answers = np.round(np.random.sample(100), decimals=2)

    # What is the probability that at least one of your first 60 answers is correct?

stats.binom(60, .01).sf(0)
stats.binom(100, .01).sf(0)

# 5. The codeup staff tends to get upset when the student break area is not cleaned up. 
# Suppose that there's a 3% chance that any one student cleans the break area when 
# they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 
# students visit the break area. How likely is it that the break area gets cleaned 
# up each day? How likely is it that it goes two days without getting cleaned up? All week?

students = .9*(22*3)
student_cleans = .03*students
stats.binom(students, .03).pmf(1) # each day
1 - stats.binom(students, .03).pmf(2)
1 - stats.binom(students, .03).pmf(5)

# 6. You want to get lunch at La Panaderia, but notice that the line is usually very 
# long at lunchtime. After several weeks of careful observation, you notice that 
# the average number of people in line when your lunch break starts is normally 
# distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes 
# for each person to order, and 10 minutes from ordering to getting your food, what 
# is the likelihood that you have at least 15 minutes left to eat your food before 
# you have to go back to class? Assume you have one hour for lunch, and ignore 
# travel time to and from La Panaderia.

stats.norm(40, 6).cdf(45)