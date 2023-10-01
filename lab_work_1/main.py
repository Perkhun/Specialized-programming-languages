import math # To use the math function sqrt

# Function to check if a data can be converted to a float. If data can we convert it to float
def is_valid_float(data):
  try:
      float(data)
      return True
  except ValueError: # Error handling ValueError to check numbers
      return False

# Prompt the user to enter the number
def get_number_from_user(prompt):
    while True:
      num_input = input(prompt)
      if is_valid_float(num_input):
          return float(num_input)
      else:
          print("Invalid input. Please enter a valid number.")

# Prompt the user to enter an operator
def get_operator_from_user():
    valid_operators = ['+', '-', '*', '/', '^', '√', '%']
    while True:
      operator = input("Enter the operator (+, -, *, /,  ^, √, %): ")
      if operator in valid_operators:
          return operator
      else:
          print("Invalid operator. Please enter a valid operator from the list (+, -, *, /, ^, √, %): ")
         
# Perform calculations based on the operator which user entered
def perform_calculation(number1, number2, operator, decimal_places):
    result = None
    try:
      if operator == '+':
        result = number1 + number2
      elif operator == '-':
        result = number1 - number2
      elif operator == '*':
        result = number1 * number2
      elif operator == '/':
        # Check for division by zero
        if number2 == 0:
          # Generation of an exception, we create an instance of an exception of type ZeroDivisionError
          raise ZeroDivisionError("Error: Division by zero is not allowed")
        else:
            result = number1 / number2
      elif operator == '^':  # exponentiation
              result = number1 ** number2
      elif operator == '√':  # sqrt
              result = math.sqrt(number1)
      elif operator == '%':  # Remainder from division
           result = number1 % number2
      return result
    # Exception handling
    except ZeroDivisionError as e: # The variable e contains information about the exception
        print(e)    

def main():
    memory = None
    calculation_records = []
    while True:
       number1 = get_number_from_user("Enter the first number: ")
       number2 = get_number_from_user("Enter the second number: ")
       operator = get_operator_from_user()
       
       decimal_places = int(input("Enter the number of decimal places: "))
     
       result = perform_calculation(number1, number2, operator, decimal_places)

       if result is not None:
            memory = result

             # Store the calculation and expression in history
            expression = f"{number1:.{decimal_places}f} {operator} {number2:.{decimal_places}f} = {result:.{decimal_places}f}"
            calculation_records.append({"expression": expression, "result": result})
            
            # Display the result with the specified decimal places
            formatted_result = f"Result: {result:.{decimal_places}f}"
            print(formatted_result)

            # Display calculation history
            history_str = ", ".join([entry["expression"] for entry in calculation_records])
            print(f"Memory operator: {history_str}")
       else:
            # If result is None, continue to the next iteration without storing the calculation
            pass
       
       # Ask user if he wants to perform one more calculation
       another_calculation = input("Do you want to perform another calculation? (yes/no): ")
       if another_calculation.lower() != 'yes':
       # Exit if user doesn't want one more calculation
          break

if __name__ == "__main__":
    main()