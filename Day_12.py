# 96. Create the following using a simple 2D list using the standard Python indexing:
#simple_array = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
#print(simple_array)

# 97. Using the 2D list from program 096, ask the user to select a row and a column and display that value. 
#simple_array = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
#row = int(input("select a row: "))
#column = int(input("select a column: "))
#print (simple_array [row] [column])

# 98. Using the 2D list from program 096, ask the user which row they would like displayed and display just that row. Ask them to enter a new value and add it to the end of the row and display the row again. 
#simple_array = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
#row = int(input("enter a row: "))
#print(simple_array [row])
#n_value = int(input("enter a new value: "))
#simple_array[row].append(n_value)
#print(simple_array[row])

# 99. Change your previous program to ask the user which row they want displayed. Display that row. Ask which column in that row they want displayed and display the value that is held there. Ask the user if they want to change the value. If they do, ask for a new value and change the data. Finally, display the whole row again
#simple_array = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
#row = int(input("enter a row: "))
#print(simple_array [row])
#column = int(input("enter a column: "))
#print(simple_array[row][column])
#c_value = input("do you want to change the value? y/n: ")
#if c_value == "y":
#	n_value = int(input("enter a new value: "))
#	simple_array[row][column] = n_value
#	print(simple_array[row])

# 100. Create the following using a 2D dictionary showing the sales each person has made in the different geographical regions: 
#sales = {"john":{"N": 3056, "S": 8463, "E": 8441, "W": 2694}, "Tom":{"N": 4832, "S": 6786, "E": 4737, "W": 3612}, "Anne":{"N": 5239, "S": 4802, "E": 5820, "W": 1859}, "Fiona":{"N": 3904, "S": 3645, "E": 8821, "W": 2451} }

# 101. Using program 100, ask the user for a name and a region. Display the relevant data. Ask the user for the name and region of data they want to change and allow them to make the alteration to the sales figure. Display the sales for all regions for the name they choose
#sales = {"john":{"N": 3056, "S": 8463, "E": 8441, "W": 2694}, "Tom":{"N": 4832, "S": 6786, "E": 4737, "W": 3612}, "Anne":{"N": 5239, "S": 4802, "E": 5820, "W": 1859}, "Fiona":{"N": 3904, "S": 3645, "E": 8821, "W": 2451} }
#name = input("enter a name: ")
#region = input("enter a region: ")
#print(sales[name][region])
#n_data = int(input("enter a new data: "))
#sales[name][region] = n_data
#print(sales[name])

# 102. Ask the user to enter the name, age and shoe size for four people. Ask for the name of one of the people in the list and display their age and shoe size
#list = {}
#for i in range (0, 4):
#	name = input("enter a name: ")
#	age = int(input("enter age: "))
#	s_size = int(input("enter shoe size: "))
#list[name] = {"age":age, "shoe size":s_size}
#ask = input("enter the name: ")
#print(list [ask])



	