# 69. Create a tuple containing the names of five countries and display the whole tuple. Ask the user to enter one of the countries that have been shown to them and then display the index number (i.e. position in the list) of that item in the tuple. 
countries_tuple = ("uk", "asia", "dubia", "ghana", "korea")
print (countries_tuple)
countries = input("enter one of the countries above: ")
print(countries, "index number", countries_tuple.index(countries))

# 70. Add to program 069 to ask the user to enter a number and display the country in that position.
countries_tuple = ("uk", "asia", "dubia", "ghana", "korea")
print(countries_tuple)
countries = input("enter one of the countries above: ")
print(countries, "index number", countries_tuple.index(countries))
num = int(input("enter a number between 0 and 4: "))
print (countries_tuple[num])

# 71. Create a list of two sports. Ask the user what their favourite sport is and add this to the end of the list. Sort the list and display it. 
sports = ["soccer", "hockey"]
sports.append(input("what is your favourite sport? "))
sports.sort ()
print (sports)

# 72. Create a list of six school subjects. Ask the user which of these subjects they don’t like. Delete the subject they have chosen from the list before you display the list again.
subjects_list =  ["math", "English", "chemistry", "biology", "computer", "physics"]
print (subjects_list)
dont_like = input("which of the subject don't you like? ")
delete = subjects_list.index(dont_like)
del subjects_list [delete]
print(subjects_list)

# 73. Ask the user to enter four of their favourite foods and store them in a dictionary so that they are indexed with numbers starting from 1. Display the dictionary in full, showing the index number and the item. Ask them which they want to get rid of and remove it from the list. Sort the remaining data and display the dictionary. 
food_dictionary = {}
food_1 = input("enter your favorite food: ")
food_dictionary [1] = food_1
food_2 = input("enter second favorite food: ")
food_dictionary [2] = food_2
food_3 = input("enter third favorite food: ")
food_dictionary [3] = food_3
food_4 = input("enter fourth favorite food: ")
food_dictionary [4] = food_4
print(food_dictionary)
get_rid = int(input("which do you want to get rid of? "))
del food_dictionary[get_rid]
print(sorted(food_dictionary.values ()))

# 74. Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and an end number between 5 and 9. Display the list for those colours between the start and end numbers the user input. 
colours = ["green", "orange", "blue", "yellow", "red", "purple", "pink", "lialac", "grey", "black"]
start = int(input("enter a start num between (0-4): "))
end = int(input("enter an end number between (5-9): "))
print (colours[start:end])

# 75. Create a list of four three-digit numbers. Display the list to the user, showing each item from the list on a separate line. Ask the user to enter a three-digit number. If the number they have typed in matches one in the list, display the position of that number in the list, otherwise display the message “That is not in the list”. 
num = [256, 257, 258, 259]
for i in num:
	print(i)
ran_pick = int(input("enter a three-digit number: "))
if ran_pick in num:
	print(ran_pick, "is in position", num.index(ran_pick))
else:
	print("that is not in the list")

# 76. Ask the user to enter the names of three people they want to invite to a party and store them in a list. After they have entered all three names, ask them if they want to add another. If they do, allow them to add more names until they answer “no”. When they answer “no”, display how many people they have invited to the party. 
name_1 = input("enter one name: ")
name_2 = input("enter second name: ")
name_3 = input("enter third name: ")
party = [name_1, name_2, name_3]
ano_name = input("do you want to add another name? y/n: ")
while ano_name == "y":
	more_names = party.append(input("enter new name: "))
	ano_name = input("do you want to add another name? y/n: ")
	print("you have", len(party), "people coming to the party")

# 77. Change program 076 so that once the user has completed their list of names, display the full list and ask them to type in one of the names on the list. Display the position of that name in the list. Ask the user if they still want that person to come to the party. If they answer “no”, delete that entry from the list and display the list again.
name_1 = input("enter one name: ")
name_2 = input("enter second name: ")
name_3 = input("enter third name: ")
party = [name_1, name_2, name_3]
ano_name = input("do you want to add another name? y/n: ")
while ano_name == "y":
	more_names = party.append(input("enter new name: "))
	ano_name = input("do you want to add another name? y/n: ")
	print("you have", len(party), "people coming to the party")
	print(party)
pick = input("enter one of name: ")
print(pick, "is in selection", party.index(pick), "on the list")
stillcome = input("do you want that person to come? y/n: ")
if stillcome == "n":
	party.remove(pick)
	print(party)

# 78. Create a list containing the titles of four TV programmes and display them on separate lines. Ask the user to enter another show and a position they want it inserted into the list. Display the list again, showing all five TV programmes in their new positions.
tv_prog = ["task", "gear", "harry potter", "the promise"]
for i in tv_prog:
	print(i)
ano_show = input("enter another show: ")
position = int(input("enter a number between (0-3): "))
tv_prog.insert(position, ano_show)
for i in tv_prog:
	print(i)

	

