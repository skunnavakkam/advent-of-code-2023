
import numpy as np

grid = []

with open("input.txt") as f:
    for line in f:
        row = [character for character in line.strip()]
        grid.append(row)

grid = np.array(grid)
grid = np.rot90(grid, 3)

new_grid = []

for row in grid:
    new_row = [i for i in row]
    for i in range(len(row)):
        curr = len(row) - i - 1
        if row[curr] == "O":
            new_row[curr] = "."
            curr += 1
            while curr < len(row) and new_row[curr] != "O" and new_row[curr] != "#":
                curr += 1
            if not (curr < len(row) and new_row[curr] != "O" and new_row[curr] != "#"):
                curr -= 1
            new_row[curr] = "O"       
    new_grid.append(new_row)

new_grid = np.array(new_grid)
print(new_grid)

values = []
for row in new_grid:
    for character_number, character in enumerate(row):
        if character == "O":
            values.append(character_number + 1)

print(sum(values))
