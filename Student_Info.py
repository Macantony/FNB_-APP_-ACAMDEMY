# Collect user info
First_Name = input( "What is your first name: ")
Surname = input(" What is your Surname: ")
Age = int(input("What is your Age: "))
Favourite_Number = float(input("What is your Favourite NUmber: "))
# greeting
print(f"Weclome ,{First_Name} {Surname}" )
# String manipulation
print(f"Name in UPPERCASE:{First_Name.upper()} {Surname.upper()}")
print(f"Name in Title case: {First_Name.title()}{Surname.title()}")
#Arithmetic Calculatoin
age_in_months = Age *12
print(f"Age in month: {age_in_months}")
# Round favourite number
rounded_number = round(Favourite_Number,2)
print(f"Favourite number rounded to 2 decimal places: {rounded_number}")
#display data types
print(" DATA TYPES")
print(f"First Name: {type(First_Name)}")
print(f"Surname: {type(Surname)}")
print(f"Age:{type(Age)}")
print(f"Favourite Number: {type(Favourite_Number)}")