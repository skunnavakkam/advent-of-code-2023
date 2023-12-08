from math import lcm

instruction = ""
instruction_length = 0

moves = {}

with open("input.txt") as f:
    lines = f.readlines()
    instruction = lines[0].strip()
    instruction_length = len(instruction)

    for line in lines[2:]:
        splitted = line.split("=")
        node = splitted[0].strip()
        splitted = splitted[1].replace("(", "").replace(")", "").split(",")
        left = splitted[0].strip()
        right = splitted[1].strip()
        tup = (left, right)
        moves[node] = tup


def steps(starting_node, instruction, moves):
    count = 0
    curr_node = starting_node
    current_instruction_index = 0
    while True:
        curr_instruction = instruction[current_instruction_index]
        count += 1
        if curr_instruction == "R":
            curr_node = moves[curr_node][1]
        elif curr_instruction == "L":
            curr_node = moves[curr_node][0]

        if curr_node[-1] == "Z":
            return count

        if current_instruction_index == len(instruction) - 1:
            current_instruction_index = 0
        else:
            current_instruction_index += 1


steps_list = []
for key in moves:
    if key[-1] == "A":
        steps_list.append(steps(key, instruction, moves))

print(f"Part One: {steps('AAA', instruction, moves)}")
print(f"Part Two: {lcm(*steps_list)}")
