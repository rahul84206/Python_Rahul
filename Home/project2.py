
#Number system convertor

inp1 = input("Enter the number: ")
org = int(input("Enter it base: "))
to = int(input("Enter the base in which it is to converted: "))
print("\n")
################################################################
if org == 2 or org == 8 or org == 10:
    inp = int(inp1)
if org == 16:
    inp = int(inp1, 16)
    h = inp
################################################################
if (to == 2 or to == 8 or to == 10 or to == 16) and org != 16:
    out1 = 0
    power = 0
    while inp > 0:
        out1 += org**power*(inp % 10)
        inp //= 10
        power += 1
    print("After conversion the result in decimal is: ", out1)

else:
    out1 = h
    print("After conversion the result in decimal is: ", out1)
#######################################################################
if to == 2:
    out2 = 0
    power = 0
    while out1 > 0:
        out2 += 10**power*(out1 % 2)
        out1 //= 2
        power += 1
    print("After conversion into binary the result is: ", out2)
#######################################################################
if to == 16:
    change_table = ['0', '1', '2', '3', '4', '5', '6',
                    '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    dec = out1
    hexa = ""
    while(dec>0):
        r = dec % 16
        hexa = change_table[r]+hexa
        dec = dec//16
    print("Hexadecimal:", hexa)
