# Aly El-Deen Yasser Ali   20231109
# Gamal Megahed Sayed      20231039
# Zyad Atef Al-Abiad       20231068

# defining some function

# validity function
def validate_binary(binary):
    check_correct = False
    while not check_correct:
        counter = 0
        check = len(binary)
        while counter < check:
            if binary[counter] not in ['1', '0']:
                binary = input("Please enter a valid binary number: ")
                break
            else:
                counter += 1
        if counter == check:
            return binary
            check_correct = True


# check length
def length_check(binary_one, binary_two):
    if len(binary_one) > len(binary_two):
        binary_two = '0' * (len(binary_one) - len(binary_two)) + binary_two
    elif (len(binary_one) < len(binary_two)):
        binary_one = '0' * (len(binary_two) - len(binary_one)) + binary_one
    return binary_one, binary_two


# two s complement
def two_s_complement(binary):
    check = len(binary)
    counter_two = check - 1
    two_s_comple = list(binary)
    while (counter_two >= 0):
        if (two_s_comple[counter_two] == '1'):
            counter_two -= 1
            break
        else:
            counter_two -= 1
    while (counter_two >= 0):
        if (two_s_comple[counter_two] == '0'):
            two_s_comple[counter_two] = '1'
        else:
            two_s_comple[counter_two] = '0'
        counter_two -= 1
    counter = 0
    result = ''
    while (counter < check):
        result = result + two_s_comple[counter]
        counter += 1
    return result


# start program-first menu
print("**binary calculator**")

# body of program
while (True):
    print("A) insert a number")
    print("B) Exit ")
    option = input()

    # to close program
    if (option == 'B'):
        break

    # if user enter anything exept A or B
    while option not in ["A", "B"]:
        print("Please enter a valid option")
        print("A) insert a number")
        print("B) Exit ")
        option = input()

    binary_one = input("Enter the binary number: ")
    # check that number is binary
    binary_one = validate_binary(binary_one)

    # secand menu
    print("**please select the operation**")
    print("A) compute one's complement")
    print("B) compute two's complement")
    print("C) addition")
    print("D) subtraction")
    choice = input()

    # if inputof secand menu is wrong
    while choice not in ["A", "B", "C", "D"]:
        print("Please enter a valid option")
        print("A) compute one's complement")
        print("B) compute two's complement")
        print("C) addition")
        print("D) subtraction")
        choice = input()

    # if choice is A(ones complement)
    if (choice == 'A'):
        counter_one = 0
        one_s_comple = list(binary_one)
        check = len(binary_one)
        while (check > counter_one):
            if (one_s_comple[counter_one] == '0'):
                one_s_comple[counter_one] = '1'
            else:
                one_s_comple[counter_one] = '0'
            counter_one += 1
        print("the one s complement=", end='')
        counter = 0
        while (counter < check):
            print(one_s_comple[counter], end='')
            counter += 1
        print('')

    # if choice is B (twos complement)
    elif (choice == 'B'):
        result = two_s_complement(binary_one)
        print('the two s complement :-', result)
    # if choice is c
    elif (choice == 'C'):
        binary_two = input("please enter the second binary:-")
        # validity
        binary_two = validate_binary(binary_two)
        # length check
        binary_one, binary_two = length_check(binary_one, binary_two)

        # summation
        counter = -1
        binary_sum = ''
        carry = '0'
        while counter >= -len(binary_one):
            bit_sum = int(binary_one[counter]) + int(binary_two[counter]) + int(carry)
            if bit_sum == 0:
                carry = '0'
                binary_sum = '0' + binary_sum
            elif bit_sum == 1:
                carry = '0'
                binary_sum = '1' + binary_sum
            elif bit_sum == 2:
                binary_sum = '0' + binary_sum
                carry = '1'
            else:
                binary_sum = '1' + binary_sum
                carry = '1'
            counter -= 1
        if carry == '1':
            binary_sum = '1' + binary_sum

        print('the summation of two binary num= ', binary_sum)

    # if choice is D
    else:
        binary_two = input("please enter the second binary:- ")
        # validity
        binary_two = validate_binary(binary_two)
        # length check
        binary_one, binary_two = length_check(binary_one, binary_two)
        # convert binary two to twos complement
        binary_two = two_s_complement(binary_two)

        # differance##here we changed second number to two s complement and add them
        counter = -1
        binary_diff = ''
        carry = '0'
        while counter >= -len(binary_one):
            bit_sum = int(binary_one[counter]) + int(binary_two[counter]) + int(carry)
            if bit_sum == 0:
                binary_diff = '0' + binary_diff
                carry = '0'
            elif bit_sum == 1:
                binary_diff = '1' + binary_diff
                carry = '0'
            elif bit_sum == 2:
                binary_diff = '0' + binary_diff
                carry = '1'
            else:
                binary_diff = '1' + binary_diff
                carry = '1'
            counter -= 1

        print('the differance between the two binary num=', binary_diff)
