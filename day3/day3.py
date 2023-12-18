filetext = ""
with open("input.txt") as f:
    filetext = f.read()

symbol_indices = []

for index, char in enumerate(filetext):
    if char not in "1234567890.\n":
        symbol_indices.append(index)


line_length = len(filetext.split("\n")[0]) + 1


moves = [
    line_length,
    line_length + 1,
    line_length - 1,
    -1 * line_length,
    -1 * line_length + 1,
    -1 * line_length - 1,
    1,
    -1,
]


part2count = 0
part1count = 0
star_dict = {}
buffer = ""
is_number = False
is_adjacent = False
current_symbol = 0
for index, char in enumerate(filetext):
    if not is_number:
        if char.isdigit():
            is_number = True
            buffer += char
            if not is_adjacent:
                for move in moves:
                    if index + move in symbol_indices:
                        is_adjacent = True
                        current_symbol = index + move
    elif is_number:
        if char.isdigit():
            buffer += char
            if not is_adjacent:
                for move in moves:
                    if index + move in symbol_indices:
                        is_adjacent = True
                        current_symbol = index + move
        else:
            number = int(buffer)

            if is_adjacent:
                part1count += number

                if current_symbol in star_dict:
                    part2count += star_dict[current_symbol] * number
                else:
                    star_dict[current_symbol] = number
            buffer = ""
            is_number = False
            is_adjacent = False
            current_symbol = 0

print(part1count, part2count)
