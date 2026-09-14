from datetime import date  # Import the date class from datetime module

# Open the file 'poo_tracker.txt' in read and write mode
with open('poo_tracker.txt', 'r+') as file:  
    content = file.read()  # Read the entire content of the file
    print(content)  # Print the content of the file to the console
    # Prompt the user for input and convert it to an integer
    todays_poos = int(input("How many times have you pooped today? ")) 
    # Write the current date to the file, turning it to a string and adding a new line
    file.write(str(date.today()) + '\n')
    # Check if the user pooped exactly once
    if todays_poos == 1:
        file.write(f"{todays_poos} poo\n")  # Write "1 poo" to the file
    # Check if the user pooped more than once
    elif todays_poos > 1:
        file.write(f"{todays_poos} poos\n")  # Write the number of poops with "poos" to the file
    # If the user didn't poop at all
    else: 
        file.write("No poos today\n")  # Write "No poos today" to the file