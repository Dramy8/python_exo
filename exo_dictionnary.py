#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#dico

#1
persona = {
    'name': 'Elie',
    'job': 'Instructor'
}
print(persona)

#2
states = {}

key = ["CA","NJ","RI"]
values = ["California", "New Jersey", "Rhode Island"]
for k in range(3):
    states[key[k]] = values[k]
print(states)

#3
dico = {}
vowels = ['a','e','i','o','u']
for v in vowels: 
    dico[v]= 0
print(dico)

#4
alphabet = {}
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
place = 1

for l in letter: 
    alphabet[place]= l
    place += 1
    
print(alphabet)

