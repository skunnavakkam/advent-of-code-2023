
filetext = ""
with open("input.txt") as f:
    filetext = f.read()

patterns = filetext.split('\n\n')
patterns2 = [pattern.strip() for pattern in patterns]
patterns = patterns2
def get_reflection(pattern:str) -> int:
    lines = pattern.splitlines()

    for line in range(1, len(lines)//2 + 1):
        if lines[0:line] == lines[line:line*2][::-1]:
            return (line, 0)
    
    lines = lines[::-1]
    for line in range(1,len(lines)//2 + 1):
        if lines[0:line] == lines[line:line*2][::-1]:
            return (len(lines) - line, 0)
        
    new_lines = []
    for column_number in range(len(lines[0])):
        new_lines.append(''.join([line[column_number] for line in lines]))
    lines = new_lines

    for line in range(1, len(lines)//2 + 1):
        if lines[0:line] == lines[line:line*2][::-1]:
            return (line, 1)
    
    lines = lines[::-1]
    for line in range(1,len(lines)//2 + 1):
        if lines[0:line] == lines[line:line*2][::-1]:
            return (len(lines) - line, 1)

arr2 = []
for pattern in patterns:
    value, vert = get_reflection(pattern)
    # change one character in pattern from # to . or vice versa
    arr = []
    to_append = 0
    for char in range(len(pattern)):
        if pattern[char] != "\n":
            arr = [char2 for char2 in pattern]
            if arr[char] == "#":
                arr[char] = "."
            else:
                arr[char] = "#"
            new_value = get_reflection(''.join(arr))
            if new_value is not None:
                if new_value[0] != value:
                    if new_value[1] == 0:
                        to_append = 100 * new_value[0]
                    else:
                        to_append = new_value[0]
                    break
    arr2.append(to_append)

print(arr2)