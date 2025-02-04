"""
Created on Sat Feb  1 19:48:06 2025

@author: somai
Replacing Vowels in a String
Explanation:
We can replace characters in a string using loops and conditional statements. This example replaces all vowels in a string with *.

Instructions:
1. Ask the user to enter a sentence.
2. Replace all vowels (a, e, i, o, u) with *.
3. Print the modified sentence.

"""
vowels = "aeiou"
word = input("Enter the word:")
temp = ""
for char in word:
    if char in vowels:
        temp += "*"
    else:
        temp += char
print(temp)
