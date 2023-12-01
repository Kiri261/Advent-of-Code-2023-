#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:16:59 2023

@author: kirishanakiritharan
"""


def letters_to_numbers(line):
    letter_to_num = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'
    }

    for word, num in letter_to_num.items():
        line = line.replace(word, num)

    digits = ''.join(filter(str.isdigit, line))

    first_number = digits[0] if digits else ''
    last_number = digits[-1] if len(digits) > 1 else ''

    return first_number + last_number

file_path = '/Users/kirishanakiritharan/Desktop/input'

total_sum = 0

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            result = letters_to_numbers(line.strip())  
            print(f"{line.strip()} -> {result}")
            if result.isdigit(): 
                total_sum += int(result)

    print(f"Total Sum: {total_sum}")

except FileNotFoundError:
    print("File not found. Please provide the correct file path.")
