#!/usr/bin/env python3
import re
f = open("input","r")
initial = f.readlines()
values = []
for line in initial:
    tmp = []
    if re.search("twone", line):
        line = re.sub("twone","21",line)
    if re.search(r"eightwo",line):
        line = re.sub("eightwo", "82", line)
    if re.search(r"oneight",line):
        line = re.sub("oneight", "18", line)
    if re.search(r"sevenine",line):
        line = re.sub("sevenine", "79", line)
    if re.search(r"one",line):
        line = re.sub("one","1",line)
    if re.search(r"two",line):
        line = re.sub("two","2",line)
    if re.search(r"three",line):
        line = re.sub("three","3",line)
    if re.search(r"four",line):
        line = re.sub("four","4",line)
    if re.search(r"five",line):
        line = re.sub("five","5",line)
    if re.search(r"six",line):
        line = re.sub("six","6",line)
    if re.search(r"seven",line):
        line = re.sub("seven","7",line)
    if re.search(r"eight",line):
        line = re.sub("eight","8",line)
    if re.search(r"nine",line):
        line = re.sub("nine","9",line)
    for l in line:
        if re.match("\d", l):
            tmp.append(l)
    v = tmp[0] + tmp[-1]
    values.append(int(v))
total_sum = 0
for cv in values:
    total_sum = total_sum + cv
print(total_sum)