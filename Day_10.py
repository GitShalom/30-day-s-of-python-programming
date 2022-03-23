# 80. Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space). 
first_name = input("enter your first name: ")
length = len(first_name)
print (length)
surname = input("enter your surname: ")
length = len(surname)
print (length)
add = first_name + " " + surname
length = len(add)
print("your full name is", add)
print (length)

# 81. Ask the user to type in their favourite school subject. Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.
fav_sub = input("enter your favourite subject: ")
for letter in fav_sub:
	print (letter, end = "-")

# 82. Show the user a line of text from your favourite poem and ask for a starting and ending point. Display the characters between those two points. 
fav_poem = "make hay while the sun shines"
print(fav_poem)
start = int(input("enter a starting num: "))
end = int(input("enter an ending num: "))
print(fav_poem[start:end])

# 84. Ask the user to type in their postcode. Display the first two letters in uppercase. 
p_code = ("enter your postcode: ")
letters = p_code [0 : 2]
print (letters.upper ())

# 85. Ask the user to type in their name and then tell them how many vowels are in their name. 
name = input("enter your name: ")
count = 0
name = name.lower ()
for x in name:
	if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
		count = count + 1
		print("vowels =", count)

# 86. Ask the user to enter a new password. Ask them to enter it again. If the two passwords match, display “Thank you”. If the letters are correct but in the wrong case, display the message “They must be in the same case”, otherwise display the message “Incorrect”. 
n_psw = input("enter a new password: ")
n_psw2 = input("enter another password: ")
if n_psw == n_psw2:
	print("thank you")
elif n_psw.lower () == n_psw2.lower ():
	print("they must be in the same case")
else:
	print("incorrect")

# 87. Ask the user to type in a word and then display it backwards on separate lines. For instance, if they type in “Hello” it should display as shown below:
word = input("enter a word: ")
length = len(word)
num = 1
for x in word:
	position = length - num
	letter = word[position]
	print(letter)
	num = num + 1