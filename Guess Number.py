#!/usr/bin/env python
# coding: utf-8

# In[3]:


#THIS CODE MADE BY RISHAB SINGH ARTICLE and The code by mindnijaX
#I just type the code again

#notes:
#1. randint() function from random module

import random
#initialize max_num variable for maximal number
max_num = 30
#generate number betweet 1 and maximal number
random_number = random.randint(1,max_num)
#initialize guess to store the comparison beteenplaer guess
guess=0
#to keep asking the playir
while guess != random_number:
    guess = int(input(f"Guess the number between 1 & {max_num}:"))
    if guess < random_number:
        print("Wrong! Too Low...")
    elif guess > random_number:
        print("Wrong! Too High...")
print(f"That's right! Random number is {random_number}")


# In[ ]:




