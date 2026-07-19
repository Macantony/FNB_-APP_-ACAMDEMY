#asking user for their password
Password = input("Enter your password:")
# Use strip to remove accidental spaces from the password
password = Password.strip()
# grab the very first and last letter of the password
First_letter = password[0]
last_letter = password[-1]
# Display the hint
print(f"Your password hint: It starts with {First_letter.upper()} and ends with {last_letter.upper()} .")
