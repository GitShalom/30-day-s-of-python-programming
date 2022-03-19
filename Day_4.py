# 27. Ask the user to enter a number with lots of decimal places. Multiply this number by two and display the answer. 
#num = float(input("enter a number with lots of decimal places: "))
#answer = num * 2
#print (answer)

# 28. Update program 027 so that it will display the answer to two decimal places.
#num = float(input("enter a number with lots of decimal places: ")) 
#answer = num * 2
#print (answer)
#print (round(answer, 2))

# 29. Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two decimal places. 
#import math

#num = int(input("enter an integer over 500: "))
#answer = math.sqrt (num)
#print (round(answer, 2))

# 30. Display pi (π) to five decimal places. 
#import math
#print (round(math.pi, 5))

# 31. Ask the user to enter the radius of a circle (measurement from the centre point to the edge). Work out the area of the circle (π*radius2). 
#import math
#radius = int(input("enter the radius of a circle: "))
#area = math.pi*(radius**2)
#print (area)

# 32. Ask for the radius and the depth of a cylinder and work out the total volume (circle area*depth) rounded to three decimal places.
#import math 
#radius = int(input("what is the radius of a cylinder? "))
#depth = int(input("what is the depth of a cylinder? "))
#area = math.pi*(radius**2)
#volume = area * depth
#print (round(volume, 3))

# 33. Ask the user to enter two numbers. Use whole number division to divide the first number by the second and also work out the remainder and display the answer in a user-friendly way (e.g. if they enter 7 and 2 display “7 divided by 2 is 3 with 1 remaining”). 
#num_1 = int(input("enter first number: "))
#num_2 = int(input("enter second number: "))
#answer_1 = num_1 // num_2
#answer_2 = num_1 % num_2
#print (num_1, "divided by", num_2, "is", #answer_1, "with", answer_2, "remaining")

# 34. Display the following message: If the user enters 1, then it should ask them for the length of one of its sides and display the area. If they select 2, it should ask for the base and height of the triangle and display the area. If they type in anything else, it should give them a suitable error message. 

ent = int(input(" Press 1 or 2 : "))

if ent == 1:
	len =int(input("  length of one of its sides :  "))
	area = len* len
	print(area)
elif ent == 2:
	base =int(input("  Enter the base of the triangle :  "))
	height = int(input("  Enter the height of the triangle :  "))
	area_of_triangle = 0.5*base*height
	print(area_of_triangle)
else:
	print(' invalid number ')
