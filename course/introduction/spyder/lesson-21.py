#!/usr/bin/env python
# coding: utf-8

#%%
# # Graphics: Line Plots
# 
# This lesson covers:
# 
# * Basic plotting 
# * Subplots 
# * Histograms 
# * Scatter Plots

#%%
# Plotting in notebooks requires using a magic command, which starts with
# `%`, to initialize the plotting backend.

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

print(msft.head())

#%%
# ## Problem: Basic Plotting
# 
# 1. Plot the `ibm` series which contains the price of IBM. 
# 2. Add a title and label the axes. 
# 3. Add markers and remove the line. 

#%%
ax = ibm.plot()
ax

#%%
ax = ibm.plot()
ax.set_title("IBM Price")
ax.set_xlabel("Time")
ax.set_ylabel("Price")

#%%
ax = ibm.plot(linestyle="none", marker="v")
ax.set_title("IBM Price")
ax.set_xlabel("Time")
ax.set_ylabel("Price")

#%%
# ## Problem: Subplot
# 
# Create a 2 by 1 subplot with the price of IBM in the top subplot and the
# price of MSFT in the bottom subplot. 

#%%
import matplotlib.pyplot as plt
plt.rc("figure", figsize=(12,8))
import seaborn
seaborn.set_style("darkgrid")

fig, axes = plt.subplots(2,1)
ibm.plot(ax=axes[0], linewidth=3)
msft.plot(ax=axes[1], color="orange", linestyle="-.")

#%%
# ## Problem: Plot with Dates
# 
# Use `matplotlib` to directly plot `ibm` against its `index`. This is a
# repeat of a previous plot but shows how to use the `plot` command directly. 

#%%
plt.plot(ibm.index, ibm.values)
ax = plt.gca()
ax.set_xlim(ibm.index[0], ibm.index[-1])

#%%
# ## Exercises
# 
# ### Exercise: Change seaborn
# 
# Produce a line plot of MSFT's price using seaborn's "whitegrid" style.

#%%


#%%
# ### Exercise: HLOC plot
# 
# Use the HLOC data to produce a plot of MSFT's 5 minute HLOC
# where the there are no lines, high is demarcated using a green triangle,
# low is demarcated using a red downward pointing triangle, open is demarcated 
# using a light grey leftward facing triangle and close is demarcated using
# a right facing triangle.
# 
# **Note** Get the axes from the first, plot, and reuse this when plotting 
# the other series.

#%%
# Setup: Load data and create values
import pandas as pd

msft = pd.read_hdf("data/hf.h5", "MSFT")
msft_5min = msft.resample("300S")
high = msft_5min.max()
low = msft_5min.min()
open = msft_5min.first()
close = msft_5min.last()


#%%

