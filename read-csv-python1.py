# Import the csv module to work with CSV files
import csv

# Open the CSV file in read mode
# newline="" prevents extra blank lines on Windows
# encoding="utf-8" handles special characters properly
# The 'with' statement automatically closes the file when done
with open("data.csv", newline="", encoding="utf-8") as f:
    # Create a DictReader object that reads each row as a dictionary
    # Keys are column headers, values are cell contents
    reader = csv.DictReader(f)

    # Loop through each row in the CSV file
    for row in reader:
        # Print the row as a dictionary
        # Example output: {'Name': 'John', 'Age': '25', 'City': 'NYC'}
        print(row)
