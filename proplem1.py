# Aly El-Deen Yasser Ali   20231109
# Gamal Megahed Sayed      20231039
# Zyad Atef Al-Abiad       20231068

# check decimal validity function
def validate_decimal(binary):
    binary = list(binary)
    for i in range(len(binary)):
        if binary[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
            return False
    return True

# check binary validity function
def validate_binary(binary):
    binary = list(binary)
    for i in range(len(binary)):
        if binary[i] not in ["0","1"]:
            return False
    return True

# check octal validity function
def validate_octal(octal):
    octal = str(octal)
    octal = list(octal)
    for i in range(len(octal)):
        if octal[i] not in ["0","1","2","3","4","5","6","7"]:
            return False
    return True

# check hexadecimal validity function
def validate_hexadecimal(hexadecimal):
    hexadecimal = list(hexadecimal)
    for i in range(len(hexadecimal)):
        if hexadecimal[i] not in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
            return False
    return True

# convert from decimal to binary
def dec_to_bin(num):
    list =[]
    while int(num) > 0:
        list+=str(int(num) % 2)
        num=int(num)//2
    list.reverse()
    return ''.join(list)

# convert from decimal to octal function
def dec_to_oct(num):
    res = 0
    i =0
    while int(num)> 0:
        digit = int(num)%8
        res = res + digit*(10**i)
        num = int(num)//8
        i = i+1
    return res

# convert from decimal to hexadecimal function
def dec_to_hexadecimal(num):
    list= []
    while int(num) > 0:
        remainder = int(num)%16
        if remainder<10:
            list.append(str(remainder))
        else:
            list.append(chr(remainder+55))
        num = int(num)//16
    list.reverse()
    return ''.join(list)

# convert from hexadecimal to decimal function
def hexadecimal_to_decimal(num):
    num = list(num)
    num.reverse()
    res =0
    for i in range(len(num)):
        if num[i] in ["A","B","C","D","E","F"]:
            num[i] = ord(num[i])-55
        else:
            num[i]=int(num[i])
        res += num[i]*(16**i)
    return res

# convert from octal to decimal function
def octal_to_dec(num):
    num = int(num)
    res = 0
    i =0
    while num > 0:
        digit = num%10
        res = res + digit*(8**i)
        num = num//10
        i = i+1
    return res

# convert from binary to decimal function
def bin_to_dec(num):
    res =0
    num=list(num)
    num.reverse()
    for i in range(len(num)):
        res += int(num[i])*(2**i)
    return res

# alternative to do while loop in python
while True:
# menu 1
    print("** numbering system converter **")
    print("A) insert a new number")
    print("B) Exit program")
    order = input("(A/B)")
    if order == "A":
        num = input("please insert a number ")
        while not validate_hexadecimal(str(num)):
            num = input("please enter a valid number number")
# menu 2
        while True:
            print("** Please select the base you want to convert a number from**")
            print("A) Decimal")
            print("B) Binary")
            print("C) octal")
            print("D) hexadecimal")
            base = input("(A/B/C/D)")
            if base in ["A", "B", "C", "D"]:
                break
# ask for valid choice
            else:
                print ("please select a valid choice ")

# menu 3
        while True:
            print("** Please select the base you want to convert a number to **")
            print("A) decimal")
            print("B) binary")
            print("C) octal")
            print("D) hexadecimal")
            base_convert = input("(A/B/C/D)")
            if base_convert in ["A", "B", "C", "D"]:
                break
# ask for valid choice
            else:
                print("please select a valid choice")

# convert from decimal to decimal
        if base == "A" and base_convert == "A":
            while not validate_decimal(str(num)):
                num = input("please enter a valid decimal number")
            print(f"The result:{num}")
# convert from decimal to binary
        elif base == "A" and base_convert == "B":
            while not validate_decimal(str(num)):
                num = input("please enter a valid decimal number")
            print("The result:",dec_to_bin(num))
# convert from decimal to octal
        elif base == "A" and base_convert == "C":
            while not validate_decimal(str(num)):
                num = input("please enter a valid decimal number")
            print("The result:",dec_to_oct(num))
# convert from decimal to hexadecimal
        elif base == "A" and base_convert == "D":
            while not validate_decimal(str(num)):
                num = input("please enter a valid decimal number")
            print("The result:",dec_to_hexadecimal(num))
# convert from binary to decimal
        elif base == "B" and base_convert == "A":
# check validate binary
            while not validate_binary(str(num)):
                num = input("please enter a valid binary number")
            print("The result:",bin_to_dec(num))
# convert from binary to binary
        elif base == "B" and base_convert == "B":
# check validate binary
            while not validate_binary(num):
                num = input("please enter a valid binary number")
            print("The result:",num)
# convert from binary to octal
        elif base == "B" and base_convert == "C":
# check validate binary
            while not validate_binary(num):
                num = input("please enter a valid binary number")
# convert from binary to decimal then to octal
            print("The result:",dec_to_oct(bin_to_dec(num)))
# convert from binary to hexadecimal
        elif base == "B" and base_convert == "D":
# check validate binary
            while not validate_binary(num):
                num = input("please enter a valid binary number")
# convert from binary to decimal then to hexadecimal
            print("The result:",dec_to_hexadecimal(bin_to_dec(num)))
# convert from octal to decimal
        elif base == "C" and base_convert == "A":
# check validate octal
            while not validate_octal(num):
                num = input("please enter a valid octal number")
            print("The result:",octal_to_dec(num))
# convert from octal to binary
        elif base == "C" and base_convert == "B":
# check validate octal
            while not validate_octal(num):
                num = input("please enter a valid octal number")
# convert from octal to decimal then binary
            print("The result:",dec_to_bin(octal_to_dec(num)))
# convert from octal to octal
        elif base == "C" and base_convert == "C":
# check validate octal
            while not validate_octal(num):
                num = input("please enter a valid octal number")
            print("The result:",num)
# convert from octal to hexadecimal
        elif base == "C" and base_convert == "D":
# check validate octal
            while not validate_octal(num):
                num = input("please enter a valid octal number")
# convert from octal to decimal then hexadecimal
            print("The result:",dec_to_hexadecimal(octal_to_dec(num)))
# convert from hexadecimal to decimal
        elif base == "D" and base_convert == "A":
# check validate hexadecimal
            while not validate_hexadecimal(num):
                num = input("please enter a valid hexadecimal number")
            print("The result:",hexadecimal_to_decimal(num))
# convert from hexadecimal to binary
        elif base == "D" and base_convert == "B":
# check validate hexadecimal
            while not validate_hexadecimal(num):
                num = input("please enter a valid hexadecimal number")
# convert from hexadecimal to decimal then binary
            print("The result:",dec_to_bin(hexadecimal_to_decimal(num)))
# convert from hexadecimal to octal
        elif base == "D" and base_convert == "C":
# check validate hexadecimal
            while not validate_hexadecimal(num):
                num = input("please enter a valid hexadecimal number")
# convert from hexadecimal to decimal then octal
            print("The result:",dec_to_oct(hexadecimal_to_decimal(num)))
# convert from hexadecimal to hexadecimal
        elif base == "D" and base_convert == "D":
# check validate hexadecimal
            while not validate_hexadecimal(num):
                num = input("please enter a valid hexadecimal number")
            print("The result:",num)

# closing the program
    elif order == "B":
        break
# ask for valid choice
    else:
        print("please select a valid choice")