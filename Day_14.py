# 112. Using the Books.csv file from program 111, ask the user to enter another record and add it to the end of the file. Display each row of the .csv file on a separate line. 
#import csv
#file = open("books.csv", "a")
#book = input("enter another book: ")
#author = input("enter author: ")
#year = input("enter year: ")
#n_record = book + "," + author + "," + year + "\n"
#file.write(str(n_record))
#file.close
#file = open("books.csv", "r")
#for row in file:
#	print(row)
#file.close ()

# 113. Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many. After all the data has been added, ask for an author and display all the books in the list by that author. If there are no books by that author in the list, display a suitable message. 
#import csv

#num = int(input("how many records do you want to add to the list? "))
#file = open("books.csv", "a")
#for x in range (0, num):
#	book = input("enter a book: ")
#	author = input("enter author: ")
#	year = input("enter year: ")
#n_record = book + "," + author + "," + year + "\n"
#file.write(str(n_record))
#file.close ()

#ask_author = input("ask for an author: ")
#file = open("books.csv", "r")
#count = 0
#for row in file:
#	if ask_author in str(row):
#		print (row)
#		count == count + 1
#if count == 0:
#    	print("there are no book in the list by that author")
#file.close ()

# 114. Using the Books.csv file, ask the user to enter a starting year and an end year. Display all books released between those two years. 

#import csv
#s_year = int(input("enter a starting year: "))
#e_year = int(input("enter an end year: "))
#file = list (csv.reader(open("books.csv")))
#tmp = []
#for row in file:
#	tmp.append(row)
#x = 0
#for row in tmp:
#	if int(tmp[x] [2]) >= s_year and int(tmp[x] [2]) <= e_year:
#		print(tmp[x])
#x = x + 1

# 115. Using the Books.csv file, display the data in the file along with the row number of each
#import csv
#file = open("books.csv", "r")
#x = 0
#for row in file:
#	display = "Row: " + str(x) + "-" + row
#	print(display)
#	x = x + 1

# 117. Create a simple maths quiz that will ask the user for their name and then generate two random questions. Store their name, the questions they were asked, their answers and their final score in a .csv file. Whenever the program is run it should add to the .csv file and not overwrite anything.
#import csv
#import random

#score = 0
#name = input("what is your name? ") 
#q_num1 = random.randint (0, 10)
#q_num2 = random.randint (10, 50)
#que_1 = str(q_num1) + "+" + str(q_num2) + "="
#ans_1 = int(input(que_1))
#realans_1 = q_num1 + q_num2
#if ans_1 == realans_1:
#	score = score + 1
#q1_num1 = random.randint (0, 10)
#q2_num2 = random.randint (10, 50)
#que_2 = str(q1_num1) + "+" + #str(q2_num2) + "="
#ans_2 = int(input(que_2))
#realans_2 = q1_num1 + q2_num2
#if ans_2 == realans_2:
#	score = score + 1
#file = open("quizscore.csv", "a")
#n_record = name+","+que_1+","+#str(ans_1)+","+que_2+","+str(ans_2)+","+#str(score)+"\n"
#file.write(str(n_record))
#file.close ()






