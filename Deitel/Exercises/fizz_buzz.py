for number in range(0,101,1):
    if number % 3 and number % 5:
        print(number, "Fizz Buzz")

    elif number % 3:
        print(number, "Fizz")

    elif number % 5:
        print(number, "Buzz")

    else:
        print(number, "Neither a FIzz nor a Buzz")
