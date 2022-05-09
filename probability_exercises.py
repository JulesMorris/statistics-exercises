#!/usr/bin/env python
# coding: utf-8

# In[29]:


import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd


# In[7]:


# 1) A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a 
# Poisson distribution with a mean of 2 cars. Make a chart of this distribution and answer these questions 
# concerning the probability of cars waiting at the drive-up window.

λ = 2

x = np.arange(0 , 10, 1)
y = stats.poisson(λ).pmf(x) #pmf used because seeking prob of single outcome

plt.bar(x, y)
plt.xticks(np.arange(0, 10, 1)) #had to include because was only showing values by 2's


# In[8]:


# What is the probability that no cars drive up in the noon hour?

stats.poisson(λ).pmf(0) #pmf used bc seeking probability of single outcome


# In[10]:


# What is the probability that 3 or more cars come through the drive through? 
    
stats.poisson(λ).sf(2) #use number - 1 here bc its prob of random variable falling above certain value


# In[12]:


#alternatively cdf can be used with same value:

1 - stats.poisson(λ).cdf(2)


# In[16]:


# How likely is it that the drive through gets at least 1 car? 
  
1 - stats.poisson(λ).pmf(0)     #why am I doing 1 - the distribution here? b/c you're adding up all the bars(likelihood) excluding through 1


# In[29]:


stats.poisson(λ).pmf(0) #represents the 0% probability that at least 1 car will come through, to exclude that 
# to answer the question, it's 1 - distribution... 1 - 0.1353352832366127 = 0.8646647167633873


# In[31]:


#alternative
stats.poisson(λ).sf(0) 


# Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. Calculate the following:
# 
#     What grade point average is required to be in the top 5% of the graduating class?
#     What GPA constitutes the bottom 15% of the class?
#     An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?
#     If I have a GPA of 3.5, what percentile am I in?
# 
# 

# In[ ]:


# Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of 
# .3. Calculate the following:

# stats.norm(mean, std) bc normal distribution    


# In[17]:


# What grade point average is required to be in the top 5% of the graduating class?

stats.norm(3, .3).isf(0.05)


# In[18]:


# What GPA constitutes the bottom 15% of the class?
stats.norm(3, 0.3).ppf(.15)


# In[20]:


# An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class.
#Decile means sorting data 10 equal parts, so third decile would be from 20 - 30 %? 1st = 0-10%, 2nd = 10-20%
stats.norm(3, 0.3).ppf([0.2, 0.3])    
    


# In[3]:


#from review 
# another method

np.quantile(np.random.normal(3, 0.3, 10_000), [0.2, 0.3])


# In[23]:


# If I have a GPA of 3.5, what percentile am I in?
stats.norm(3, 0.3).cdf(3.5)
stats.norm(3, 0.3).cdf(3.5) * 100 #95th percentile


# In[5]:


#by Simulation

#(np.random.normal(mean, std, trial_num).mean())

(np.random.normal(3, 0.3, 10_000) < 3.5).mean() * 100


# In[8]:


#A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 
# click-throughs. How likely is it that this many people or more click through?

#A binomial distribution is defined by a number of trials, and a probability of success.

n = 4326 #number of visitors (trials)
p = 0.02 # avg click rate, (probability)
stats.binom(n, p).sf(96) #97 - 1 "or more" is crucial, sf is not inclusive, so to get 97, must subtract 1


# In[6]:


# from review (simulation)
clicks = np.random.choice([0,1], (100_000, 4326), p = [0.98 , 0.02])

(clicks.sum(axis = 1) >= 97).mean()


# In[9]:


# from review (Poisson approximation)
λ = n * p
stats.poisson(λ).sf(96)


# You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question.
# 
# What is the probability that at least one of your first 60 answers is correct?
# 
# 

# In[30]:


n = 60 #number of questions out of 100 being examined
p = 0.01 

stats.binom(n, p).sf(0) 


# In[12]:


# From review (simulation)

answers = np.random.choice([0 , 1], (10_000 , 60), p = [0.99, 0.01])
(answers.sum(axis = 1) >= 1).mean()


# The codeup staff tends to get upset when the student break area is not cleaned up. Suppose that there's a 3% 
# chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of 
# the 3 active cohorts of 22 students visit the break area. How likely is it that the break area gets cleaned 
# up each day? How likely is it that it goes two days without getting cleaned up? All week?

# In[15]:


# How likely is it that the break area gets cleaned up each day?

n = .9 * 3 * 22
p = 0.03

stats.binom(n, p).sf(0)


# In[33]:


#How likely is it that the break area gets cleaned up each day? L & V
stats.binom(n, p).pmf(5)


# In[16]:


# How likely is it that it goes two days without getting cleaned up?

stats.binom(n * 2, p).pmf(0)


# In[17]:


# All week?
stats.binom(n * 5, p).pmf(0)


# In[18]:


#alternatively

1 - stats.binom(n * 5, p).sf(0)


# In[19]:


#from review
x = np.arange(0,9)
y = stats.binom(n , p).pmf(x)
plt.bar(x, y, width = 0.9)
plt.xlabel("Number of times area is cleaned per day")


# You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

# In[22]:


#from review

#convert to minutes

# mean number of minutes = 15 * 2 = 30 mins
# std = 3 * 2 = 6 mins
# max time I can be in line without getting late to class = 60(total mins for lunch) - 15(Avg # ppl in line) - 10(food order to arrival time) - 2(order time) = 33 minutes
mean = 15 * 2 
std = 3 * 2


stats.norm(30, 6).cdf(33)


# In[23]:


#by simulation
(np.random.normal(30, 6, 100_000) < 33).mean()


# In[24]:


x = np.arange(0, 60, 0.1)
y = stats.norm(mean, std).pdf(x)

plt.plot(x , y)
plt.vlines(33, 0, stats.norm(mean, std).pdf(33), ls = '--', color = 'r')
plt.ylim(0, 0.07)


# In[ ]:





# In[27]:


#by simulation
#33 mins/2 = 16.5 people

(np.random.normal(15, 3, 100000) < 16.5).mean() 


# Connect to the employees database and find the average salary of current employees, along with the standard deviation. For the following questions, calculate the answer based on modeling the employees salaries with a normal distribution defined by the calculated mean and standard deviation then compare this answer to the actual values present in the salaries dataset.
# 
#    a) What percent of employees earn less than 60,000?
#    b) What percent of employees earn more than 95,000?
#    c) What percent of employees earn between 65,000 and 80,000?
#    d) What do the top 5% of employees make?
# 

# In[30]:


#review

from env import get_db_url

url = get_db_url('employees')
query = """
SELECT *
FROM salaries s
WHERE s.to_date > Now()
"""

salaries = pd.read_sql(query, url)


# In[31]:


salaries


# In[33]:


#calculate mean and std from the data above

mean = salaries.salary.mean()
std = salaries.salary.std()


# In[34]:


mean, std


# In[35]:


#what percent of employees earn less than $60,000?
stats.norm(mean, std).cdf(60000)


# In[36]:


#what percent of employees earn more than 95,000?

stats.norm(mean, std).sf(95000) #no need to subtract 1 in sf because the difference would be negligable on number so large


# In[37]:


#what percent of employees earn between 65,000 and 80,000?

np.diff(stats.norm(mean, std).cdf([65000 , 80000]))


# In[39]:


#what do the top 5% of employees make?

round(stats.norm(mean, std).isf(0.05), 2)


# In[ ]:




