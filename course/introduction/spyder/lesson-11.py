#!/usr/bin/env python
# coding: utf-8

#%%
# # Accessing Elements in NumPy Arrays
# 
# This lesson covers:
# 
# * Accessing specific elements in NumPy arrays
# 
# Accessing elements in an array or a DataFrame is a common task. To begin this lesson, clear the
# workspace set up some vectors and a $5\times5$ array. These vectors and matrix will make it easy
# to determine which elements are selected by a command.
# 
# 
# Using `arange` and `reshape` to create 3 arrays:
# 
# * 5-by-5 array `x` containing the values 0,1,...,24 
# * 5-element, 1-dimensional array `y` containing 0,1,...,4
# * 5-by-1 array `z` containing 0,1,...,4
# 

#%%
import numpy as np
x = np.arange(25).reshape((5,5))
print(x)

#%%
y = np.arange(5)
print(y)

#%%
z = np.arange(5).reshape((5,1))
print(z)

#%%
# ## Zero-based indexing
# Python indexing is 0 based so that the first element has position `0`, the second has position `1`
# and so on until the last element has position `n-1` in an array that contains `n` elements in
# total.
# 
# ## Problem: Scalar selection
# Select the number 2 in all three, `x`, `y`, and `z`.
# 
# 
# **Question**:  Which index is rows and which index is columns?

#%%
print(x[0, 2])


#%%
print(y[2])

#%%
print(z[2, 0])

#%%
# ## Problem: Scalar selection of a single row
# 
# Select the 2nd row in `x` and `z` using a single integer value.
#  
# **Question**: What is the dimension of `x` and the second row of `x`

#%%
print(x[1])

#%%
print(x[1].shape)

#%%
print(z[1])

#%%
print(z[1].shape)

#%%
# ## Problem: Slice selection of a single row
# 
# Use a slice to select the 2nd row of `x` and the 2nd element of `y` and `z`.
# 
# **Question**: What are the dimension selections?

#%%
print(x[1:2])

#%%
print(x[1:2].shape)

#%%
print(y[1:2].shape)

#%%

print(z[1:2])
#%%
# ## Problem: List selection of a single row
# 
# Use a list to select the 2nd row of `x` and the 2nd element of `y` and `z`.
# 
# **Question**: What are the dimension selections?

#%%
print(x[[1]])

#%%
print(x[[1]].shape)

#%%
print(z[[1]])

#%%
# ## Problem: Selecting a single Column
# Select the 2nd column of x using a scalar integer, a slice and a list.
# 
# **Question**: What the the dimensions of the selected elements?

#%%
print(x[:, 1])

#%%
print(x[:, 1].shape)


#%%

print(x[:, 1:2])

#%%

print(x[:, [1]])

#%%
# ## Problem: Selecting a block of specific columns
# Select the 2nd and 3rd columns of x using a slice.

#%%
print(x[:, 1:3])

#%%

print(x[:, [1,2]])

#%%
# ## Problem: Selecting a block of specific rows
# Select the 2nd and 4th rows of x using both a slice and a list. 
# 

#%%

print(x[1:4:2])

#%%

print(x[[1, 3]])

#%%
# ## Problem: Selecting a block of specific rows and columns
# Combine these be combined to select the 2nd and 3rd columns and 2nd and 4th rows.

#%%
print(x[1:4:2, 1:3])

#%%
print(x[1:4:2, [1, 2]])

#%%
print(x[[1, 3], 1:3])

#%%

print(x[[1,3], [1,2]])

#%%
# ## Problem: Use `ix_` to select rows and columns using lists
# Use `ix_` to select the 2nd and 4th rows and 1st and 3rd columns of `x`.

#%%
print(x[np.ix_([1,3], [1,2])])

#%%
print(np.ix_([1,3], [1,2]))

#%%
print(x[[[1,1],[3,3]], [[1,2], [1,2]]])

#%%
# ## Problem: Convert a DataFrame to a NumPy array
# 
# Use  `.to_numpy` to convert a DataFrame to a NumPy array.

#%%
# Setup: Create a DataFrame
import pandas as pd
import numpy as np

names = ["a", "b", "c", "d", "e"]
x = np.arange(25).reshape((5,5))
x_df = pd.DataFrame(x, index=names, columns=names)
print(x_df)


#%%

x_df.to_numpy()

print(x_df)

#%%
# ## Problem: Use `np.asarray` to convert to an array
# 
# Use  `np.asarray` to convert a DataFrame to a NumPy array.

#%%
np.asarray(x_df)

print(x_df)

#%%
# ## Exercises
# 
# ### Exercise: Block selection
# 
# Select the second and third rows of `a` and the first and last column.
# Use at least three different methods including all slices, `np.ix_`, and
# mixed slice-list selection.

#%%
# Setup: Data for Exercises

import numpy as np
rs = np.random.RandomState(20000214)
a = rs.randint(1, 10, (4,3))
b = rs.randint(1, 10, (6,4))

print(f"a = \n {a}")
print()
print(f"b = \n {b}")


#%%


#%%


#%%


#%%
# ### Exercise: Row Assign
# 
# Assign the first three elements of the first row of `b` to `a`.
# 
# **Note** Assignment sets one selected block in one array equal to another 
# block.
# 
# ```python
# x[0:2,0:3] = y[1:3,1:4]
# ```

#%%


#%%
# ### Exercise: Block Assign
# 
# Assign the block consisting the first and third columns and the second and last rows of `b`
# to the last two rows and last two columns of `a`

#%%

