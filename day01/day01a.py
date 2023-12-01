#!/usr/bin/env python3

import re

# read input file
f = open("input","r")
calibrations = f.readlines()

values = []

for line in calibrations:
	tmp = []
	for l in line:
		if re.match("\d",l):
			tmp.append(l)
	v = tmp[0] + tmp[-1]
	values.append(int(v))

total_sum = 0
for cv in values:
    total_sum = total_sum + cv

print(total_sum)