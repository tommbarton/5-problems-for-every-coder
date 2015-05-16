# The easiest way to perform this task is to
# do the following although this will circumvent
# the exercise of utilizing a list and for loop
# 
#		mylist = range(7)   # Creates a range of 0-6 in the mylist variable.
#		print sum(mylist)   # Displays the sum of the list.

mylist = [1,2,3,4,5,6]				# Creates a list with the numbers we need.
index = 0							# Declare an index variable to track list position.
total = 0							# Decalre a total starting at 0 that we can add to with each loop pass.
for item in mylist:					# The loop will run as many times as the list is long.
	total = total + mylist[index]	# Increments the total by the current list item the loop is running.
	index = index+1					# Increment the index so it will reference the next item in the next pass.
	
print total							#	Displays our data.