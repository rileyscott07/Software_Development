import csv
from pathlib import Path

# __file__ means this Python file, and with_name points to the CSV beside it.
csv_file = Path(__file__).with_name("customers-100.csv")

# Open the CSV file so we can read its contents,newline="" prevents extra blank lines while reading the file
with csv_file.open(newline="", encoding="utf-8") as file:
	# list() stores all of those customer dictionaries in one list
	customers = list(csv.DictReader(file))

# Ask the user which customer row they want and turn the answer into a number
selected_customer = int(input("Enter the number of customer to display: "))

# Check that the selected number is between 1 and the number of rows
if 1 <= selected_customer <= len(customers):
	# lists start counting at 0, so subtract 1 to get the row the user expects
	customer = customers[selected_customer - 1]
	# Use the CSV headers to get and print this customer's first and last name
	print(customer["First Name"], customer["Last Name"])
else:
	# Show a helpful message if the user entered a row that does not exist
	print(f"Please enter a number from 1 to {len(customers)}.")