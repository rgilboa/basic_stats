#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt #imports matplotlib under alias plt for brevity

def basicStats(x):

    for i in x: # Iterate on the values in the sample to find out how many there are
      length = i + 1 
#     print('The sample x contains this many values:'); print(length) # Print the number of values in the sample
    
    sum = 0 #Declare a variable called sum
    for i in x: #Enter for loop iterating on sample list
      sum = sum + x[i] #add the value of x at the current loop index on each iteration
#     print('The sum of the values in x is:'); print(sum)

    mean = sum/length #compute the mean using the precalculated values of sum and length
#     print('The mean of x is:'); print(mean) #Print to the console
    
    std_sum = 0
    for a in x:
      std_sum = std_sum + (x[a]-mean)**2

    std_dev = (std_sum/(length-1))**0.5
#     print('The standard deviation of the values in x is:'); print(std_dev)
    
#     print('The mean of x is:'); print(mean) #Print to the console
#     print('The standard deviation of the values in x is:'); print(std_dev)
    
    count = 0
    for i in x: #For each loop iteration, compare a value of x-mu to the standard dev. If the difference is less than mu, add one to the count.
        if abs(x[i]-mean) < std_dev:
            count = count + 1
#     print('There are this many values of x within one standard deviation of the mean:'); print(count)
    
        
    x = [x]
    plt.hist(x, bins = [0, 5, 10, 15, 20, 25])
    plt.show()
    
    return mean, std_dev

