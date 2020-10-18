#!/usr/bin/env python
# coding: utf-8

#%%
# # Graphics: Other Plots
# 
# This lesson covers:
# 
# * Histograms 
# * Scatter Plots

#%%
# Plotting in notebooks requires using a magic command, which starts with `%`,
# to initialize the plotting backend.

#%%
# Setup
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')


#%%
# Begin by loading the data in hf.h5. This data set contains high-frequency
# price data for IBM and MSFT on a single day stored as two Series. IBM is
# stored as "IBM" in the HDF file, and MSFT is stored as "MSFT.

#%%
import pandas as pd
ibm = pd.read_hdf("data/hf.h5", "IBM")
msft = pd.read_hdf("data/hf.h5", "MSFT")

#%%
# ## Problem: Histogram
# 
# Produce a histogram of MSFT 1-minute returns (Hint: you have to produce
# the 1-minute Microsoft returns first using `resample` and `pct_change`).

#%%
rets = msft.resample("60S").last().pct_change().dropna()
ax = rets.plot.hist(bins = 21)
ax.set_title("1-minute MSFT returns (%)")


#%%
# ## Problem: Scatter Plot
# 
# Scatter the 5-minute MSFT returns against the 5-minute IBM returns.
# 
# *Hint*: You will need to create both 5-minute return series, merge them,
# and then plot using the combined DataFrame. 

#%%
import matplotlib.pyplot as plt
plt.rc("figure", figsize=(12,8))
import seaborn as sns
sns.set_style("darkgrid")

msft_rets = msft.resample("300S").last().pct_change().dropna()
ibm_rets = ibm.resample("300S").last().pct_change().dropna()

combined = pd.DataFrame({"MSFT": msft_rets, "IBM": ibm_rets})
combined = combined.dropna()
combined.head()

ax = combined.plot.scatter(x="MSFT", y="IBM", marker="x", s=64)

bound = combined.abs().max().max()
ax.set_xlim(-1.1*bound, 1.1*bound)
ax.set_ylim(-1.1*bound, 1.1*bound)


#%%
# ## Problem: Saving plots
# 
# Save the previous plot to PNG and PDF.

#%%
fig = ax.get_figure()
fig.savefig("scatter.pdf")
fig.savefig("scatter.png", dpi=300, transparent=True)

#%%
# ## Exercises
# 
# ### Exercise: Visualize 5 and 10 minute returns
# 
# Produce a 2 by 1 subplot with a histogram of the 5-minute returns of IBM in the
# top panel and 10-minute returns of IBM in the bottom. Set an appropriate title on
# each of the 2 plots.

#%%


#%%
# ### Exercise: Export the result of the previous exercise to JPEG and PDF   
# 

#%%


#%%
# ## Exercise: Plot histograms and a scatter plot
# 
# Produce a 2 by 2 subplot with:
# 
# * Create a square figure with a size of 10 by 10 using `plt.rc`
# * Histograms of IBM and MSFT on the diagonals
# * Scatter plots on the off-diagonals where the x and y line up with the
#   histogram on the diagonal.
# * Set the limits of the scatter plots to match the appropriate histogram
#   x and y limit.
# * Clean up the plot using `tight_layout`

#%%


#%%
# ### Exercise: Use pandas plotting tools
# 
# Use `pandas.plotting.scatter_matrix` to produce a similar plot to the previous exercise.

#%%

