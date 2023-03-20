#!/usr/bin/env python
# coding: utf-8

# In[33]:


name = input("Enter your name: ")
weight = int(input("Enter your weight in pound: "))
height = int(input("Enter your height in feet: "))
BMI = (weight * 703) / (height * height)

print(BMI)
if BMI>0:
    if(BMI<18):
        print("You are Normal.")
    elif(BMI<25):
        print("You are heathly weight.")
    elif(BMI<30):
        print("You are Obese Class I.")
    elif(BMI<5):
        print("You are Obese Class II.")   
    else:
        print("Enter valid inputs")


# In[32]:





# In[29]:


if BMI>0:
    if(BMI<18.5):
        print(name +", you are underwight.")
    elif (BMI<=24.9):
        print(name +", you are normal weight.")
    elif (BMI<29.9):
        print(name +", you are overweight. You need to exercise more and stop sitting and writing so many python tutorials.")
    elif (BMI<34.9):
        print(name +", you are obese.")
    elif (BMI<39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid input")


# In[ ]:


Mild Thinness	17 - 18.5
Normal	18.5 - 25
Overweight	25 - 30
Obese Class I	30 - 35
Obese Class II	35 - 40
Obese Class III	> 40


# In[22]:


if BMI>0:
    if(BMI<18.5):
        print(name +", you are underwight.")
    elif (BMI<=24.9):
        print(name +", you are normal weight.")
    elif (BMI<29.9):
        print(name +", you are overweight. You need to exercise more and stop sitting and writing so many python tutorials.")
    elif (BMI<34.9):
        print(name +", you are obese.")
    elif (BMI<39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid input")


# In[ ]:





# In[ ]:





# In[ ]:




