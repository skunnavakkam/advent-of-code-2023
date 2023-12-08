import re
from time import perf_counter_ns
from math import isqrt, sqrt


time = 0
distance = 0

with open("input.txt") as f:
    f = f.readlines()
    time = int("".join(re.findall("[0-9]+", f[0])))
    distance = int("".join(re.findall("[0-9]+", f[1])))

time1 = perf_counter_ns()
for i in range(10000):
    int(isqrt(time * time - (distance << 2))) | 1
print((perf_counter_ns() - time1) / 10000)
