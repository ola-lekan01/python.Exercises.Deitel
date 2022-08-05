grade = int(input("Enter Score: "))

if grade >= 70 and grade <= 100:
    print("Your Grade is A ")
if grade >= 60 and grade <= 69:
    print("Your Grade is B")
if grade >= 50 and grade <= 59:
    print("Your Grade is c")
if grade >= 45 and grade <= 49:
    print("Your Grade is D")
if grade >= 40 and grade <= 44:
    print("Your Grade is E")
if grade < 40 and grade >= 0:
    print("Your Grade is F")
else:
    print("Wrong input")