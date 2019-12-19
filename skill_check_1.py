#!/usr/bin/env python

'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
If you are unfamiliar with divisors, they are numbers that divide evenly into another number.
For example, 10 is a divisor of 100 because 100 / 10 has no remainder.
'''

# Prompt the user for a natural number- cast the collected data as an int and store it in the variable usernum
usernum = int(input("Enter a natural number: "))

# Create an empty list 'divisors'
divisors = []

'''
Loop through a the range of numbers from 1 to usernum+1 
By default, range() starts at 0, we need to start at 1, and the upper limit is -to- the second argument.
To include the user provided number, we need to add 1 to the number
'''
for i in range(1,usernum+1):
    '''
    Using the Modulus operator (%) we can return the remainder of dividing the left hand operand by the right hand operand.
    for example, 10 % 2 = 5, so the remainder is 0, which means we have found a divisior.
    If we use 10 % 3, the remainder is 1, because 3 goes into 10 3 times (9) and the remainder is 1.
    When we find a divisor in the list, we append it to the previously created list 'divisors', increase i by 1, and run the operation again
    '''
    if(usernum%i==0):
        divisors.append(i)
    i = i+1

# Lastly, print the list of divisors of the user inputted number 
print(divisors)


