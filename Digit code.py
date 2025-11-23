# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 19:06:11 2025

@author: Admin
"""

# Program to print the digit at a given position in the series

num = int(input("Enter the number: "))
digit_till = int(input("Enter the digit till you want the series to be printed: "))

# creating the series as one long string
series = ""
for i in range(1, num + 1):
    series += str(i)

# trimming series up to required digits
required_seq = series[:digit_till]

print("The required seq is: ", required_seq)

pos = int(input("Enter the digit position: "))

if 1 <= pos <= len(required_seq):
    print(f"Number at digit {pos} is: {required_seq[pos-1]}")
else:
    print("Invalid position")