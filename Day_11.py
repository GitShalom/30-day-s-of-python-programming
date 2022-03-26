# 88. Ask the user for a list of five integers. Store them in an array. Sort the list and display it in reverse order. 
#from array import *
#number = array ("i", [])
#for i in range (0, 5):
#	num = int(input("enter one number: "))
#	number.append (num)
#numbers = sorted(number)
#number.reverse ()
#print(number)

# 89. Create an array which will store a list of integers. Generate five random numbers and store them in the array. Display the array (showing each item on a separate line). 

#from array import *
#import random
#num = array ("i", [])
#for i in range (0, 5):
#	list = random.randint (1, 50)
#	num.append(list)
#for i in num:
#	print (i)

# 90. Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array, otherwise display the message “Outside the range”. Once five numbers have been successfully added, display the message “Thank you” and display the array with each item shown on a separate line. 
#from array import *
#number = array ("i", [])
#while len(number) < 5:
#	num = int(input("enter a number between 10 and 20: "))
#	if num >= 10 and num <= 20:
#		number.append(num)
#	else:
#		print("outside the range")
#	for i in number:
#		print(i)

# 91. Create an array which contains five numbers (two of which should be repeated). Display the whole array to the user. Ask the user to enter one of the numbers from the array and then display a message saying how many times that number appears in the list. 
#from array import *
#number = array ("i", [3, 10, 8, 6, 3])
#for i in number:
#		print (i)
#num = int(input("enter one of the number: "))
#if number.count (num) == 1:
#	print(num, "is in the list once")
#else:
#	print(num,"is in the list", number.count(num), "times")

# 92. Create two arrays (one containing three numbers that the user enters and one containing a set of five random numbers). Join these two arrays together into one large array. Sort this large array and display it so that each number appears on a separate line. 
#from array import *
#import random

#num_1 = array ("i", [])
#num_2 = array ("i", [])
#for i in range (0, 3):
#	num = int(input("enter a num: "))
#	num_1.append (num)
#for i in range (0, 5):
#	num = random.randint (1, 50)
#	num_2.append (num)
#num_1.extend (num_2)
#num_1 = sorted (num_1)
#for i in num_1:
#	print(i)

# 93. Ask the user to enter five numbers. Sort them into order and present them to the user. Ask them to select one of the numbers. Remove it from the original array and save it in a new array. 
#from array import *
#number = array ("i", [])
#for i in range (0, 5):
#	num = int(input("enter a num: "))
#	number.append (num)
#number = sorted (number)
#for i in number:
#	print (i)
#num = int(input("select one of the num: "))
#if num in number:
#	number.remove (num)
#num_2 = array ("i", [])
#num_2.append (num)
#print (number)
#print (num_2)


		
	