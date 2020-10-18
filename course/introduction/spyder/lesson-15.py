#!/usr/bin/env python
# coding: utf-8

#%%
# # Boolean Arrays 
# 
# This lesson covers:
# 
# * Creating Boolean arrays
# * Combining Boolean arrays
# * `all` and `any`
# 
# Begin by loading the data in momentum.csv.
# 

#%%
# Setup: Load the momentum data

import numpy as np
import pandas as pd

momentum = pd.read_csv("data/momentum.csv", index_col="date", parse_dates=True)

print(momentum.head())

mom_01 = momentum["mom_01"]
mom_10 = momentum["mom_10"]
mom_05 = momentum["mom_05"]


#%%
# ## Problem: Boolean arrays
# For portfolios 1 and 10, determine whether each return is $<0$ (separately).

#%%
mom_01_neg = mom_01 < 0
print(mom_01_neg.head(20))

#%%
mom_10_neg = mom_10 < 0
print(mom_10_neg.head(20))

#%%
# ## Problem: Combining boolean arrays
# Count the number of times that the returns in both portfolio 1 and portfolio
# 10 are negative. Next count the number of times that the returns in portfolios
# 1 and 10 are both greater, in absolute value, that 2 times their respective
# standard deviations. 

#%%
both = mom_01_neg & mom_10_neg
print(both.head(20))

#%%
both = mom_01_neg & mom_10_neg
print(both.sum())

#%%
print(((mom_01 < 0) & (mom_10 < 0)).sum())

#%%
import numpy as np

print(np.logical_and(mom_10_neg, mom_01_neg).sum())

#%%
mom_01_large = mom_01.abs() > (2 * mom_01.std())
mom_10_large = mom_10.abs() > (2 * mom_10.std())

both_large = mom_01_large & mom_10_large
print(both_large.sum())

#%%
# ## Problem: Combining boolean arrays
# For portfolios 1 and 10, count the number of times either of the returns is $<0$.
# 

#%%
print((mom_01_neg | mom_10_neg).sum())

#%%
print(np.logical_or(mom_01_neg, mom_10_neg).sum())

#%%
# ## Problem: Count the frequency of negative returns
# 
# What percent of returns are negative for each of the 10 momentum portfolios?

#%%
neg_returns = momentum < 0
print(neg_returns.mean())

#%%
# ## Problem: Use `any` to find large losses
# 
# Use any to determine if any of the 10 portfolios experienced a loss
# greater than -5%.

#%%
print((momentum < -5).any())

#%%
print(np.any(momentum < -5, axis = 0))

#%%


#%%
# Use `all` and negation to do the same check as `any`.

#%%
print(~((momentum > -5).all()))

#%%
# ## Exercises
# 
# ### Exercise: all and any
# Use `all` and `sum` to count the number of days where all of the portfolio returns
# were negative. Use `any` to compute the number of days with at least 1 negative
# return and with no negative returns (Hint: use negation (~ or `logical_not`)). 

#%%


#%%


#%%


#%%
# ### Exercise: Count Extreme Days
# 
# Count the number of days where each of the portfolio returns is less than the 
# 5% quantile for the portfolio. Also report the fraction of days where all are in their
# lower 5% tail.

#%%


#%%

