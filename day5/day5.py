import re

with open("input.txt") as f:
    f = f.readlines()
    seeds = [int(i) for i in re.findall("[0-9]+", f[0])]
    