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
while True:
	# Print Menu
	print("= = = = = M E N U = = = = =")
	print("   1 -> Add New Profile ")
	print("   2 -> Search Database")
	print("   3 -> Exit Program")
	print("= = = = = = = = = = = = = =")
	print()
	# Input Function
	whatDo = int(input("What do you want to do? (1-3): "))

	if whatDo == 1:
		# Values to insert in database 
		name = input("Full Name:    ")
		age  = input("Age:          ")
		civStat = input("Civil Status: ")
		occup = input("Occupation:   ")
		addre = input("Address:      ")
		contact = input("Contact No.:  ")
		print("= = = = = S A V E D = = = = =")
		# Insert values into database
		database[name] = { 
		"Full Name   " : name,
		"Age         " : age,
		"Civil Status" : civStat,
		"Occupation  " : addre,
		"Contact No. " : contact
		}

	if whatDo == 2:
		name = input("Full Name: ")
		print("= = = = = = = = = = = = = =")
		print()
		if name in database:
			for key in database[name]:
				print("  ", key, ":", database[name][key])
		else:
			print("Profile does not exist")
		print()

	if whatDo == 3:
		confirm = input("Exit? (y/n): ")
		if confirm == "y":
			print()
			print("= = = E X I T I N G = = =")
			exit()
	# Loop from Print Menu
