#!/usr/bin/env python3

class Forest():
    def __init__(self, f):
        """
            f is the full data of the forest
        """
        self.x_pos = 0
        self.y_pos = 0
        self.forest = list()
        for l in f.splitlines():
            self.ingest_line(l)

    def ingest_line(self, line):
        """
            Will ingest a line and store it
            in the forest by appending it.
        """
        self.forest.append(list(line))

    def down_the_slope(self, right, down):
        """
            Updates the position
        """
        self.x_pos += right
        self.y_pos -= down

    def __str__(self):
        for row in self.forest:
            print(''.join(row))
        return ""


test_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

f = Forest()
for l in test_data.splitlines():
    f.ingest_line(l)

print("Now print what I have")
print(f)