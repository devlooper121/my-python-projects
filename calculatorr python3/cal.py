# Calculator

# add
def add(n1, n2):
  return n1 + n2

# substract
def substract(n1, n2):
  return n1 - n2

# multiply
def multiply(n1, n2):
  return n1 * n2

# divide
def div(n1, n2):
  return n1 / n2

operations = {
  "+" : add, 
  "-" : substract,
  "*" : multiply,
  "/" : div,
  }
def calculator(n1, n2, operator):
  if operator in operations:
    current_func = operations[operator]
    return current_func(n1,n2)
  

from art_cal import logo
print(logo)

num1 = int(input("Enter first number: "))
print("Operators: ")
for op in operations:
  print(op)
calculating = True

while calculating:
  operator = input("Choose operator : ")
  num2 = int(input("Enter next number: "))
  answer = calculator(num1,num2, operator)
  print(f"{num1} {operator} {num2} = {answer}.")
  continue_or_not = input("Type 'y' to continue calculations : ").lower()
  if continue_or_not == 'y':
    num1 = answer
  else:
    calculating = False
