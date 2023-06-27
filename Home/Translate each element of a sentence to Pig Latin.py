s = input('Enter a string : ')
s = s+' '
slen = len(s)
pos = 0
word = ''
str1 = ''
for i in range(0, slen):
    if s[i] == ' ':
        word = s[pos:i]
        pos = i+1
        lword = len(word)
        first = ''
        last = ''
        final = ''
        for i in range(lword+1):
            if word[i] in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
                break
        first = word[0:i]
        last = word[i:]
        final = last+first+'ay'
        str1 = str1+final+' '
print("Sentence in Pig Latin is : ", str1)
