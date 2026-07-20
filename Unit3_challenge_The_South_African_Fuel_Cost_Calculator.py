#Ask the user for info
Km = float(input("Enter how many kilometers you want to drive: "))
Petrol = float(input("Enter the current pertol price per litre: R"))
# Assume thier car uses excalty 1 litre of fuel for every 10 kilometers driven
litres_needed = Km/10
# Calculate the total cost
total_cost = litres_needed*Petrol
# print the final cost with 2 decimal points
print(f"The final cost is R{round(total_cost,2)}")