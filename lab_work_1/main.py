while True:
# Function to check if a data can be converted to a float. If data can we convert it to float
  def is_valid_float(data):
    try:
        float(data)
        return True
    except ValueError:
        return False

# Prompt the user to enter the first number
  while True:
    num1_input = input("Enter the first number: ")
    if is_valid_float(num1_input):
        number1 = float(num1_input)
        break
    else:
        print("Invalid input. Please enter a valid number.")

# Prompt the user to enter the second number
  while True:
    num2_input = input("Enter the second number: ")
    if is_valid_float(num2_input):
        number2 = float(num2_input)
        break
    else:
        print("Invalid input. Please enter a valid number.")

# Prompt the user to enter an operator
  valid_operators = ['+', '-', '*', '/']
  while True:
    operator = input("Enter the operator (+, -, *, /): ")
    if operator in valid_operators:
        break
    else:
        print("Invalid operator. Please enter a valid operator from the list (+, -, *, /).")

# Perform calculations based on the operator which user entered
  if operator == '+':
    result = number1 + number2
  elif operator == '-':
    result = number1 - number2
  elif operator == '*':
    result = number1 * number2
  elif operator == '/':
    # Check for division by zero
    if number2 == 0:
        result = "Error: Division by zero is not allowed"
    else:
                result = number1 / number2
   

# Display the result
  print("Result:", result)

#Ask user if he wants to perform one more calculation
  another_calculation = input("Do you want to perform another calculation? (yes/no): ")
  if another_calculation.lower() != 'yes':
        #exit if user doesn't want one more calculation
        break
 