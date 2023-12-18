
import numpy as np

filetext = []
with open("input.txt") as f:
    filetext = f.readlines()

dupe = []
dupe2 = []
for line in filetext:
    temp = [(1 if i == "#" else 0) for i in line.strip()]
    if sum(temp) == 0:
        dupe.append(temp)
        dupe.append(temp)
        dupe2.append(temp)
    else:
        dupe.append(temp)
        dupe2.append(temp)
    
arr = np.transpose(np.array(dupe))
new_arr = []
for line in arr:
    if np.sum(line) == 0:
        new_arr.append(line)
        new_arr.append(line)
    else:
        new_arr.append(line)
arr = np.transpose(np.array(new_arr))
wheres = np.where(arr == 1)

galaxies = []

for i, j in zip(wheres[0], wheres[1]):
    galaxies.append((i,j))

def manhattan_distance(x1, x2, y1, y2):
    return np.abs(x1 - x2) + np.abs(y1 - y2)


ret = 0
for p in range(len(galaxies)):
    for q in range(p, len(galaxies)):
        galaxy1x, galaxy1y = galaxies[p]
        galaxy2x, galaxy2y = galaxies[q]
        ret += manhattan_distance(galaxy1x, galaxy2x, galaxy1y, galaxy2y)

ret1 = ret

arr = np.array(dupe2)
wheres = np.where(arr == 1)

galaxies = []

for i, j in zip(wheres[0], wheres[1]):
    galaxies.append((i,j))

ret = 0
for p in range(len(galaxies)):
    for q in range(p, len(galaxies)):
        galaxy1x, galaxy1y = galaxies[p]
        galaxy2x, galaxy2y = galaxies[q]
        ret += manhattan_distance(galaxy1x, galaxy2x, galaxy1y, galaxy2y)

print((ret1 - ret) * 999_999 + ret)