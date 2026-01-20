import random #import random module


# random_number = random.randint(1,6) # Include last number
# random_number = random.randrange(1,7) # Exlude last number


secret = random.randint(1,10)

print("Guess a number from 1 to 10.")

while True:
  guess = int(input("Enter a number: "))

  if guess == secret:
    print("You Guess Correct!!!")
    break
  elif guess < secret:
    print("Try Higher Number.")
  else:
    print("Try Lower")  




