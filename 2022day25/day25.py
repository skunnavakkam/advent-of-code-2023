def snafu_to_decimal(snafu):
    ret = 0
    for index, letter in enumerate(snafu[::-1]):
        if letter == "-":
            ret -= 5**index
        elif letter == "=":
            ret -= 2 * (5**index)
        else:
            ret += int(letter) * 5**index
    return ret


trans_rev = {4: "-", 3: "=", 2: "2", 1: "1", 0: "0"}


def decimal_to_snafu(decimal: int) -> str:
    snafu = ""
    while decimal > 0:
        rem, decimal = decimal % 5, round(decimal / 5)
        snafu += trans_rev[rem]
    return snafu[::-1]


with open("input.txt") as f:
    total = 0
    for line in f:
        total += snafu_to_decimal(line.strip())
        print()
    print(decimal_to_snafu(total))
