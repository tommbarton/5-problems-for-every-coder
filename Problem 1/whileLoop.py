# Summing a list with a while loop in python

mylist = [1,2,3,4,5,6]				# Creates a list with the numbers we need.
index = 0							# Declare an index variable to track list position.
total = 0							# Decalre a total starting at 0 that we can add to with each loop pass.
while index < len(mylist):			# While the index is less than the length of the list it will continue to loop.
	total = total + mylist[index]	# Adding the current item in the list with the total.
	index = index + 1				# Incrementing the index with every pass of the loop.
print total							# Display total.