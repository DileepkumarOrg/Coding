import pandas as pd
import requests
from pathlib import Path

# Load your Excel sheet
df = pd.read_excel('Pet_Store_Accessories.xlsx')

# Create a directory to save images
image_dir = Path('pet_images')
image_dir.mkdir(exist_ok=True)

# Function to download images
def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {url}")

# Iterate over the DataFrame and download images
for index, row in df.iterrows():
    product_name = row['Accessory Name']
    image_url = row['Image URL']  # Ensure this column exists in your Excel
    if pd.notna(image_url):  # Check if the URL is not NaN
        image_filename = image_dir / f"{product_name.replace(' ', '_')}.jpg"
        download_image(image_url, image_filename)