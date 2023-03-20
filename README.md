# Python-Project

The Body Mass Index (BMI) Calculator can be used to calculate BMI value and corresponding weight status while taking height into consideration. It is used for both men and women, age 20 or older.

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
