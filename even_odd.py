#Program created to determine if a number is even or odd 
#Even and Odd Number Checker with Validation
while True:
try:
number = int(input("Enter a number: "))

if number % 2 == 0:
print("The number is EVEN")
else:
print("The number is ODD")

except ValueError:
print("PLease enter a valid integer: ")

choice = input ("Do you want to try again? (yes/no): ").lower()
if choice != "yes":
print("Program ended.")
break
