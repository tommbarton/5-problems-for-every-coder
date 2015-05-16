# Summing a list with recursion

def sumList(myList): # Creates a function with our passed data stored in the myList variable
   if len(myList) == 1: # When there is only one item left in the list it will return the data and end the recursive function
        return myList[0]
   else:
        return myList[0] + sumList(myList[1:])  #  This will take the first list item and add it to a recursive function call that passes the slice list at the second item to the last.

print(sumList([1,2,3,4,5,6])) # This displays our data and initiates our recursive function.
