# while True
# conditon
# break

while True:
  num = int(input("Enter a number: "))
  if num % 2 == 0:
    print("even")
  else:
    print("Odd")

  choice = input("Do you want to check another number? y/n: ")

  if choice == "n":
    print("Exiting Program")
    break

   