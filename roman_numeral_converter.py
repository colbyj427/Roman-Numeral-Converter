"""
Program which will take in a number in the form of Roman Numerals and
output the number in decimal form, or take in a decimal form number,
and output the Roman Numeral version.
"""


def rom_num_checker(numerals):
    """
    Function which checks the order of the numerals, to ensure a numeral 
    is not entered which is invalid. Example: XXC
    Will also return False if a letter is input which is not a roman numeral.
    """
    counter = 0
    for numeral in numerals: #iterate through each individual numeral to ensure
        counter += 1         #it is not followed by a numeral of greater value.
        if numeral == 'M':
            return True
        if numeral == 'D':
            for n in numerals[counter-1:]:
                if n == 'M':
                    return False
                else:
                    return True
        elif numeral == 'C':
            try:        #try statement stops the check from stepping past the edge of the string.
                for n in numerals[counter+1]:
                    if n == 'M' or n == 'D':
                        return False
                    else:
                        return True
            except:
                return True
        elif numeral == 'L':
            for n in numerals[counter-1:]:
                if n == 'M' or n == 'D' or n == 'C':
                    return False
                else: 
                    return True
        elif numeral == 'X':
            try:
                for n in numerals[counter+1:]:
                    if n == 'M' or n == 'D' or n == 'C' or n == 'L':
                        return False
                    else:
                        return True
            except:
                return True
        elif numeral == 'V':
            for n in numerals[counter-1:]:
                if n == 'M' or n == 'D' or n == 'C' or n == 'L' or n == 'X':
                    return False
                else:
                    return True
        elif numeral == 'I':
            try:
                for n in numerals[counter+1:]:
                    if n == 'M' or n == 'D' or n == 'C' or n == 'L' or n == 'X' or n == 'V':
                        return False
                    else:
                        return True
            except:
                return True
        else:
            return False

def rom_num_converter(numerals):
    """
    Function which takes in a roman numeral,
    and returns the numeral as a decimal number.
    """

    next_num = numerals[0]
    total = 0
    counter = 0

    if rom_num_checker(numerals) == False:  #Check that the numeral is valid.
        return 'Not a valid Roman Numeral.'
    
    #loop through the numeral to total the values, checking for subtractive notation
    for num in numerals:
        counter += 1    #increment counter to make next_num simpler
        if counter < len(numerals):
            next_num = numerals[counter]    #change the next numeral being dealt with in case reference is needed
        if num == 'M':
            total += 1000   #add M to the total
        elif num == 'D':
            total += 500
        elif num == 'C':
            if next_num == 'M' or next_num == 'D':   #if it is subtractive notation, compute accordingly
                total -= 100
            else:
                total += 100
        elif num == 'L':
            total += 50
        elif num == 'X':
            if next_num == 'C' or next_num == 'L':
                total -= 10
            else:
                total += 10
        elif num == 'V':
            total += 5
        else:
            if next_num == 'X' or next_num == 'V':
                total -= 1
            else:
                total += 1
    return total
    #return the decimal value

#Define a function to convert decimal numbers into Roman Numerals
def decimal_converter(decimal):
    """
    Function which converts a decimal number into roman numerals by separating the place values
    then calling a function on each place value to return the numerals.
    """
    converted = ''
    decimal_copy = decimal
    #Functions to convert thousands, hundreds, tens, and ones places in decimal to numerals.
    def convert_thousands(num):
        amount_ms = num / 1000
        return 'M' * int(amount_ms)
    def convert_hundreds(num):
        if num == 900:
            return 'CM'
        elif num > 500:
            amount_cs = (num - 500) / 100
            return 'D' + (('C') * int(amount_cs))
        elif num == 500:
            return 'D'
        elif num == 400:
            return 'CD'
        else:
            amount_cs = num / 100
            return 'C' * int(amount_cs)
    def convert_tens(num):
        if num == 90:
            return 'XC'
        elif num > 50:
            amount_xs = (num - 50) / 10
            return 'L' + ('X' * int(amount_xs))
        elif num == 50:
            return 'L'
        elif num == 40:
            return 'XL'
        else:
            amount_xs = num / 10
            return 'X' * int(amount_xs)
    def convert_ones(num):
        if num == 9:
            return 'IX'
        elif num > 5:
            amount_is = num - 5
            return 'V' + ('I' * int(amount_is))
        elif num == 5:
            return 'V'
        elif num == 4:
            return 'IV'
        else:
            return 'I' * num
        
    # Logic to determine which functions need to be called.
    if decimal > 3999: #A roman numeral cannot exceed this value
        return 'Number is too high. Cannot be converted.'
    elif decimal >= 1000:
        ones = decimal_copy % 10
        decimal_copy = decimal_copy//10
        tens = (decimal_copy % 10) * 10
        decimal_copy = decimal_copy//10
        hundreds = (decimal_copy % 10) * 100
        decimal_copy = decimal_copy//10
        thousands = (decimal_copy % 10) * 1000

        converted += convert_thousands(thousands)
        converted += convert_hundreds(hundreds)
        converted += convert_tens(tens)
        converted += convert_ones(ones)

    elif decimal >= 100:
       ones = decimal_copy % 10
       decimal_copy = decimal_copy//10
       tens =  (decimal_copy % 10) *10
       decimal_copy = decimal_copy//10
       hundreds = (decimal_copy % 10) *100

       converted += convert_hundreds(hundreds)
       converted += convert_tens(tens)
       converted += convert_ones(ones)
       
    elif decimal >= 10:
       ones = decimal_copy % 10
       decimal_copy = decimal_copy//10
       tens =  (decimal_copy % 10) *10

       converted += convert_tens(tens)
       converted += convert_ones(ones)

    elif decimal >= 1:
        ones = decimal_copy % 10

        converted += convert_ones(ones)
    
    else:
        return 'Not a valid number.'
    return converted


#Allow it to accept input

user_input = None

while True:
    print('\nType Exit to quit.')
    user_input = input('Input roman numeral or number here: ')
    if user_input == 'Exit':
        break
    if user_input == '':
        print("Invalid input")
    try:
        int(user_input)
    except:
        decimal_num = rom_num_converter(user_input)
        print(f'\n{user_input} \n{decimal_num}\n')
    else:
        rom_num = decimal_converter(int(user_input))
        print(f'\n{user_input} \n{rom_num}\n')
