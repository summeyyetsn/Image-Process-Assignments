#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [
    [4,8,2],
    [9,5,1]
    ]
print(a)


# In[3]:


import numpy as np
A = np.array([[1,2,3],[4,5,6]])
print(A)


# In[4]:


array = np.zeros((2,3))
print(array)


# In[6]:


array1=np.ones((8,4))
print(array1)


# In[8]:


num1 = 25
num2 = 5 
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
print(f"toplam={sum} , fark={sub}, çarpım={mul}, bölüm={div}")


# In[12]:


x=10
print(x)
x+=5
print(x)
x-=2
print(x)


# In[15]:


number = int(input("Enter a number: "))
if number>0:
    print("Number is POSITIVE! ")
elif number<0:
    print("Number is NEGATIVE! ")
else:
    print("Number is ZERO !")


# In[21]:


for i in range(10):
    print(f"--> {i}")


# In[24]:


for j in range(15,10,-1):
    print(f"--> {j}")


# In[25]:


my_name="Seher Sümeyye Tosun"
for letter in(my_name):
    print(letter)


# In[41]:


arr=[1,4,6,8,2,7,3,7]
length=len(arr)
sum = 0
i = 0
while i < length:
    sum = sum + arr[i]
    i = i+1
print("Sum", sum)


# In[48]:


def sum_function(a,b):
    summation = a + b
    print(summation)
x = 10
y = 24
sum_function(x,y)
sum_function(50,74)


# In[ ]:




