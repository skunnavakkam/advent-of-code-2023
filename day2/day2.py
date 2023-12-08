import re

with open("input.txt") as f:
    count = 0
    for index, line in enumerate(f):
        max_blue = max([int(i) for i in re.findall("([0-9]+) blue", line)])
        max_green = max([int(i) for i in re.findall("([0-9]+) green", line)])
        max_red = max([int(i) for i in re.findall("([0-9]+) red", line)])

        count += max_blue * max_green * max_red

