# Input a string and determine whether it is a palindrome or not

s = input("Enter a string : ")
s1 = s[::-1]

if s == s1:
	print("It's a Palindrome!")
else:
	print("It's not a Palindrome!")
