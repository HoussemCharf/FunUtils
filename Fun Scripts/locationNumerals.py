'''The idea here is to create a class to convert from decimal numbers to location numerals and back.
One method that takes an integer and returns the location numeral in
abbreviated form. That is, you pass in 9 and it returns ad
Second method that takes a location numeral and returns its value as an integer.
That is, you pass ad in, and it returns 9
Third method that takes a location numeral and returns it in abbreviated form.
That is, you pass in abbc and it returns ad'''

import math

class LocationNumerals:

    @classmethod
    def return_integer_location(self, variable):
        location = []
        number = int(variable)

        while number >= 0:
            if number:
                y = int(math.log(number, 2))
                number -= 2**y

                if y > 25:
                    location.append('z')
                else:
                    location.append(chr(ord('a')+y))
            else:
                print (
                    'Your location numeral is: {}'.format(
                        ''.join(sorted(location))
                    )
                )
                return variable

    @classmethod
    def return_location_integer(self, variable):
        loc_array = list(variable)
        numeral_array = []
        numeral = 0

        for l in loc_array:
            numeral_array.append(ord(l)-ord('a'))

        while len(numeral_array) > 0:
            x = numeral_array.pop()
            numeral = numeral + 2**x

        print('Your numeral location is: {}'.format(str(numeral)))
        return loc_array

    @classmethod
    def return_abbreviaton(self, variable):
        count = {}
        abbr_array = []
        abbreviated = False

        for n in list(variable):
            if n in count:
                count[n] += 1
                abbreviated = True
            else:
                count[n] = 1

        for n in count:
            mcn = count.get(n)
            repeated_list = []
            if mcn > 1:
                '''treatment of more the two repeated letters'''
                if mcn >= 2:
                    while mcn >= 0:
                        if mcn % 2 == 0:
                            if mcn == 0:
                                count[n]=0
                                break
                            else:
                                mcn -= 2
                                repeated_list.append(chr(ord(n)+1))
                        else:
                            count[n]=n
                            mcn -= 1
                            repeated_list.append(chr(ord(n)))
                else:
                    abbr_array.append(chr(ord(n)+1))
                '''end of treatment of more the two repeated letters'''
            else:
                count[n] = n

            if mcn != 0:
                abbr_array.append(count.get(n))

            if len(repeated_list):
                abbr_array = abbr_array + repeated_list

        if abbreviated:
            self.return_abbreviaton(abbr_array)
        else:
            print(
                'Your abbreviated location is: {}'.format(
                    ''.join(sorted(abbr_array))
                )
            )

operation = raw_input(
    "Choose your operation: \n"
    "1 - Return Integer's Location\n"
    "2 - Return Location's Integer\n"
    "3 - Return Abbreviated Location\n"
)

if operation:
    while int(operation) > 3:
        operation = raw_input(
            "Choice unrecognized, please choose your operation: \n"
            "1 - Return Integer's Location\n"
            "2 - Return Location's Integer\n"
            "3 - Return Abbreviated Location\n"
        )

    if 3 >= int(operation) > 1:
        variable = raw_input("Type your location: ")

        while not variable:
            variable = raw_input("Type your location: ")
        if int(operation) == 2:
            LocationNumerals.return_location_integer(variable)
        else:
            LocationNumerals.return_abbreviaton(variable)
    elif int(operation) == 1:
        variable = raw_input("Type your integer: ")

        while not variable:
            variable = raw_input("Type your integer: ")
        LocationNumerals.return_integer_location(variable)