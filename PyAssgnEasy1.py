#Python program that determines whether a given number is even or odd.

x=int(input("Enter x"))
if x>0:
    print("x is a positive number")
elif x<0:
    print("x is a negative number")
else:
    print("x is neither positive nor negative")
if x==0:
    print("x is neither even nor odd")
elif x%2==0:
    print("x is an even number")
else:
    print("x is an odd number")
