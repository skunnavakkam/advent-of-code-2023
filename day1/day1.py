import re

words_to_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

"""
use for pt 1 of the task
words_to_numbers = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}
"""

digits = "0123456789"

regex = "(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))"

total = 0
with open("input.txt") as f:
    for line in f:
        found_list = re.findall(regex, line)
        total += words_to_numbers[found_list[0]] * 10 + words_to_numbers[found_list[-1]]
print(total)
