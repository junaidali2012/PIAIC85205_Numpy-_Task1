#!/usr/bin/env python
# coding: utf-8

# # Reading Recipes 
# 
# Note: Data file is recipes.csv Attached with jupyter notebook
1. Start by importing NumPy as np
# In[1]:


import numpy as np


# 2. All of Alize’s recipes call for milk, eggs, sugar, flour, and butter. For example, her cupcake recipe calls for:
# 
# Flour Sugar Eggs Milk Butter 2 cups 0.75 cups 2 eggs 1 cups 0.5 cups Create a NumPy array that represents this data. Each element should be a number (i.e., 2 for “2 cups”). Save this array as cupcakes.

# In[3]:


cupcakes = np.array([2,0.75,2,1,0.5]) # creating numpy array from this given data
cupcakes


# 3. Alize’s assistant has compiled all of her recipes into a csv (comma-separated variable) file called recipes.csv. Load this file into a variable called recipes.
# 
# ###########Explore yourselves how to load a csv file in numpy#######

# In[8]:


import csv
from numpy import loadtxt # import csv file
recipes = loadtxt ('recipes.csv', delimiter=',')
recipes = np.array(recipes)
recipes


# 4.Display recipes using print.
# Display recipes using print.
# 
# 
# Each row represents a different recipe. Each column represents a different ingredient.
# 
# Recipe	       Cups of Flour	Cups of Sugar	Eggs	Cups of Milk	Cups of Butter
# 
# Cupcakes	         …	              …	          …	         …	              …
# 
# Pancake	             …                …	          …	         …	              …
# 
# Cookie	             …	              …	          …	         …	              …
# 
# Bread	             …	              …	          …	         …	              …

# In[10]:


print("Recipes_Cups of Flour_Cups of Sugar_Eggs_Cups of Milk_Cups of Butter")
print(f"Cupkcakes______{recipes[0][0]}________{recipes[0][1]}______{recipes[0][2]}_____{recipes[0][3]}__________{recipes[0][4]}") # same rows columns changing
print(f"Pancake________{recipes[1][0]}________{recipes[1][1]}______{recipes[1][2]}_____{recipes[1][3]}________{recipes[1][4]}")
print(f"Cookie_________{recipes[2][0]}________{recipes[2][1]}______{recipes[2][2]}_____{recipes[2][3]}__________{recipes[2][4]}")
print(f"Bread__________{recipes[3][0]}________{recipes[3][1]}______{recipes[3][2]}_____{recipes[3][3]}__________{recipes[3][4]}")


# 5.The 3rd column represents the number of eggs that each recipe needs.
# 
# Select all elements from the 3rd column and save them to the variable eggs.

# In[11]:


eggs = recipes[:,[2]]
eggs


# 6.Which recipes require exactly 1 egg? Use a logical statement to get True or False for each value of eggs.

# In[12]:


print(np.where(eggs==1.,True,False))
print("after using logical statement i know that Second & Third Recipies Exactly '1' Egg ")


# 7.Alize is going to make 2 batches of cupcakes (1st row) and 1 batch of cookies (3rd row).
# 
# You already have a variable for cupcakes. Create a variable for cookies with the data from the 3rd row.
# 

# In[13]:


cookies = recipes[2]  # RETRIVING DATA FROM 3RD ROW
cookies


# 8.
# Get the number of ingredients for a double batch of cupcakes by using multiplication on cupcakes. Save your new variable to double_batch.

# In[15]:


double_batch = cupcakes * 2 #DOUBLING THE CUPCAKES BY USING MULTIPLICAITON AND STORING INTO DOUBLE BATCH
double_batch


# 9.
# Create a new variable called grocery_list by adding cookies and double_batch.

# In[18]:


grocery_list = cookies + double_batch # ADDING COOKIES AND DOUBLE_BATCH
grocery_list


# In[16]:





# In[ ]:




