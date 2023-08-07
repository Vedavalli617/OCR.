import pytesseract
import json
from datetime import datetime
import mysql.connector

def extract_text_from_image(image_path):
    try:
        # Extract text from the image using pytesseract
        extracted_text = pytesseract.image_to_string(image_path)
        
        # Prepare the data to be saved as JSON
        data = {"text": extracted_text}
        json_data = json.dumps(data)
        
        # Generate a unique timestamp for the JSON file name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        json_file = f"extracted_imagetext_{timestamp}.json"
        
        # Save the JSON data to a file
        with open(json_file, "w") as file:
            file.write(json_data)

        # Specify the path to the JSON file
        json_file = f"extracted_imagetext_{timestamp}.json"

        # Read the contents of the JSON file
        with open(json_file, "r") as file:
            json_data = file.read()

        # Remove newline characters from the JSON data
        json_data = json_data.replace("\n", " ")
        
        # Example: Remove a specific key from the JSON data
        '''if '\n' in json_data:
            del json_data['\n']'''

        # json_data = ''.join(json_data.split('\n'))
        # Write the modified JSON data back to the file
        with open(json_file, "w") as file:
            file.write(json_data)
        
        print("Newline characters removed from the JSON file.")
        # Step 1: Read the JSON file and parse it into Python data structures
        with open(json_file, 'r') as file:
            data = json.load(file)

        print("Text extracted and saved in", json_file)
    except Exception as e:
        print("An error occurred:", str(e))

# Ask the user to input the image file path
image_path = input("Enter the path to the image file: ")

# Call the function to extract text and save it in JSON
extract_text_from_image(image_path)
