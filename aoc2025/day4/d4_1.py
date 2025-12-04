import numpy as np
from scipy.signal import convolve2d

check_kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

# Fewer than 4 rolls in the eight adjacent positions

lines = []
with open("aoc2025/day4/input.txt") as f:
    for line in f:
        r = []
        for char in line.strip():
            if char == "@":
                r.append(1)
            else:
                r.append(0)
        lines.append(r)

rolls = 0

data = np.array(lines)
data_padded = np.pad(data, pad_width=1, mode='constant', constant_values=0)
rows, cols = data.shape

conv_check = convolve2d(data_padded, check_kernel, mode='valid')

final_result = data * conv_check

print(np.where((0 < final_result) & (final_result < 5), 1, 0).sum())

