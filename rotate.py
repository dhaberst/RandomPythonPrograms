'''
A curious problem that involves 'rotating' a number and solving a number of contraints

Author: Daniel Haberstock
Date: 05/26/2018

Sources used:
https://stackoverflow.com/questions/19463556/string-contains-any-character-in-group

'''

def rotate(x):
    # split up the integer into a list of single digit strings
    splitx = [i for i in str(x)]

    # reverse it since we are always doing 1/2 rotations
    splitx.reverse()
    
    # initialize the final solution string
    y = ''

    # loop through the list of digits
    # we only need to rotate 6/9 since they are the only number that will flip
    for digit in splitx:
        if digit == "6":
            y += "9"
        elif digit == "9":
            y +="6"
        else:
            y += digit

    return int(y)

# now to solve the riddle
# we need to define our rotate assumption which is to say that if the 
#  number contains a letter 2,3,4,5,7 it is not allowed to be part of the solution
# 1. 100 <= x <= 999 --> for x in range(100, 1000)
# 2. rotate(x) + 129 = x --> if rotate(x) + 129 == x
# 3. rotate(x - 9) = x - 9 --> rotate(x - 9) == x - 9
# we know if both 2. and 3. are true then we found a solution
rotateAssumption = True

for x in range(100, 1000):
    if rotateAssumption:
        if any(num in str(x) for num in "23457"):
            continue

    if rotate(x) + 129 == x and rotate(x - 9) == x - 9:
        print("I found the number: ", x)
