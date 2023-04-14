#Python program to create a pyramid pattern

n=20
for i in range(1, 11):
    print(' '*n, end='') # repeat space for n times
    print('* '*(i)) # repeat stars for i times
    n-=1