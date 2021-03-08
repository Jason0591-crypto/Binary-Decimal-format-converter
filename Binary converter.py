# This function converts numbers in decimal format to binary format
def dec_convert_bin(base_num):
    # Create a list to hold all the binary digits
    list1 = []
    # Create a variable that will calculate the number left
    num = base_num
    # While the number have not yet been all converted into binary, this loop will keep on running and converting the number to binary
    while num > 0:
        # The remainder of the number after it has been divided by 2
        rem = num % 2
        # Adding the remainder to the list of binary numbers
        list1.append(rem)
        # The number being reduced without its  after being converted
        num = num // 2
    # Reversing the list
    list1.reverse()
    # Returning the converted binary number
    return list1


print(dec_convert_bin(64))


# This function converts numbers in binary format into decimal format
def bin_convert_dec():
    # This line of code allows the binary number the user entered to be converted into a list and becomes easier to convert to decimal
    base_num = list(input("Please enter the number you want to convert"))
    # This line reverses the base number, which allows the program to read it normally, transforming it
    # into its actual format, since the number, after being converted into a list, was actually reversed due
    # to the nature of lists(the correct order is actually for the numbers to be reversed)
    base_num.reverse()
    # Setting the length of the list, which is also the amount of time the loop will run
    length = len(base_num) - 1
    # The final number that will be returned
    final_dec = 0
    # added_num = 0
    # While the count have not ran out, the loop will continuously read the next digit in the number
    while length >= 0:
        # This line will add the current digit to the final output in decimal
        added_num = (2**length) * int(base_num[length])
        # Adding the actual size of the digit in decimal to the final output
        final_dec += added_num
        # The number goes down to the next digit
        length -= 1
    # Return the final output
    return final_dec


print(bin_convert_dec())
