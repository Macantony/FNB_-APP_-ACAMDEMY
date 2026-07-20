# set a fixed varriable representing the current balance
balance = 1000
# ask the user the amount he/she wants to withdraw
amount = float(input("Enter the amount you want to withdraw: R"))
# use if, when  the amount is less than or equal to the balance if not use e
if amount <= 0 :
    print("Invalid amount. You must withdraw more than R0")
elif amount <= balance :
    print(f"Withdrawal was successfully! Remaining balance: {round(balance-amount,2)}")
else:
    print("Declined.Insuffictent funds")