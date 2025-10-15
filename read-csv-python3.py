# Import the csv module to work with CSV files
import csv

# Open the CSV file in read mode
# newline="" prevents extra blank lines on Windows
# encoding="utf-8" handles special characters properly
with open("data.csv", newline="", encoding="utf-8") as f:
    # Read all rows from the CSV file into a list
    # reader becomes a list of lists containing all CSV data
    reader = list(csv.reader(f))

# Check if file has at least headers and one data row
if len(reader) > 1:
    # Create new headers by adding "ID" column at the beginning
    # reader[0] contains the original header row
    # headers becomes ["ID", "Name", "Age", "City"]
    headers = ["ID"] + reader[0]

    # Create new rows with row numbers added as first column
    # reader[1:] skips the header row and gets all data rows
    # enumerate(reader[1:], start=1) gives (1, row1), (2, row2), etc.
    # Each new row is [row_number] + original_row
    # rows becomes [[1, 'John', '25'], [2, 'Jane', '30'], ...]
    rows = [[i] + row for i, row in enumerate(reader[1:], start=1)]

    # Calculate column widths by comparing headers and all data rows
    # zip(headers, *rows) transposes data into columns
    # For each column, find the maximum length needed
    # This ensures both headers and data fit properly
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(headers, *rows)]

    # Print the header row
    # For each header and its width, pad the header with spaces
    # ljust(w) adds spaces to the right until reaching width w
    # Join all headers with " | " separator
    print(" | ".join(h.ljust(w) for h, w in zip(headers, col_widths)))

    # Print a separator line under the headers
    # sum(col_widths) adds up all column widths
    # 3 * (len(col_widths) - 1) accounts for " | " separators between columns
    # Creates a line of dashes like "----------|----|--------"
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))

    # Loop through each data row
    for row in rows:
        # For each cell, convert to string and pad with spaces
        # ljust(w) adds spaces to the right until reaching width w
        # Join all cells with " | " separator
        # Example: "1  | John      | 25   | NYC     "
        print(" | ".join(str(c).ljust(w) for c, w in zip(row, col_widths)))
else:
    # If file is empty or has only headers, print error message
    print("CSV file is empty or contains only headers")
