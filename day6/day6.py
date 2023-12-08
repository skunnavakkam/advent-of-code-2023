import re

time_list = []
distance_list = []

with open("input.txt") as f:
    f = f.readlines()
    time_list = [int(i) for i in re.findall("[0-9]+", f[0])]
    distance_list = [int(i) for i in re.findall("[0-9]+", f[1])]

count = 1

for time, distance in zip(time_list, distance_list):
    temp_count = 0
    for speed in range(time + 1):
        if (speed * (time - speed)) > distance:
            temp_count += 1
    count *= temp_count

print(count)
