#!/usr/bin/env python
# coding: utf-8

#%%
# # Basic Python Types
# 
# This lesson covers:
# 
# * Inputting scalars and strings
# * Lists
# * Tuples
# * Dictionaries
# 

#%%
# ## Problem: Input scalar floating point and integers
# 
# 1. Create a variable called `scalar_float` containing $\pi$ to 4 digits.
# 2. Create a variable called `scalar_int` containing 31415. 
# 3. Print each value using the `print` function.   

#%%
scalar_float = 3.1415
scalar_int = 31415

print(scalar_float)
print(scalar_int)

#%%
# ## Problem: Create a string and an f-string
# 
# 1. Create a variable called `a_string` containing `This is a string`
# 2. Create a f-string the prints `The value of scalar_float is 3.1415` using
#    the variable created in the previous step
# 3. Create two string, `first` containing `String concatenation` and the
#    second containing ` is like addition`, and join the two using `+` to produce
#    `String concatenation is like addition`. 

#%%
a_string = "This is a string"
a_string = 'This is a string'

print(f"The value of scalar_float is {scalar_float}")
print(f"The value of scalar_int is {scalar_int}")

first = "String concatenation"
second = " is like addition"
first + second

#%%
# ## Problem: Create a list
# 
# 1. Create a list containing `scalar_float` and `scalar_int`
# 2. Add `a_string` to the list.
# 3. Select the second element from the list 
# 4. Select the the lst two elements of the list

#%%
a_list = [scalar_float, scalar_int]
print(a_list)

a_list.append(a_string)
print(a_list)

#%%
second_element = a_list[1]
print(second_element)

a_list[:2]

a_list[-2:]

#%%
# ## Problem: Create a list of lists
# 
# 1. Create a list containing the two lists `[1, 2, 3]` and `[4, 5, 6]`
# 2. Select the element 5 from the nested list

#%%
second_list = [[1,2,3],[4,5,6]]

second_list

second_row = second_list[1]
second_row

second_element_second_row = second_row[1]
second_element_second_row

second_list[1][1]
#%%
# ## Problem: Create a tuple
# 
# 1. Create a tuple containing the values (1, 2.0, "c")
# 2. Select the element "c" from the tuple

#%%
tpl = (1,2.0, "c")
tpl

tpl[2]

tpl[-1]

#%%
# ## Problem: Convert a list to a tuple and back
# 
# 1. Convert the list-of-lists created to a tuple-of-tuples
# 2. Convert the tuple-of-tuples back to a list of lists

#%%
second_tuple = (tuple(second_list[0]), tuple(second_list[1]))
second_tuple

re_list = [list(second_tuple[0]), list(second_tuple[1])]
re_list
#%%
# ## Problem: Create a dictionary
# 
# 1. Create a dictionary containing the key-value pairs `"float"` and 3.1415,
#    `"int"` and 31415, and `"string"` and `"three-point-one-four-one-five"`.

#%%
a_dict = {"float": 3.1415, "int": 31415, "string": "three-point-on-four-one-five"}

a_dict


#%%
# ## Problem: Lookup and Change a value
# 
# 1. Look up the value of `"float"`.
# 2. Change the value of `"float"` to `22 / 7`.

#%%
a_dict["float"]

a_dict["float"]=22/7
a_dict

#%%
# ## Problem: Add and remove a key 
# 
# 1. Add the new key "better_float" with the value 3.141592.
# 2. Remove the key "float" and its value.

#%%
a_dict["better_float"] = 3.141592
a_dict

del a_dict["float"]

a_dict

#%%
# ## Exercises
# 
# ### Exercise: Manipulating lists
# 
# 1. Create an empty list called `lst`
# 2. Add the elements `9`, `"Eight"` and `7.0` (in order) to the list.
# 3. Extend the list with the list `["Six", 5, 4.0]` using `extend`
# 4. Select first 4 elements of `lst`
# 5. Select last 3 elements of `lst`
# 

#%%
lst = []

#%%
lst.append(9)
lst.append("Eight")
lst.append(7.0)
lst

#%%
lst.extend(["Six", 5, 4.0])
lst
#%%
print(lst[:5])

#%%
print(lst[-3:])

#%%


#%%


#%%
# ### Exercise: Dictionary Manipulation
# 
# 1. Create a empty dictionary called `dct`
# 2. Add the pairs "apple" and 1, "banana" and 2.0, and "cherry" and "iii"
# 3. Replace the value of "apple" with "I"
# 4. Remove the entry for "banana"
# 5. Add an entry "date" with the value 4

#%%
dct = {}

#%%
dct["apple"] = 1
dct["banana"] = 2.0
dct["cherry"] = "iii"
print(dct)

#%%
dct["apple"] = "I"
dct

#%%
del dct["banana"]
print(dct)

#%%
dct["date"] = 4
print(dct)

#%%
# ### Exercise: Directly create a Dictionary
# 
# Using the final verion of `dct` from the previous exercise:
# 
# 1. Directly initialize a new dictionary called `other_dct`.
# 2. Use an f-string to print the values associated with each key.
# 
# **Hint** You must use both types of quotes. For example, to access a value in
# an f-string.
# 
# ```python
# f"{other_dct['apple']}"
# ```

#%%
other_dct = dct
print(other_dct)

#%%
print(f"{other_dct['apple']}, {other_dct['cherry']}, {other_dct['date']}")

#%%
# ### Exercise: Tuple Manipulation
# 
# 1. Create a tuple `tpl` containing 100 and 4
# 2. Convert to a list, add the elements 101 and 5
# 3. Convert back toa tuple

#%%
tpl = (100,4)
tpl = tuple(tpl)
print(tpl)
print(tpl[0])

#%%
converted_lst = [tpl[0], tpl[1]]
print(converted_lst)

#%%
conv_tpl = (converted_lst[0], converted_lst[1])
print(conv_tpl)
