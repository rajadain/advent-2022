# https://adventofcode.com/2022/day/2

rules = {
    "A": {
        "X": 1 + 3,
        "Y": 2 + 6,
        "Z": 3 + 0,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 1 + 6,
        "Y": 2 + 0,
        "Z": 3 + 3,
    },
}

with open("./input.txt") as input:
    pairs = [(line[0], line[2]) for line in input.readlines()]
    score = sum([rules[i][j] for i, j in pairs])
    print(score)
