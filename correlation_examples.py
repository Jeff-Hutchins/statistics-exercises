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



print(employees.shape)
print(employees.dtypes)
employees.sample(5)

import pandas as pd
from env import host, user, password
    
employees_url = get_db_url(user, password, host, 'employees')

employees = pd.read_sql('''SELECT
    e.*,
    datediff('2002-09-30', e.hire_date) tenure,
    t.title,
    t.from_date title_from,
    datediff('2002-09-30', t.from_date) t_tenure,
    et.titles,
    s.salary,
    s.from_date salary_from,
    datediff('2002-09-30', s.from_date) s_tenure,
    es.salaries
FROM
    employees e
JOIN 
    titles t 
    USING(emp_no)
JOIN 
    salaries s 
    USING(emp_no)
JOIN
    (SELECT 
        emp_no,
        count(*) titles
    FROM
        titles
    GROUP BY
        emp_no) et
    USING(emp_no)
JOIN
    (SELECT 
        emp_no,
        count(*) salaries
    FROM
        salaries
    GROUP BY
        emp_no) es
    USING(emp_no)
WHERE
    s.to_date > '2002-09-30'
    AND t.to_date > '2002-09-30';
''', employees_url)

print(employees.shape)
print(employees.dtypes)
employees.sample(5)
