
# def get_factors(number):
#     factors = []
#     for i in range(1, number+1):
#         if number%i == 0:
#             factors.append(i)
#     return factors

# def chunk(num_list, factor):
#     len_i = len(num_list)

#     split_lists = []

#     for i in range(0, len_i, factor):
#         split_lists.append(num_list[i:i+factor])

#     jaditis = []
#     for i in range(1,len(split_lists)):
#         ja = split_lists[0] == split_lists[i]
#         jaditis.append(ja)
#         if ja == False:
#             return False
#     if len(jaditis) == 0:
#         return False
#     return all(jaditis)



# with open("/home/moosthuizen/AOC/aoc2025/day2/input.txt") as f:
#     ranges = [(int(num.split("-")[0]), int(num.split("-")[1])) for num in f.readline().split(",")]

# invalid_numbers = []

# for r in ranges:
#     for i in range(r[0],r[1]+1,1):
#         i_str = list(str(i))
#         len_i = len(i_str)
#         factors = get_factors(len_i)

#         for f in factors:
#             if f != len_i:
#                 t = chunk(i_str, f)
#                 if t == True:
#                     invalid_numbers.append(i)
#                     break

# print(sum(invalid_numbers))


def is_repetition(s: str) -> bool:
    """
    Returns True if s is composed of repeated substrings.
    Example: '1212' -> True, '123' -> False
    """
    return (s + s)[1:-1].find(s) != -1


with open("/home/moosthuizen/AOC/aoc2025/day2/input.txt") as f:
    ranges = [
        (int(a), int(b))
        for a, b in (part.split("-") for part in f.readline().split(","))
    ]

invalid_numbers = []

for start, end in ranges:
    for n in range(start, end + 1):
        if is_repetition(str(n)):
            invalid_numbers.append(n)

print(sum(invalid_numbers))
