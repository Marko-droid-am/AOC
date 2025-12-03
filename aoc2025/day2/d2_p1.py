

def repeated_pattern(s):
    n = len(s)
    lps = [0] * n  # longest prefix suffix

    # Build LPS (prefix-function / failure function from KMP)
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]
        if s[i] == s[j]:
            j += 1
            lps[i] = j

    length_of_smallest_block = n - lps[-1]

    if n % length_of_smallest_block == 0:
        pattern = s[:length_of_smallest_block]
        count = n // length_of_smallest_block
        return pattern, count

    return None , None # no repetition


with open("/home/moosthuizen/AOC/aoc2025/day2/input.txt") as f:
    ranges = [(int(num.split("-")[0]), int(num.split("-")[1])) for num in f.readline().split(",")]

invalid_numbers = []

for r in ranges:
    for i in range(r[0], r[1]+1, 1):
        i_str = str(i)
        pattern, count = repeated_pattern(i_str)


print(sum(invalid_numbers))