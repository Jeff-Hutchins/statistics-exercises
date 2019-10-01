import numpy as np
import pandas as pd

np.random.seed(123)

# 1. How likely is it that you roll doubles when rolling two dice?

trials = 10_000
n_dice = 2

rolls = pd.DataFrame(np.random.choice([1, 2, 3, 4, 5, 6], (trials, n_dice)))
rolls

(rolls[rolls[0]==rolls[1]].count()/rolls.count()) * 100

# 2. If you flip 8 coins, what is the probability of getting exactly 3 
# heads? What is the probability of getting more than 3 heads?

trials = 10_000
coins = 8
heads = 1
tails = 0
flips = pd.DataFrame(np.random.choice([0,1], (trials, coins)))
flips[flips.sum(axis=1) == 3].count()/flips.count() * 100

# 3. There are approximitely 3 web development cohorts for every 1 data 
# science cohort at Codeup. Assuming that Codeup randomly selects an 
# alumni to put on a billboard, what are the odds that the two 
# billboards I drive past both have data science students on them?

trials = 10_000
selection = 1
cohorts = np.random.choice([0, 0, 0, 1], (trials, selection))
(cohorts.sum(axis=1) > 0).astype(int).mean() * 100

# 4. Codeup students buy, on average, 3 poptart packages (+- 1.5) a day 
# from the snack vending machine. If on monday the machine is restocked 
# with 17 poptart packages, how likely is it that I will be able to buy 
# some poptarts on Friday afternoon?
trials = 10_000
poptarts_per_day = 3 # +-1.5
poptarts = 17
# 15 +- 7.5, so 7.5, 15, or 22.5
(np.random.randint(7.5, 22.5, (trials, 1)) < 17).sum()/trials * 100


# 5. Compare Heights:

    # Men have an average height of 178 cm and standard deviation of 8cm.

    inches = 178 / 2.54
    feet = inches / 12

    m_height = 178
    m_std_dev_height = 8

    # Women have a mean of 170, sd = 6cm.

    w_height = 170
    w_std_dev_height = 6

    # If a man and woman are chosen at random, P(woman taller than man)?

    trials = 10_000

    # men range 170 - 186
    # women range 164 - 176

    (np.random.uniform(170, 186, (trials, 1)) < np.random.uniform(164, 176, (trials, 1))).sum() / trials * 100
   


# 6. When installing anaconda on a student's computer, there's a 1 in 250 
# chance that the download is corrupted and the installation fails. 
# What are the odds that after having 50 students download anaconda, 
# no one has an installation issue? 100 students?



    # What is the probability that we observe an installation issue within 
    # the first 150 students that download anaconda?



    # How likely is it that 450 students all download anaconda without an 
    # issue?



# 7. There's a 70% chance on any given day that there will be at least one 
# food truck at Travis Park. However, you haven't seen a food truck 
# there in 3 days. How unlikely is this?



    # How likely is it that a food truck will show up sometime this week?



# 8. If 23 people are in the same room, what are the odds that two of them 
# share a birthday? What if it's 20 people? 40?



