number = int(intput("Enter a number: "))

if not number.isdigit():
  print("Invalid input")
else:
  number = int(number)
  
if number % 2 == 0:
  print("The number", number, "is even")
else:
  print("The number", number, "is odd")
