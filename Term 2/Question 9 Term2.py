# Write a program that repeatedly asks the user to enter product names and prices. Store the product names as keys and prices as values. When a user is done entering the products and prices, allow them to repeatedly enter a product name and print the corresponding price or message if the product is not in the dictionary.

Pdict={}
Y=0
Total=int(input("Total no. of products : "))
while Y<Total:
    Pnames=input("Enter the product name : ")
    Prices=input("Enter it's price : ")
    Pdict[Pnames]=Prices
    Y+=1
while True:
    Pnames=input("Enter the product name whose price you want to check : ")
    if Pnames in Pdict:
        print("The price of",Pnames,"is",Pdict[Pnames])
    else:
        print("Not found")
    cond=input("Do you want to continue (y or n)? ")
    if cond=="y":
        continue
    else:
        break
    
