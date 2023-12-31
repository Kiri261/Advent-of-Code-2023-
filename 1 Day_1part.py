#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:53:35 2023

@author: kirishanakiritharan
"""

def calculate_calibration(line):
    digits = [char for char in line if char.isdigit()]

    if digits:
        first_digit = int(digits[0])
        last_digit = int(digits[-1])
        calibration_value = int(str(first_digit) + str(last_digit))
        return calibration_value
    else:
        return 0  

def sum_calibration_values_from_file(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            total_sum += calculate_calibration(line)  

    return total_sum

file_path = '/Users/kirishanakiritharan/Desktop/input'  

result = sum_calibration_values_from_file(file_path)
print("The sum of all calibration values is:", result)
