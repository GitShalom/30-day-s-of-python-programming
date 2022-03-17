# 12. Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.
num_1 = int(input("enter first_num: "))
num_2 = int(input("enter second_num: "))
if num_1 > num_2:
	print (num_2, num_1)
else:
	print (num_1, num_2)

# 13. Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, otherwise display “Thank you”.
num = int(input("enter a number under 20: "))
if num >= 20:
	print ("Too high")
else:
	print ("Thank you")

# 14. Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”. 
user = int(input("enter a number between 10 and 20: "))
if user >= 10 and user <= 20:
	print ("Thank you")
else:
	print ("incorrect answer")

# 15. Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”. 
colour = input("enter favourite colour: ")
if colour == "red" or colour == "RED" or colour == "Red":
	print ("i like red too")
else:
	print("i don't like that colour, i prefer red")

# 16. Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the answer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”. If they did not answer yes to the first question, display the answer “Enjoy your day”. 
user = input("is it raining? ")
user = str.lower (user)
if user == "yes":
	windy = input("is it windy? ")
	windy = str.lower (windy)
elif windy == "yes":
	print ("is it too windy for an umbrella")
elif:
	print ("take an umbrella")
else:
	print ("enjoy your day")

# 17. Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, display the message “You can learn to drive”, if they are 16, display the message “You can buy a lottery ticket”, if they are under 16, display the message “You can go Trickor-Treating”. 
age = int(input("how old are you? "))
if age >=18:
	print ("you can vote? ")
elif age == 17:
	print ("you can learn to drive")
elif age == 16:
	print ("you can buy a lottery ticket")
else:
	print ("you can go Trickor-Treating")

# 18. Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is between 10 and 20, display “Correct”, otherwise display “Too high”. 
user = int(input("enter a number: "))
if user <= 10:
	print ("too low")
elif user >=10 and user <=20:
	print ("correct")
else:
	print ("too high")

# 19. Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”. 
user = input("enter 1, 2, or 3: ")
if user == "1":
	print ("thank you")
elif user == "2":
	print ("well done")
elif user == "3":
	print ("correct")
else:
	print ("error message")
	
	




		
	