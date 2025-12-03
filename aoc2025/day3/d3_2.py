def get_max_ind(char_list):
    max_val = max(char_list)
    max_ind = char_list.index(max_val)

    return max_val, max_ind

n = 12

total_v = 0
with open("/home/moosthuizen/AOC/aoc2025/day3/input.txt") as f:
    for line in f:
        char_list = list(line.strip())
        line_len = len(char_list)
        prev_ind = -1
        left = 12
        chars = []
        for i in range(n):
            s_start = prev_ind+1
            s_end = line_len-left+1
            max_val, rel_ind = get_max_ind(char_list[s_start:s_end])
            max_ind = s_start+rel_ind
            left = left-1
            prev_ind = max_ind
            chars.append(max_val)
        total_v += int("".join(chars))
print(total_v)
