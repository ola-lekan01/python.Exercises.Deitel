import random

random_number = random.randint(0, 100)

count = 0;
while (count < 3):
    guess_number = int(input("Enter Number: "))

    if(guess_number == random_number):
        print("You are a lucky Guesser")

    if (guess_number < random_number):
        print("Number too Small, Try again")

    if (guess_number > random_number):
        print("Number too High, Try again")

    count+=1

print("You have Exhausted your Trials")

range_number = list(range(0, 100, 5))
print(range_number)

for range_number in range(0,200,10):
    print(range_number , end=" ")