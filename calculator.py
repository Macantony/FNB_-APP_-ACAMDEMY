#using input to collect the two numbers from the user
Num_1 = float(input("Enter your first number: "))
Num_2 = float(input("Enter your second number: "))
# Using Arithmrtic operators for calculation and rounding them by 2
print(f"Addition : {round(Num_1+Num_2,2)}")
print(f"Subraction: {round(Num_1-Num_2,2)}")
print(f"Multiplication: {round(Num_1*Num_2,2)}")
#Incase the second consist of zero 
if Num_2 !=0:
   print(f"Division: {round(Num_1/Num_2,2)}")
   print(f"Floor Division:{round(Num_1//Num_2,2)}")
   print(f"Modulus: {round(Num_1%Num_2,2)} ")
else:
    print("Division: Can not be divided by zero")
    print("Floor Division:Can not be divided by zero ")
    print("Modulus: Can not be divided by zero")