# Palindrome String or not
# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]

s = input("Enter a string:")
ans = isPalindrome(s)
print(ans)
if ans:
    print("Yes")
else:
    print("No")
