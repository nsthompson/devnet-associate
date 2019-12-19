#!/usr/bin/env python

'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

# Prompt the user for a word to test, store the collected value as the variable word
word = input("Enter a word: ")

'''
Check if the user provided word is the same as the reverse of the user provided word.
Strings are just lists of characters.  Using slicing, you can reverse a list leveraging [::-1].
'''
if (word.lower() == word[::-1].lower()):
    print(f"{word} is a palindrome\n")    
else:
    print(f"{word} is not a palindrome\n")