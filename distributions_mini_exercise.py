# Use a scipy statistical distribution to answer the questions below:
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

np.random.seed(123)

die_distribution = stats.randint(1, 7)

# What is the probability of rolling a 1?

die_distribution.pmf(1)

# There's a 1 in 2 chance that I'll roll higher than what number?

die_distribution.isf(1/2)

# What is the probability of rolling less than or equal to 2?

die_distribution.cdf(2)

# There's a 5 in 6 chance that my roll will be less than or equal to what number?

die_distribution.ppf(5/6)

# There's a 1 in 2 chance that my roll will be less than or equal to what number?

die_distribution.ppf(1/2)

# What is the probability of rolling less than or equal to 6?

die_distribution.cdf(6)

# There's a 1 in 3 chance that I'll roll higher than what number?

die_distribution.isf(1/3)

# What is the probability of rolling higher than a 1?

die_distribution.sf(1)

# There's a 2 in 3 chance that my roll will be less than or equal to what number?

die_distribution.ppf(2/3)

# There's a 2 in 3 chance that I'll roll higher than what number?

die_distribution.isf(2/3)

# There's a 1 in 3 chance that my roll will be less than or equal to what number?

die_distribution.ppf(1/3)

# There's a 1 in 6 chance that I'll roll higher than what number?

die_distribution.isf(1/6)


