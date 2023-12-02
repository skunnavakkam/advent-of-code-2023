with open("input.txt") as f:
    text = f.read().split("\n\n")
    for pair in text:
        list1 = eval(pair.split("\n")[0])
        list2 = eval(pair.split("\n")[1])
