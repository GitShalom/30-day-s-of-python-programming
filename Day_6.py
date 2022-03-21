# 45. Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. Add that number to the total and print the message “The total is… [total]”. Stop the loop when the total is over 50. 
total = 0
while total <= 50:
	number = int(input("enter a number: "))
	answer = number + total
	print ("the total is", answer)

# 46. Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message “The last number you entered was a [number]” and stop the program
value = int(input("enter a number: "))
while value <= 5:
	print("the last number you entered was a", value)

# 47. Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total.
num_1 = int(input("enter a number: "))
num_2 = int(input("enter another number: "))
total = num_1 + num_2
que = input("do you want to add another number? (y/n) ")
while que == "y":
	print("the total is", total)

# 49. Create a variable called compnum and set the value to 50. Ask the user to enter a number. While their guess is not the same as the compnum value, tell them if their guess is too low or too high and ask them to have another guess. If they enter the same value as compnum, display the message “Well done, you took [count] attempts”. 
compnum = 50
count = 1
user = int(input(" Enter a number : "))
while user != compnum:
	if user < compnum:
		print(" Too low \n Please try again ")		
		
	else:
		print(' Too high \n Please try again ')

	count  = count + 1
	
	user = int(input(' Have another guess :  '))
	print('Well done, you took' , count, ' attempts')

# 50. Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message “Too low” and ask them to try again. If they enter a value above 20, display the message “Too high” and ask them to try again. Keep repeating this until they enter a value that is between 10 and 20 and then display the message “Thank you”. 
num = int(input("enter a number between 10 and 20: "))
while num < 10 or num > 20:
	if num < 10:
		print("too low")
else: 
	print("too high")
	num = int(input("try again: "))
	print("thank you")

# 51. Using the song “10 green bottles”, display the lines “There are [num] green bottles hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle should accidentally fall”. Then ask the question “how many green bottles will be hanging on the wall?” If the user answers correctly, display the message “There will be [num] how many green bottles will be hanging on the wall If they answer incorrectly, display the message “No, try again” until they get it right. When the number of green bottles gets down to 0, display the message how many green bottles will be hanging on the walll”. 

num  = 10

while num >0:
	print(' There are', num , 'green botyles hanging on the wall')
	print(num, 'green bottles hanging omn the wall. ')
	print(' if 1 green bottle should accidentally fall. ')
	num = num - 1
	answer = int(input( ' how many green bottles will be hanging on the wall? '))
	if answer == num:
		print(' There will be' , num , ' green bottles will be hanging on the wall')
	else:
		while answer != num:
			answer = int(input('No try again : '))
print(' How many green bottles will be hanging on the wall ?  ')
