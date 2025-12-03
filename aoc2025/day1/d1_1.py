class Dial():
    def __init__(self):
        self.val = 50
        self.max = 99

        self.total_0 = 0

    def get_true_steps(self, steps):
        trips = steps // (self.max + 1)
        self.total_0 += trips
        return steps - (trips * (self.max + 1))

    def forward(self, steps):
        total_steps = self.val + self.get_true_steps(steps)
        if total_steps > self.max:
            if not self.val == 0:
                self.total_0 += 1
            self.val = abs(self.max - total_steps + 1)
        else:
            self.val = total_steps
            if self.val == 0:
                self.total_0 += 1

    def back(self, steps):
        total_steps = self.val - self.get_true_steps(steps)
        if total_steps < 0:
            if not self.val ==0:
                self.total_0 += 1
            self.val = abs(self.max + total_steps +1)
        else:
            self.val = total_steps
            if self.val == 0:
                self.total_0 += 1

        

d = Dial()

with open("/home/moosthuizen/AOC/aoc2025/day1/input.txt") as f:
    for line in f:
        # print(line)
        direction = line[0]
        dist = int(line[1:])
        if direction == 'L':
            d.back(dist)
        if direction == 'R':
            d.forward(dist)

        # print(d.val, d.total_0)

print(d.total_0)