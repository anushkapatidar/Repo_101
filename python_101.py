def check_integer(x):
    if not isinstance(x, int):
        raise TypeError("Error: x must be an integer.")  # Raise TypeError if x is not an integer
    return f"The value of x is: {x}"

# Get user input
try:
    user_input = input("Enter a value for x: ")  # Prompt for input
    # Attempt to convert the input to an integer
    x = int(user_input)  
    result = check_integer(x)  # Check if x is an integer
    print(result)  # Print the result if valid
except ValueError:
    print("Error: Please enter a valid integer.")  # Handle invalid integer conversion
except TypeError as e:
    print(e)  # Print the TypeError message if raised
