#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random


# In[ ]:


def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 6
    for attempt in range(max_attempts):
        guess = int(input("Enter your guess "))
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else :
            print("Congrats, you guessed it :) !!!")
            break
    if guess != random_number: 
        print(f"Too bad :( , the number was {random_number}")
        
number_guessing_game()


# In[ ]:




