# Python-Project

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
