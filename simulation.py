#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd

df = pd.DataFrame()
np.random.seed(123)


# In[2]:


#1) How likely is it that you roll doubles when rolling two dice?

n_trials = nrows = 10_000
n_dice = ncols = 2

rolls = np.random.choice([1, 2, 3, 4, 5, 6], n_trials * n_dice).reshape(nrows, ncols)
rolls


# In[53]:


#From review

n_rows = 10_000
n_cols = 2 #represents rolling 2 dice during each simulation

rolls = np.random.choice([1,2,3,4,5,6], size = (n_rows , n_cols)) #6-sided die
rolls = pd.DataFrame(rolls , columns = ["die1", "die2"]) #turn into dataframe bc easier to manipulate
rolls.head()


# In[54]:


#how many outcomes from die match each other?
#what's the chance of rolling doubles?

(rolls.die1 == rolls.die2).mean()


# In[3]:


# 2) If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of 
# getting more than 3 heads?

n_trials = nrows = 10_000
n_dice = ncols = 8

rolls = np.random.choice(['Heads', 'Tails'], size = 80_000).reshape(nrows, ncols) #creates array

coin_flips = np.random.choice(['Heads', 'Tails'], size = (10_000, 8))
n_heads = (coin_flips == 'Heads').sum(axis = 1) #axis = 1 sums rows, default behavior is to sum columns
(n_heads == 3).mean() #0.2201
(n_heads > 3).mean() #0.6312


# In[56]:


#from review

n_rows = 10_000
n_cols = 8 #for flipping 8 coins at once

flips = np.random.choice(["Heads", "Tails"], size = (10_000 , 8))
flips = pd.DataFrame(flips) #turn into dataframe to make data manipulation easier


# In[57]:


flips["n_heads"] = (flips == "Heads").sum(axis = 1)
flips.head()


# In[58]:


flips["n_tails"] = (flips == "Tails").sum(axis = 1)


# In[60]:


#what's the probability of gettting exactly 3 heads?
(flips.n_heads == 3).mean()


# In[61]:


#whats' the prbability of getting more than 3 heads?
(flips.n_heads > 3).mean()


# In[4]:


# 3) There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming 
# that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards 
# I drive past both have data science students on them?

#75% chance (0.75) of devs, 25%(0.25) of ds students


billboard_sim = np.random.choice(['DS', 'Dev'],
                                p = [.25, .75],
                                size = (10_000, 2))
((billboard_sim == 'DS').sum(axis = 1) == 2).mean()


# In[62]:


# from review

n_rows = 10_000
n_cols = 2 # for 2 billboards in a row

billboards = np.random.choice(["Web Development" , "Data Science"],
                             p = [.75, .25],
                             size =(n_rows , n_cols))

billboards = pd.DataFrame(billboards) #turn into dataframe


# In[63]:


billboards["number_of_data_science"] = (billboards == "Data Science").sum(axis = 1)
(billboards.number_of_data_science == 2).mean()


# In[5]:


# 4) Codeup students buy, on average, 3 poptart packages with a standard deviation of 1.5 a day from the snack 
#vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will 
#be able to buy some poptarts on Friday afternoon? (Remember, if you have mean and standard deviation, 
#use the np.random.normal)

#mean = 3
#std = 1.5/day

poptarts = round((np.random.normal(loc = 3, scale = 1.5, size = (10_000, 5)).sum(axis = 1) < 17).mean() * 100,2)
print(f'The likelihood of being able to buy poptarts on Friday afternoon is {poptarts}%')
#5 is the number of days, so the number of 'trials' is 10,000 and the 5th day, are there less than 17 


# In[64]:


#from review

n_rows = 10_000
n_cols = 5 #to represent a 5 day week

mean = 3
std = 1.5

poptarts = np.random.normal(mean, std, size = (n_rows , n_cols)).round()
poptarts = pd.DataFrame(poptarts, columns = ["Mon", "Tues", "Wed", "Thurs", "Fri"])


# In[65]:


poptarts["n_consumed"] = poptarts.sum(axis = 1)
poptarts.head()


# In[66]:


#What's the chance we can buy poptarts Friday afternoon
#This setup would predicate
(poptarts.n_consumed < 17).mean()


# 
# 
# Compare Heights
# 
#     Men have an average height of 178 cm and standard deviation of 8cm.
#     Women have a mean of 170, sd = 6cm.
#     Since you have means and standard deviations, you can use np.random.normal to generate observations.
#     If a man and woman are chosen at random, what is the likelihood the woman is taller than the man?
# 
# 

# In[6]:


mens_heights = (np.random.normal(178, 8, 10_000))
womens_heights = (np.random.normal(170, 6, 10_000))

(womens_heights > mens_heights).mean()


# When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted 
# and the installation fails. What are the odds that after having 50 students download anaconda, no one has an 
# installation issue? 100 students? What is the probability that we observe an installation issue within the 
# first 150 students that download anaconda? How likely is it that 450 students all download anaconda without an issue?

# In[13]:


#will use booleans, True represents corrupted download
#propbability of 1/250 = 0.004 & 249/250 = .996

n_downloads = 50 #number of students downloads
anaconda_sim = np.random.choice(
                                [True, False],
                                p = [.004, .996],
                                size = (10_000, n_students))

corrupted_percent = round((1 - anaconda_sim.any(axis = 1).mean()) * 100, 2) 
print(f'The chances of uncorrupted downloads out of {n_downloads} is {corrupted_percent}%' )


# In[14]:


n_downloads = 100
anaconda_sim = np.random.choice(
                                [True, False],
                                p = [1/250, 249/250],
                                size = [10_000, n_students])
corrupted_percent = round((1 - anaconda_sim.any(axis = 1).mean()) * 100, 2)
print(f'The chances of uncorrupted downloads out of {n_downloads} is {corrupted_percent}%')


# In[15]:


n_downloads = 150
anaconda_sim = np.random.choice(
                                [True, False],
                                p = [1/250 , 249/250],
                                size = [10_000, n_students])

corrupted_percent = round((1 - anaconda_sim.any(axis = 1).mean()) * 100, 2)
print(f'The chances of uncorrupted downloads out of {n_downloads} is {corrupted_percent}%')


# In[16]:


n_students = 450
anaconda_sim = np.random.choice([True, False],
                               p = [1/250, 249/250],
                               size = [10_000, n_students])

corrupted_percent = round((1 - anaconda_sim.any(axis = 1).mean()) * 100, 2)
print(f'The chances of uncorrupted downloads out of {n_downloads} is {corrupted_percent}%')


# In[46]:


# from review

n_rows = 100_000
n_cols = 50

installs = np.random.choice([0 , 1],
                           p = [0.004, 0.996],
                           size = (n_rows , n_cols))

(installs.sum(axis = 1) == 50).mean()


# In[48]:


n_cols = 100

installs = np.random.choice([0 , 1],
                           p = [0.004, 0.996],
                           size = (n_rows , n_cols))

(installs.sum(axis = 1) == 100).mean()


# In[49]:


n_cols = 150

installs = np.random.choice([0 , 1],
                           p = [0.004 , 0.996],
                           size = (n_rows , n_cols ))

(installs.sum(axis = 1) == 150).mean()


# In[50]:


n_cols = 450

installs = np.random.choice([0 , 1],
                           p = [0.004 , 0.996],
                           size = (n_rows , n_cols))

(installs.sum(axis = 1) == 450).mean()


# 
# 
# There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?
# 
# How likely is it that a food truck will show up sometime this week?
# 

# In[21]:


foodtruck_sim = np.random.choice(['Food Truck', 'No Food Truck'],
                                p = [.7, .3],
                                size = [10_000, 5])

foodtruck_percent = round(((foodtruck_sim == 'Food Truck').any(axis = 1).mean()) * 100, 2)

print(f'The chances of a foodtruck showing up is {foodtruck_percent}%')


# In[34]:


#from review:
n_rows = 10_000
n_cols = 3 #to represent 3 days in a row

trucks = np.random.choice([1 , 0],
                         size = [n_rows , n_cols],
                         p = [0.7, 0.3])
(trucks.sum(axis = 1) > 0).mean()


# In[28]:


trucks_percent = round(((trucks.sum(axis = 1) > 0).mean()) * 100, 2)
print(f'The chances of a foodtruck showing up is {trucks_percent}%')


# If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?

# In[52]:


simulation = np.random.randint(1, 366, size = (10_000, 23))
simulation = pd.DataFrame(simulation)
(simulation.apply(lambda birthdays: birthdays.nunique(), axis = 1) < 23).mean()


# In[35]:


# from review

n_rows = 10_000
n_cols = 23 #to represent 23 individuals

birthdays  = np.random.choice(range(365), size = (n_rows , n_cols))
birthdays = pd.DataFrame(birthdays)
birthdays["n_unique"] = birthdays.nunique(axis = 1)

#whats the proportion of rows where we have multiple shared days
(birthdays.n_unique != 23).mean()


# In[38]:


n_rows = 10_000
n_cols = 20 #to represent 20 individuals

birthdays =np.random.choice(range(365), size = (n_rows, n_cols))
birthdays = pd.DataFrame(birthdays)
birthdays["n_unique"] = birthdays.nunique(axis = 1)


(birthdays.n_unique != 20).mean()


# In[41]:


n_rows = 10_000
n_cols = 40 #to represent 40 individuals

birthdays = np.random.choice(range(365), size = (n_rows, n_cols))
birthdays = pd.DataFrame(birthdays)
birthdays["n_unique"] = birthdays.nunique(axis = 1)

(birthdays.n_unique != 40).mean()


# In[44]:


#graph of rooms of increasing size

x = range(1, 100)

#N will be a list of N for each room size
N = [n * (n-1) / 2 for n in x]

#Get the probability for each N
y = [1 - (364 / 365) **n for n in N]


# In[45]:


import matplotlib.pyplot as plt

plt.title("Probability of at least two people sharing a birthday")
plt.plot(x , y)
plt.xlabel("Number of people in the room")
plt.ylabel("Probability")


# In[ ]:





# In[ ]:




