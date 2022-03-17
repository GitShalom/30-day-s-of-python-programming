#Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a userfriendly format.
started_num = int(input("how many slices of pizza the user started with: "))
end_num = int(input("how many slices have they eaten: "))
slice_left = started_num - end_num
print("they have", slice_left, "slices_remaining")


		
	