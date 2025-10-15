# Import the csv module to work with CSV files
import csv

# Open the CSV file in read mode
# newline="" prevents extra blank lines on Windows
# encoding="utf-8" handles special characters properly
with open("data.csv", newline="", encoding="utf-8") as f:
    # Create a csv.reader object and convert all rows to a list
    # This loads the entire CSV into memory at once
    # reader becomes a list of lists: [['Name', 'Age'], ['John', '25'], ...]
    reader = list(csv.reader(f))

# Check if the file has any data before processing
if reader:
    # Calculate the maximum width needed for each column
    # zip(*reader) transposes rows into columns
    # For each column, find the longest cell value
    # col_widths becomes a list like [10, 5, 8] for each column's width
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(*reader)]

    # Loop through each row in the reader
    for row in reader:
        # For each cell in the row, convert to string and pad with spaces
        # ljust(width) adds spaces to the right until reaching the width
        # Join all cells with " | " separator
        # Example: "Name      | Age  | City    "
        print(
            " | ".join(str(cell).ljust(width) for cell, width in zip(row, col_widths))
        )
