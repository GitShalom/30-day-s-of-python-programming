# 35. Ask the user to enter their name and then display their name three times. 
name = input("enter your name: ")
for i in range (0, 3):
	print(name)

# 36. Alter program 035 so that it will ask the user to enter their name and a numbe and then display their name that number of times. 
name = input("enter your name: ")
number = int(input("enter a number: "))
for i in range (0, number):
	print(name)

# 37. Ask the user to enter their name and display each letter in their name on a separate line.
name = input("enter your name: ") 
for i in name:
	print(name)

# 38. Change program 037 to also ask for a number. Display their name (one letter at a time on each line) and repeat this for the number of times they entered
name = input("enter your name: ")
number = int(input("enter a number: "))
for i in name:
    for x in range (0, number):
    	print(i)

# 39. Ask the user to enter a number between 1 and 12 and then display the times table for that number. 
number = int(input("enter a number between 1 and 12: "))
for i in range (1, 13):
    ans = number * i
    print(number, "x", i, "=", ans)

# 40. Ask for a number below 50 and then count down from 50 to that number, making sure you show the number they entered in the output. 
number = int(input("enter a number below 50: "))
for i in range (50, number - 2, -2):
	print(i) 

# 41. Ask the user to enter their name and a number. If the number is less than 10, then display their name that number of times; otherwise display the message “Too high” three times. 
name = input("enter your name: ")
number = int(input("enter a number: "))
if number < 10:
	for i in range (0, number):
		print(number)
	else:
		for i in range (0, 4):
			print("too high")

# 42. Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that number included. If they do, then add the number to the total. If they do not want it included, don’t add it to the total. After they have entered all five numbers, display the total.
total = 0
for i in range (0, 5):
	num = int(input("enter five numbers: "))
	answer = input("do you want that number included? (y/n) ")
	if answer == "y":
		total = num + total
		print(total)

# 43. Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number and then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down from 20 to that number. If they entered something other than up or down, display the message “I don’t understand”. 
direction = input("which direction do you want to count? (up or down) : ")

if direction == "up":
	top_number = int(input('what is your top number : '))
	for i in range(1, top_number + 1):
		print(i)
		
elif direction == 'down':
	number_below = int(input(' Enter a number below 20 : '))
	for i in range(20, number_below - 1, -1):
		print(i)
	
else:
	print(' Invalid option selected \n Try again.')

# 44. Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. If they enter a number which is 10 or higher, display the message “Too many people”. 
invite = int(input("how many people do you want to invite to the party? "))
if invite < 10:
	for i in range (0, invite):
		name = input("what is your name? ")
		print(name, "has been invited")
	else:
		print("too many people")
	
	