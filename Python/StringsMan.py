"""s=['a','e','i','o','u']
s1="Routhu Dileep Kumar"
for i in s1:
    if i in s:
        print(i)
        """

import csv
import random

def generate_milk_data(num_records=1000):
    data = []
    for _ in range(num_records):
        fat = random.randint(0, 1)  # 0 for low, 1 for high
        color = random.randint(240, 255)  # Example range
        temperature = random.randint(2, 8)  # Example range
        turbidity = random.randint(0, 1)  # 0 for low, 1 for high

        # More realistic grade generation example (still simplified)
        if fat == 1 and turbidity == 0:  # High fat, low turbidity
            grade = "high"
        elif fat == 0 and turbidity == 1: # low fat, high turbidity
            grade = "low"
        elif fat == 1 and turbidity == 1: # high fat, high turbidity
            grade = "medium"
        else: # low fat, low turbidity
            grade = "medium"

        data.append([fat, color, temperature, turbidity, grade])
    return data

def write_to_csv(data, filename="milk_data.csv"):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Fat (Binary)", "Color", "Temperature (C)", "Turbidity (Binary)", "Grade"])  # Header row
        writer.writerows(data)

if __name__ == "__main__":
    milk_data = generate_milk_data()
    write_to_csv(milk_data)
    print(f"Generated {len(milk_data)} records and saved to milk_data.csv")