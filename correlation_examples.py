# Is there a linear relationship between city mileage and highway mileage?
# There is no linear relationship between city and highway mileage

import math
import numpy as np
from scipy import stats

from pydataset import data

mpg = data('mpg')
mpg

x = mpg.hwy
y = mpg.cty 

r, p = stats.pearsonr(x,y)

print(f'r = {r:.4}')
print(f'p = {p}')

mpg.plot.scatter('hwy', 'cty')
# Reject null hypothesis, there is a linear relationship between the two


# Null Hypothesis - There is no linear relationship between displacement and city mileage
# Alternative Hypothesis - There is a linear relationship between displacement and city mileage

x = mpg.displ
y = mpg.cty 

r, p = stats.pearsonr(x,y)

print(f'r = {r:.4}')
print(f'p = {p}')

mpg.plot.scatter('displ', 'cty')
# Reject null hypothesis, there is a linear relationship between the two
