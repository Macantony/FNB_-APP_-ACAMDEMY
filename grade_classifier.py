# input learner details
Name = input("Enter your learner name: ")
sub1 = input("Enter your first subject name  ")
sub2 = input("Enter your second subject name : ")
sub3 = input("Enter your third subject name : ")
# asking for marks 
marks1 = float(input(f"Enter your marks for {sub1} : "))
marks2 = float(input(f"Enter your marks for {sub2} : "))
marks3 = float(input(f"Enter your marks for {sub3} : "))
#calculate the average mark fot the three subjects
Average_mark = (marks1+marks2+marks3)/3
# determine grade
if Average_mark >= 80:
    grade ="A"
elif Average_mark >= 70:
    grade = "B"
elif Average_mark >= 60:
    grade ="C"
elif Average_mark >= 50:
    grade = "D"
else:
    grade = "F"
# Determine pass/fail status
if Average_mark >= 50:
    Status ="Pass"
else:
    Status = "Fail"
# flag any individual subjects 40 below as 'intervention needed'
Intervention = ""
if marks1 <= 40:
    Intervention +=f"Intervention is needed in {sub1}\n"
if marks2 <= 40 :
    Intervention +=f"Intervention is needed in {sub2}\n"
if marks3 <= 40 :
    Intervention +=f"Intervention needed in {sub3}\n"
if Intervention == "":
    Intervention = "No Intervention is needed"
print("         REPORT CARD")
print(f"Student name: {Name}")
print(f"{sub1}: {marks1}")
print(f"{sub2}: {marks2}")
print(f"{sub3}: {marks3}")
print(f"Average : {Average_mark}")
print(f"Grade: {grade}")
print(f"Status: {Status}")
print(f"Interventation:{Intervention}")