hands = []
bids = []
values = []

with open("input.txt") as f:
    for line in f:
        hand = line[0:5]
        bid = int(line[6:].strip())
        hands.append(hand)
        bids.append(bid)

card_dict = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 0,
    "Q": 10,
    "K": 11,
    "A": 12,
}

array13 = [13**i for i in range(6)]


def convert_cards_to_int(hand):
    ret = 0
    for index, card in enumerate(hand[::-1]):
        ret += card_dict[card] * array13[index]
    ret += convert_hand_to_int(hand) * array13[5]
    return ret


def convert_hand_to_int(hand):
    sethand = set(hand)
    if "J" in sethand:
        if len(sethand) == 1:
            return 6
        if len(sethand) == 2:
            return 6
        if len(sethand) == 3:
            Jcount = hand.count("J")
            if Jcount == 1 and max([hand.count(i) for i in sethand]) == 2:
                return 4
            else:
                return 5
        if len(sethand) == 4:
            return 3
        if len(sethand) == 5:
            return 1
    else:
        # five of a kind
        if len(sethand) == 1:
            return 6
        # one pair
        if len(sethand) == 4:
            return 1
        # high card
        if len(sethand) == 5:
            return 0
        # three of a kind & 2 pair
        if len(sethand) == 3:
            arr = [hand.count(i) for i in sethand]
            if max(arr) == 3:
                return 3
            else:
                return 2
        if len(sethand) == 2:
            arr = [hand.count(i) for i in sethand]
            if max(arr) == 4:
                return 5
            else:
                return 4


values = [convert_cards_to_int(i) for i in hands]


sorted_pairs = sorted(zip(values, bids))

count = 0

values, bids = zip(*sorted_pairs)

for index, bid in enumerate(bids):
    count += bid * (index + 1)

print(count)
