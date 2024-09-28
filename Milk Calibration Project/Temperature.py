import os
import glob
import time
import csv

# Load the required kernel modules
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Base directory for temperature sensor data
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# Name of the CSV file
filename = "temperature_readings.csv"

# Check if the file already exists
file_exists = os.path.isfile(filename)


def read_temp_raw():
    """Reads the raw temperature data from the sensor."""
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines


def read_temp():
    """Parses and returns the temperature in Celsius and Fahrenheit."""
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f


# Infinite loop to keep reading the temperature and saving it to the CSV file
while True:
    temp_c, temp_f = read_temp()  # Get temperature in Celsius and Fahrenheit
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp

    # Append the temperature data to the CSV file
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write header only if the file does not exist
        if not file_exists:
            writer.writerow(['Timestamp', 'Temperature_C', 'Temperature_F'])
            file_exists = True  # Set this to True after the first write

        # Write the current temperature data with a timestamp
        writer.writerow([current_time, temp_c, temp_f])

    print(f"{current_time}: {temp_c} °C / {temp_f} °F")
    time.sleep(1)