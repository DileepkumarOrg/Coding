# Taking two inputs from the user in a single line using map
input_values = map(int, input("Enter two numbers separated by space: ").split())

# Extracting the values from the map object
num1, num2 = input_values

# Printing the inputs
print("First number:", num1)
print("Second number:", num2)
