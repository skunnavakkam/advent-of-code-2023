with open("input.txt", "r") as file:
    instructions, directions = file.read().split("\n\n")

instructions = list(instructions)
directions_dict = {}

directions = directions.splitlines()
for item in directions:
    current_location, next_locations = item.split(" = ")
    next_locations = tuple(next_locations.strip("()").split(", "))
    directions_dict[current_location] = next_locations

count = 0
current_instruction_index = 0
current_location = "AAA"
while current_location != "ZZZ":
    count += 1
    current_instruction = instructions[current_instruction_index]
    if current_instruction == "L":
        current_location = directions_dict[current_location][0]
    else:
        current_location = directions_dict[current_location][1]

    if current_instruction_index == len(instructions) - 1:
        current_instruction_index = 0
    else:
        current_instruction_index += 1

print(count)
