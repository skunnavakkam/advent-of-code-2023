
import re

ret = 0
line_count = 0
with open("input.txt") as f:
    for line in f:
        nums = [int(i) for i in re.findall("\d+", line)]
        onsens = line.split(" ")[0] * 5
        questioncount = onsens.count("?")
        ret += 2**questioncount
        # for i in range(2**questioncount):
        #     bits = format(i, f'0{questioncount}b')
        #     bits = bits.replace("0",".")
        #     bits = bits.replace("1","#")


        #     temp_arr = []
        #     question_number = 0
        #     for character in onsens:
        #         if character == "?":
        #             temp_arr.append(bits[question_number])
        #             question_number += 1
        #         else:
        #             temp_arr.append(character)
            
        #     onsens_copy = "".join(temp_arr).split(".")
        #     # remove empty strings
        #     onsens_copy = [i for i in onsens_copy if i != ""]
        #     if [len(i) for i in onsens_copy] == nums:
        #         ret += 1
        # line_count += 1
        # if line_count % 10 == 0:
        #     print(line_count)

print(ret)
