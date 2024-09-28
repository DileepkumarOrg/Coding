"""import pandas as pd

df = pd.DataFrame(columns=['Name', 'Age', 'City'])
num_records = int(input("How many records do you want to add? "))
for _ in range(num_records):
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")
    # Append the user input as a new row to the DataFrame
    df = df.append({'Name': name, 'Age': age, 'City': city}, ignore_index=True)

filename = "example_pandas.csv"
df.to_csv(filename, index=False)
print(f"Data has been written to {filename}")
"""
"""import pandas as pd

# Create an empty DataFrame with column names
df = pd.DataFrame(columns=['Name', 'Age', 'City'])

# Ask the user how many records they want to add
num_records = int(input("How many records do you want to add? "))

# Collecting records from the user and appending to the DataFrame
for _ in range(num_records):
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")

    # Creating a temporary DataFrame for each new row
    new_row = pd.DataFrame({'Name': [name], 'Age': [age], 'City': [city]})

    # Concatenating the new row with the existing DataFrame
    df = pd.concat([df, new_row], ignore_index=True)

# Name of the CSV file
filename = "example_pandas.csv"

# Writing the DataFrame to a CSV file
df.to_csv(filename, index=False)

print(f"Data has been written to {filename}")"""

"""import pandas as pd
import os

# Name of the CSV file
filename = "example_pandas.csv"

# Check if the file already exists
file_exists = os.path.isfile(filename)

# Create an empty DataFrame with column names (for new entries)
df = pd.DataFrame(columns=['Name', 'Age', 'City'])

# Ask the user how many records they want to add
num_records = int(input("How many records do you want to add? "))

# Collecting records from the user and appending to the DataFrame
for _ in range(num_records):
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")

    # Creating a temporary DataFrame for each new row
    new_row = pd.DataFrame({'Name': [name], 'Age': [age], 'City': [city]})

    # Concatenating the new row with the existing DataFrame
    df = pd.concat([df, new_row], ignore_index=True)

# Writing the DataFrame to the CSV file in append mode
df.to_csv(filename, mode='a', header=not file_exists, index=False)

print(f"Data has been appended to {filename}")

"""

"""import csv
import os

# Name of the CSV file
filename = "example.csv"

# Check if the file already exists
file_exists = os.path.isfile(filename)

# Collecting records from the user
num_records = int(input("How many records do you want to add? "))

# Writing to the CSV file in append mode
with open(filename, mode='a', newline='') as file:
    writer = csv.writer(file)

    # Write the header only if the file doesn't exist
    if not file_exists:
        writer.writerow(['Name', 'Age', 'City'])

    # Collect records and write them to the CSV file
    for _ in range(num_records):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        city = input("Enter City: ")
        writer.writerow([name, age, city])

print(f"Data has been appended to {filename}")
"""

import csv
import os

# Name of the CSV file
filename = "example.csv"

# Check if the file already exists
file_exists = os.path.isfile(filename)

# Collecting records from the user
num_records = int(input("How many records do you want to add? "))

# Writing to the CSV file in append mode
with open(filename, mode='a', newline='') as file:
    writer = csv.writer(file)

    # Write the header only if the file doesn't exist
    if not file_exists:
        writer.writerow(['Temperature', 'pH', 'Turbidity'])

    # Collect records and write them to the CSV file
    for _ in range(num_records):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        city = input("Enter City: ")
        writer.writerow([name, age, city])
print(f"Data has been appended to {filename}")