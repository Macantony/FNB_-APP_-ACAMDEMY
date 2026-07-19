# collect user info
First = input("Enter your first name: ")
Last = input("Enter your last name: ")
Bio = input(" Enter your bio: ")
#create a username (first initial + last name in lowercase)
username = (First[0] + Last).lower()
# full name in title case
Full_name = (f" {First} {Last}").title()
# remove all all whitespace from the bio using .strip()
New_bio = Bio.strip()
#Replacing "I AM" with "I'M" in tthe bio
bio = New_bio.replace("I am","I'M")
# counting the number of characters in the bio
Bio_lenght = len(bio)
# displaying all output using f-strings
print(f"\n              User Profile")
print(f"Full Name : {Full_name}")
print(f"Username  : {username}")
print(f"BIO       : {bio}")
print(f"Bio lenght: {Bio_lenght}")
