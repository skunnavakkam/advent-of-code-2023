lines = []
with open("input.txt") as f:
    lines = f.readlines()


def e_next(seq):
    if not any(seq):
        return 0
    else:
        eseq = [a - b for a, b in zip(seq[1:], seq[:-1])]
        # print(eseq)
        e = e_next(eseq)
        e = seq[-1] + e
        # print(f"next = {e}")
        return e


seqs = [[int(x) for x in line.split()] for line in lines]
print(sum(e_next(seq) for seq in seqs))
