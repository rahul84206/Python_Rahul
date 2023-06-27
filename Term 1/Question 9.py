# Count and display the number of vowels, consonants, uppercase, lowercase characters in string

vowels = 0
consonant = 0
uc = 0
lc = 0

str = input("Enter a string : ")
for i in range(0, len(str)):
    ch = str[i]
    if ((ch >= 'a' and ch <= 'z')):
        lc = lc+1
    if ((ch >= 'A' and ch <= 'Z')):
        uc = uc+1
    if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
         ch = ch.lower()
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        vowels += 1
    else:
        consonant += 1

print("Vowels:", vowels)
print("Consonant:", consonant)
print("Uppercase:", uc)
print("Lower case:", lc)
