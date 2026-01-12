import random

secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:
    guess = int(input("Enter a number between 1 and 10: "))

    if guess == secret_number:
        print("You guessed it!")
    elif guess > secret_number:
        print("Too High")
    else:
        print("Too Low")
