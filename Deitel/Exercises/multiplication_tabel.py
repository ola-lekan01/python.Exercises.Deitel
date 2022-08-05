number = 13

for num in range(1, number):
    print()
    print(num, "times tables")
    for num2 in range(1, number):
        print(num, "*" , num2,"=", num * num2)