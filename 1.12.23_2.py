#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:21:35 2023

@author: kirishanakiritharan
"""

file_path = "/Users/kirishanakiritharan/Desktop/input"

with open(file_path) as input_file:
    lines = input_file.read().split("\n")[:-1]

word_conversion = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def decode_numbers(day):
    if day:
        for i in range(len(lines)):
            for word in word_conversion:
                lines[i] = lines[i].replace(word, word[0] + word_conversion[word] + word[-1])

    total_decoded = 0

    for line in lines:
        extracted_number = ""
        for char in line:
            if char.isdigit():
                extracted_number += char

        total_decoded += int(extracted_number[0] + extracted_number[-1])

    return total_decoded

print("Sum of decoded numbers:", decode_numbers(True))
