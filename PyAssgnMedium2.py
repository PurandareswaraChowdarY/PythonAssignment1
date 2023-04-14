#Python program to check if a string is palindrome or not

s1=input("Enter s1")
print(s1)
s2=s1[-1::-1]
print(s2)
if s1==s2:
    print("Palindrome")
else:
    print("Not a palindrome")