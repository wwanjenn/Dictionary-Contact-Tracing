# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

# Example Output:

# Menu:
#  1 -> Add an item
#  2 -> Search
#  3 -> Exit (y/n)

# What do you want to do? (1-3): 1
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# Saved!
# What do you want to do? (1-3): 2
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890What do you want to do? (1-3): 3
# Exit? n
database = {}
# Print Menu
print()
print("= = = = = M E N U = = = = =")
print("   1 -> Add New Profile ")
print("   2 -> Search Database")
print("   3 -> Exit Program")
print("= = = = = = = = = = = = = =")
print()
# Input Function
whatDo = int(input("What do you want to do? (1-3): "))

if whatDo == 1:
	name = input("FullName:     ")
	age  = input("Age:          ")
	civStat = input("Civil Status: ")
	occup = input("Occupation:   ")
	addre = input("Address:      ")
	contact = input("Contact #:    ")

# Loop from Print Menu
