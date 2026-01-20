total = 0

while True:
  num = float(input("Enter number to add(0 to stop): "))
  if num == 0:
    print("Exiting Sum")
    break
  total += num #total = total + num
print(total)

