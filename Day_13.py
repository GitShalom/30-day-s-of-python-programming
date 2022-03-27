# 105. Write a new file called “Numbers.txt”. Add five numbers to the document which are stored on the same line and only separated by a comma. Once you have run the program, look in the location where your program is stored and you should see that the file has been created. The easiest way to view the contents of the new text file on a Windows system is to read it using Notepad. 
file = open ("Numbers.txt", "w")
file.write("5 ")
file.write("6")
file.write("7")
file.write("8")
file.write("9")
file.close ()

# 106. Create a new file called “Names.txt”. Add five names to the document, which are stored on separate lines. Once you have run the program, look in the location where your program is stored and check that the file has been created properly. 
file = open ("Names.txt", "w")
file.write("shalom\n")
file.write("love\n")
file.write("joseph\n")
file.write("blessing\n")
file.write("endurance\n")
file.close ()

# 108. Open the Names.txt file. Ask the user to input a new name. Add this to the end of the file and display the entire file
file = open ("Names.txt", "a")
n_name = input("enter a name: ")
file.write(n_name + "\n")
file.close
file = open ("Names.txt", "r")
print(file.read ())
file.close

# 110. Using the Names.txt file you created earlier, display the list of names in Python. Ask the user to type in one of the names and then save all the names except the one they entered into a new file called Names2.txt
file = open ("Names.txt", "r")
print(file.read ())
file.close ()
file = open ("Names.txt", "r")
s_name = input("enter a name from the list: ")
s_name = s_name + "\n"
for row in file:
	if row != s_name:
		file = open("Names2.txt", "a")
		n_record = row
		file.write(n_record)
		file.close ()
file.close()

