
line:str = ""

with open("input.txt") as f:
    line = f.read().strip()

sequences = line.split(",")

def get_hash(text:str) -> int:
    ret = 0

    for character in text:
        ret += ord(character)
        ret *= 17
        ret %= 256
    
    return ret

print(f"Part 1: {sum([get_hash(sequence) for sequence in sequences])}")

boxes = [list() for _ in range(255)]
values = [list() for _ in range(255)]

def box_printer():
    for box_number, box in enumerate(boxes):
        if len(box) != 0:
            print(f"{box_number}: {box}, {values[box_number]}")

for sequence in sequences:

    if "-" in sequence:
        #print(sequence)
        string = sequence.strip("-")
        hash = get_hash(string)
        if string in boxes[hash]:
            index = boxes[hash].index(string)
            boxes[hash].pop(index)
            values[hash].pop(index)
    else: 
        splitted = sequence.split("=")
        string = splitted[0]
        value = int(splitted[1])
        hash = get_hash(string)
        #print(sequence)
        if string in boxes[hash]:
            index = boxes[hash].index(string)
            values[hash][index] = value
        else:
            boxes[hash].append(string)
            values[hash].append(value)

sums = []
for box_number, box in enumerate(values):
    for lens_number, lens in enumerate(box):
        sums.append((box_number + 1) * (lens_number + 1) * lens)

print(f"Part 2: {sum(sums)}")