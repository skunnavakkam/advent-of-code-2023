from numpy import diff
def iter(input_list):
    return (0 if not any(input_list) else input_list[-1] + iter(diff(input_list)))
with open("input.txt") as f:
    lines = f.readlines()
    print(sum([iter([int(i) for i in line.split(" ")]) for line in lines]))
    print(sum([iter([int(i) for i in line.split(" ")][::-1]) for line in lines]))
