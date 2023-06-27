
# Number System Converter (Btween Binary, Octal & Decimal)

while 1 > 0:
    inp = int(input("Enter the number : "))
    org = int(input("Enter it's base : "))
    to = int(input("Enter the base in which it is to be converted : "))
    print("\n")
#######################################################################
    if to == 2 or to == 8 or to == 16 or to == 10:
        out1 = 0
        power = 0
        while inp > 0:
            out1 += org**power*(inp % 10)
            inp //= 10
            power += 1
        print("After conversion the result in decimal is : ", out1)
#######################################################################
    if to == 8:
        out2 = 0
        power = 0
        while out1 > 0:
            out2 += 10**power*(out1 % 8)
            out1 //= 8
            power += 1
        print("After conversion into octal the result is : ", out2)
#######################################################################
    elif to == 2:
        out4 = 0
        power = 0
        while out1 > 0:
            out4 += 10**power*(out1 % 2)
            out1 //= 2
            power += 1
        print("After conversion into binary the result is: ", out4)
#######################################################################
    change_table = ['0', '1', '2', '3', '4', '5', '6',
                    '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    dec = out1
    hexa = ''

    while(dec > 0):
        r = dec % 16
        hexa = change_table[r] + hexa
        dec = dec//16
print("Hexadecimal: ", hexa)
