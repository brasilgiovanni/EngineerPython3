#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create a code that calculate the perimeter and area of a simple square
# Notice: the user needs be able to provide the dimension

lado = float(input("Enter here the sides value of square: "))
x = 4*lado
y = lado**2
print('perimeter: ',x, '- área: ',y)


# In[ ]:


# Here, we will create a code able to calculate the notes mean

# Importing the statistics module 
from statistics import mean
  
# list of positive integer numbers
note01 = float(input('Type the first note here: '))
note02 = float(input('Type the second note here: '))
note03 = float(input('Type the third note here: '))
note04 = float(input('Type the fourth note here: '))
notes = [note01, note02, note03, note04]
  
mean_notes = mean(notes) 
  
# Printing the mean 
print("The arithmetic mean is", mean_notes)


# In[ ]:


# Getting information of user

name = input('Enter your name here: ')
v_day = input('Type the expiration day: ')
v_month = input('Type the expiration month: ')
v_invoice = input('Type the value [R$]: ')
print('Olá,', name)
print('Your invoice due on', v_day,'of', v_month, 'with value R$', v_invoice,'is closed.')


# In[ ]:


# Now we can see a example using the operations [//] and [%]
# we want to calculate the number of days, hours and minutes, when the user enter with seconds
# The operations [//] results in interger number of division, no decimal part
#  - Example: 150 // 4 == 37, beacuse 150 / 4 = 37,50, so the integer part is 37.0, and 0,50 is a decimal.
# the operations [%] results in rest of a division 
# - Example: 150 % 4 == 2, beacuse 150/2 == 75 and 75 / 2 there is no interger number, so the rest of division is 2.

n_seconds = float(input('Por favor, entre com o número de segundos que deseja converter: '))
day = int(n_seconds // 86400)
hour = int(n_seconds % 86400 // 3600)
minute = int(n_seconds % 86400 % 3600 // 60)
seconds = int(n_seconds % 86400 % 3600 % 60)
print(day,'days,',hour,'hours,',minute,'minutes and',seconds,'seconds')


# In[34]:


# Here we exercise one more time the use of operations [//] and [%]
# But now, we want to discover the number that represents the ten digits

n_int = int(input('Enter here a integer number (no float): '))
aux = n_int // 10
aux2 = aux % 10
print(f'The ten digits is: {aux2}')

