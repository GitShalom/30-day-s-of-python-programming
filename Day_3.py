# 20. Ask the user to enter their first name and then display the length of their name.
#first_name = input("enter your first_name: ")
#length = len(first_name)
#print (length)

# 21. Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of whole name. 
#first_name = input("enter your first_name: ")
#surname = input("enter your surname: ")
#name = first_name +" " + surname
#length = len(name)
#print (name)
#print (length)

# 22. Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.
#first_name = input("enter your first name in lowercase: ") 
#surname = input("enter your surname in lowercase: ")
#first_name = first_name.title ()
#surname = surname.title ()
#name = first_name + " " + surname
#print (name)

# 23. Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1).
#rhyme = input("type in the first line of a nursery rhyme: ") 
#length = len(rhyme)
#print ("this has", length, " letters in it")
#start = int(input("enter a starting number: "))
#end = int(input("enter an ending number: "))
#part = (rhyme[start:end])
#print (part)

# 24. Ask the user to type in any word and display it in upper case. 
#user = input("type in any word: ")
#user = user.upper ()
#print (user)

# 25. Ask the user to enter their first name. If the length of their first name is under five characters, ask them to enter their surname and join them together (without a space) and display the name in upper case. If the length of the first name is five or more characters, display their first name in lower case. 
#name = input("enter your first_name: ")
#if len(name) < 5:
#	surname = input("enter your surname: ")
#	name = name+surname
#	print (name.uppercase ())
#else:
#	print (name.lowercase ())

# 26. Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case. 
