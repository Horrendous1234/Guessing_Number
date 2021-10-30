import random

number = random.randint(1, 100)
guessed_number = int(input("Enter your number"))

while True:
    guessed_number = int(input("Enter your number"))
    if number == guessed_number:
        print("You guessed it right")
        exit()

    elif guessed_number > number:
        print("The guessed number is greater than number ")
    elif guessed_number < number:
        print("The guessed number is less than number")


