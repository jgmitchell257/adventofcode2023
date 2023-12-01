#!/usr/bin/env python3

import re

# read input file
f = open("input","r")
calibrations = f.readlines()

calibration_values = []


def get_v0(v):
    if re.match(r"\d",v):
        return v
    else:
        if v == "one":
            return "1"
        if v == "eightwo":
            return "8"
        if v == "two":
            return "2"
        if v == "eighthree":
            return "8"
        if v == "three":
            return "3"
        if v == "threeight":
            return "3"
        if v == "four":
            return "4"
        if v == "five":
            return "5"
        if v == "fiveight":
            return "5"
        if v == "six":
            return "6"
        if v == "seven":
            return "7"
        if v == "eight":
            return "8"
        if v == "nine":
            return "9"
        if v == "zero":
            return "0"
        if v =="nineight":
            return "9"
        if v == "oneight":
            return "1"

def get_v1(v):
    if re.match(r"\d",v):
        return v
    else:
        if v == "one":
            return "1"
        if v == "eightwo":
            return "3"
        if v == "two":
            return "2"
        if v == "eighthree":
            return "3"
        if v == "three":
            return "3"
        if v == "threeight":
            return "8"
        if v == "four":
            return "4"
        if v == "five":
            return "5"
        if v == "fiveight":
            return "8"
        if v == "six":
            return "6"
        if v == "seven":
            return "7"
        if v == "eight":
            return "8"
        if v == "nine":
            return "9"
        if v == "zero":
            return "0"
        if v =="nineight":
            return "8"
        if v == "oneight":
            return "8"

for line in calibrations:
    tmp = re.findall(r"\d|oneight|one|eightwo|two|eighthree|threeight|three|four|five|fiveight|six|seven|nineight|eight|nine|zero",line)
    print(tmp)
    v0 = tmp[0]
    v0 = get_v0(v0)
    
    v1 = tmp[-1]
    v1 = get_v1(v1)
    v01 = str(v0) + str(v1)
    calibration_values.append(int(v01))

total_sum = 0

for cv in calibration_values:
    total_sum = total_sum + cv

print(total_sum)