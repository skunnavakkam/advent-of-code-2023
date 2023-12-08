import re

total = 0

with open("input.txt") as filetext:
    f = filetext.readlines()
    number_of_scratchcards = [1 for i in f]
    for line_index, line in enumerate(f):
        new_string = line.split(":")[1]
        numbers = re.findall("[0-9]+", new_string)
        winning_numbers = set(
            [int(i) for i in re.findall("[0-9]+", new_string.split("|")[0])]
        )
        my_numbers = set(
            [int(i) for i in re.findall("[0-9]+", new_string.split("|")[1])]
        )
        print(winning_numbers)
        print(my_numbers)
        count = 0
        for number in my_numbers:
            print(number, winning_numbers, number in winning_numbers)
            count += 1 if number in winning_numbers else 0
        for i in range(1, count + 1):
            number_of_scratchcards[i + line_index] += number_of_scratchcards[line_index]

print(sum(number_of_scratchcards))
