def get_max_ind(char_list):
    max_val = max(char_list)
    max_ind = char_list.index(max_val)

    return max_val, max_ind

total_v = 0
with open("/home/moosthuizen/AOC/aoc2025/day3/input.txt") as f:
    for line in f:
        m1, m2 = "", ""
        
        char_list = list(line.strip())
        line_len = len(char_list)
        max_val, max_ind = get_max_ind(char_list)
        if max_ind == line_len-1:
            m2 = max_val
            m1, _ = get_max_ind(char_list[:max_ind])
        else:
            m1 = max_val
            m2, _ = get_max_ind(char_list[max_ind+1:])
        total_v += int(m1+m2)

print(total_v)

        