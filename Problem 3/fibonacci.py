fib = [0,1] # Starts the fibonacci sequence with 0 and 1
index = 2   # Start the index at 2 since we will be adding to the 3rd spot on list
while len(fib) < 100: # Runs this loop while the list is less than 100 items long.
    fib.append(fib[index-1]+fib[index-2]) # Adds the previous 2 list items to each other and appends them to the next spot on the list.
    index = index + 1 #increments our index
print(fib) #displays our work.
