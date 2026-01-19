# Taking input from user
num1 = float(input("Enter first number: "))
operation = input("Enter +,-,*,/: ")
num2 = float(input("Enter second number: "))


if operation == "+":
  print(num1 + num2)
elif operation == "-":
  print(num1 - num2)
elif operation == "*":
  print(num1 * num2)
elif operation == "/":
  if num2 != 0:
    print(num1/num2)
  else:
    print("We cannot divide by 0")
else:
  print("Invalid Operation.")      
  





