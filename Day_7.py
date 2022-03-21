# 52. Display a random integer between 1 and 100 inclusive.
#import random
#num = random.randint (1, 100)
#print (num)

# 53. Display a random fruit from a list of five fruits. 
#import random
#fruit = random.choice (["orange", "grape", "apple", "carrot", "cherry"])
#print (fruit)

# 54. Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the same as the randomly selected value, display the message “You win”, otherwise display “Bad luck”. At the end, tell the user if the computer selected heads or tails. 
#import random
#choice = random.choice ("h" or "t")
#make_choice = input("make your choice (h) or (t): ")
#if make_choice == choice:
#	print("you win")
#else:
#	print("bad luck")
#if choice == "h":
#	print("it's head")
#else:
#	print("it's tail")

# 55. Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly, display the message “Well done”, otherwise tell them if they are too high or too low and ask them to pick a second number. If they guess correctly on their second guess, display “Correct”, otherwise display “You lose”. 
#import random
#num = random.randint (1, 5)
#guess = int(input("enter a num: "))
#if guess == num:
#	print("well done")
#elif guess > num:
#	print("too high")
#	guess = int(input("guess for the second time: "))
#	if guess == num:
#		print("correct")
#	else:
#		print("you lose")
		
#elif guess < num:
#	print("too low")
#	guess = int(input("guess for the second time: "))
#	if guess == num:
	#		print("correct")
#	else:
#		print("you lose")
		
# 56. Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until they enter the number that was randomly picked.
#import random
#whole_num = random.randint(1, 10) 
#correct = False
#while correct == False:
#	num = int(input("enter a number: "))
#	if num == whole_num:
#		correct = False

# 57. Update program 056 so that it tells the user if they are too high or too low before they pick again.
#import random
#whole_num = random.randint(1, 10) 
#correct = False
#while correct == False:
#	num = int(input("enter a number: "))
#	if num == whole_num:
#		correct = False
#	elif num > whole_num:
#		print("too high")
#	else:
#		print("too low")
 
