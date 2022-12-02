# https://adventofcode.com/2022/day/2

rules = {
    "A": {
        "X": 0 + 3,
        "Y": 3 + 1,
        "Z": 6 + 2,
    },
    "B": {
        "X": 0 + 1,
        "Y": 3 + 2,
        "Z": 6 + 3,
    },
    "C": {
        "X": 0 + 2,
        "Y": 3 + 3,
        "Z": 6 + 1,
    },
}

with open("../2a/input.txt") as input:
    pairs = [(line[0], line[2]) for line in input.readlines()]
    score = sum([rules[i][j] for i, j in pairs])
    print(score)
