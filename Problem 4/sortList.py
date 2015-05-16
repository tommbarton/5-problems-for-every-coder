## Write a function that given a list of
## non negative integers, arranges them
## such that they form the largest possible
## number. For example, given [50, 2, 1, 9],
## the largest formed number is 95021.

listX=[50,2,1,9]

sortedListX = sorted(map(str, listX), cmp=lambda x1,x2: cmp(x1+x2, x2+x1), reverse=True)

print int(''.join(sortedListX))
