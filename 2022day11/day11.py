import re


class Monkey:
    def __init__(self, input_string) -> None:
        self.operator_number = "square"
        self.is_square = False
        self.number_of_items_inspected = 0
        lines = input_string.split("\n")
        for line in lines:
            if line.strip().startswith("Starting items: "):
                self.starting_items = [int(i) for i in re.findall("\d+", line)]
            elif line.strip().startswith("Test"):
                self.divisor = int(re.findall("[0-9]+", line)[0])
            elif line.strip().startswith("If true"):
                self.monkey_true = int(re.findall("[0-9]+", line)[0])
            elif line.strip().startswith("If false"):
                self.monkey_false = int(re.findall("[0-9]+", line)[0])
            elif line.strip().startswith("Operation"):
                if line.count("old") > 1:
                    self.is_square = True
                else:
                    if "*" in line:
                        self.operator = "*"
                    else:
                        self.operator = "+"
                    self.operator_number = int(re.findall("[0-9]+", line)[0])

    def operation(self, x):
        if self.is_square:
            return x * x
        elif self.operator == "*":
            return x * self.operator_number
        else:
            return x + self.operator_number

    def __str__(self):
        return f"""
        Starting items: {self.starting_items}
        Operation: {self.operation(3)}
        Test: divisible by {self.divisor}
        If true: throw to monkey {self.monkey_true}
        If false: throw to monkey {self.monkey_false}   
            """


if __name__ == "__main__":
    with open("filename.txt", "r") as file:
        file_contents = file.read()
    monkeys = [Monkey(splitted) for splitted in file_contents.split("\n\n")]

    modulo = 1
    for monkey in monkeys:
        modulo *= monkey.divisor

    for i in range(10000):
        for index, monkey in enumerate(monkeys):
            for worry_level in monkey.starting_items:
                monkey.number_of_items_inspected += 1
                # worry_level = monkey.operation(worry_level) // 3
                worry_level = monkey.operation(worry_level) % modulo
                if worry_level % monkey.divisor == 0:
                    monkeys[monkey.monkey_true].starting_items.append(worry_level)
                else:
                    monkeys[monkey.monkey_false].starting_items.append(worry_level)
            monkey.starting_items = []

    items_inspected = [monkey.number_of_items_inspected for monkey in monkeys]
    items_inspected.sort()
    print(items_inspected[-1] * items_inspected[-2])
