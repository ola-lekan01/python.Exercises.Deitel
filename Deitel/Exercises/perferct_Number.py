number = int(input("Enter a number: "))

fact: int = 1
total: int = 0
while fact < number:
    if number % fact:
        total += fact
    fact +=1

if total == number:
    print(number , "is a perfect Number")

elif total > number:
    print(number , "is an abundant Number")

else:
    print(number , "is a Deficent Number")
