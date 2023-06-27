from _typeshed import HasFileno


word=input('Enter a word : ')
ln=len(word)
first=''
last=''
final=''
for i in range(ln+1):
    if word[i] in ['a,''A','e','E','i','I','o','O','u','U']:
        break
first=word[0:i]
last=word[i:]
final=last+first+'ay'
print("Text in Pig Latin is : ",final)
