print("Hello Welcome to Calculator 4.0.")
print("you have five operators you can choose from.")
num = input("Enter any of these charactars for the exact answer +,-,*,/,**: ")
a = float(input("Please enter your first number: "))
b = float(input('Please enter your second number: '))
answer = 0
if num == "+":
  answer = a + b 
elif num == "-":
  answer = a - b
elif num == "*":
  answer = a * b
elif num == "/":
  answer = a / b
elif num == "**":
  answer = a ** b
else:
  print("Invalid operator, please try again.")
print("Your answer is", a, num , b, "=", answer) 
print("Thank you for using Calculator pro, have a nice day.")
