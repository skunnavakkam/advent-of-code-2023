
filetext = ""

with open("input.txt") as f:
    filetext = f.read()

line_length = len(filetext.split("\n")[0]) + 1
s_index = filetext.index("S")
moves_taken1 = [-1 for _ in filetext]
moves_taken2 = [-1 for _ in filetext]
visited_squares1 = [s_index]
visited_squares2 = [s_index]

vert_array = []
for letter in filetext:
    if letter in "S|FLJ7":
        vert_array.append(1)
    else:
        vert_array.append(0)
vert_array.append(0)

# we can define each of the pieces by where the start and end points are
# | - index + line_length, index - line_length
# F - index + 1, index + line_length
# - - index + 1, index - 1
# L - index + 1, index - line_length
# J - index - 1, index - line_length
# 7 - index - 1, index + line_length

pipes = {
    "|": (line_length, -1 * line_length),
    "F": (1, line_length),
    "-": (1, -1),
    "L": (1, -1 * line_length),
    "J": (-1, -1 * line_length),
    "7": (-1, line_length)
}

moves = [
    1, -1,
    line_length, line_length + 1, line_length - 1,
    -1 * line_length, -1 * line_length + 1, -1 * line_length - 1
]

index1 = 0
index2 = 0
for move in moves:
    new_index = s_index + move
    char_at = filetext[new_index]
    if char_at == ".":
        continue
    pipe_start_diff, pipe_end_diff = pipes[char_at]
    pipe_start, pipe_end = new_index + pipe_start_diff, new_index + pipe_end_diff
    if pipe_start == s_index or pipe_end == s_index:
        if index1 == 0:
            index1 = new_index
        else:
            index2 = new_index

# loop for index 1
count = 1
moves_taken1[index1] = count
while True:
    char_at = filetext[index1]
    visited_squares1.append(index1)
    pipe_start_diff, pipe_end_diff = pipes[char_at]
    pipe_start, pipe_end = index1 + pipe_start_diff, index1 + pipe_end_diff
    new_index = 0
    if pipe_end not in visited_squares1:
        new_index = pipe_end
    elif pipe_start not in visited_squares1:
        new_index = pipe_start
    else: 
        break
    moves_taken1[index1] = count
    count += 1
    index1 = new_index
moves_taken1[index1] = count


# loop for index 2 (literally the same code)
count = 1
moves_taken2[index2] = count
while True:
    char_at = filetext[index2]
    visited_squares2.append(index2)
    pipe_start_diff, pipe_end_diff = pipes[char_at]
    pipe_start, pipe_end = index2 + pipe_start_diff, index2 + pipe_end_diff
    new_index = 0
    if pipe_end not in visited_squares2:
        new_index = pipe_end
    elif pipe_start not in visited_squares2:
        new_index = pipe_start
    else: 
        break
    moves_taken2[index2] = count
    count += 1
    index2 = new_index
moves_taken2[index2] = count



final_array = []
for visited1, visited2 in zip(moves_taken1, moves_taken2):
    final_array.append(min((visited1, visited2)))
final_array.append(-1)
final_array += [-1 for _ in range(line_length)]
final_array[s_index] = 0

import numpy as np
final_array = np.array(final_array)
final_array = final_array.reshape((-1, line_length))

vert_array = np.array(vert_array)
vert_array = vert_array.reshape((-1, line_length))

num_rows = len(final_array)
area = 0
counter = 0
for row, (path_row, vert_row) in enumerate(zip(final_array, vert_array)):
    is_inside = False
    counter = 0
    for column, (number, vert) in enumerate(zip(path_row, vert_row)):
        if number == -1: # not a pipe
            if counter % 2 == 1:
                area += 1
                final_array[row][column] = -2
        else:
            if final_array[row + 1][column] == number + 1:
                counter += 1
            if final_array[row + 1][column] == number - 1:
                counter -= 1
            
print(area)
np.savetxt('output.txt', final_array, fmt='%6d')