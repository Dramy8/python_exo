#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ex1

#1
listing = [1,2,3,4]
for val in listing:
    print(val)
    
    
    
#2
listing = [1,2,3,4]

for l in listing: 
    print(l * 20)


    
#3
names = ["Elie", "Tim", "Matt"]
letters = []

for name in names:
    letters.append(name[0])

print(letters)



#4
new = [1,2,3,4,5,6]

pairs = []

for n in new:
    if n % 2 == 0:
        pairs.append(n)

print(pairs)


#5
s = [1, 2, 3, 4]
t = [3, 4, 5, 6]
common = []

for n in s:
    if n in t:
        common.append(n)

print(common)

#6
words = ["Elie", "Tim", "Matt"]

new_words = []

for word in words:
    new_words.append(word.lower()[::-1])

print(new_words)


#7
s = "first"
t = "third"
common = []

for n in s:
    if n in t:
        common.append(n)

print(common)


#8
result = []
for number in range(1,101):
    if number % 12 == 0: 
        result.append(number)
print(result)

#9
nvx = []
word = "amazing"
vowel = ["a","e","i","o","u"]
for letter in word:
    if not letter in vowel:
        nvx.append(letter)
print(nvx)


#10
values =[]
add = ([0,1,2])
for val in range(3):
    values.append(add)
    
print(values)

#11
structure =[]
suite = ([0,1,2,3,4,5,6,7,8,9])
for su in range(10):
    structure.append(suite)
    
for su in structure:
    print(su)


# In[ ]:




