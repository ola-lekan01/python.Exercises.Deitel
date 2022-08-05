number = int(input("Enter Number: "))
flag = False
if number > 2:
    for num in range(2, number):
        if number % num == 0:
            flag = True
            break
if flag:
     print(number , "is not a Prime number")
else:
    print(number, "is a prime number")