#!/usr/bin/env python3
import sys
from itertools import combinations

# First, ingest the data
# with open(sys.argv[1], "r") as f:
with open('./indata.txt', 'r') as f:
	my_nums = [int(i) for i in f.read().splitlines()]

combos = combinations(my_nums, 2)

for x, y in combos:
	if x+y == 2020:
		print(f"The answer is {x*y}")
		break