import csv

# Data with headers
data = [
    ['Name', 'Age', 'City']
]

# Ask the user how many records they want to add
num_records = int(input("How many records do you want to add? "))

# Collecting records from the user
for _ in range(num_records):
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")
    data.append([name, age, city])

# Name of the CSV file
filename = "example.csv"

# Writing to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Data has been written to {filename}")