with open("./input.txt") as input:
    txt = input.read()
    elves = [
        [int(calories) for calories in elf.splitlines()] for elf in txt.split("\n\n")
    ]
    max_calories_per_elf = max([sum(calories) for calories in elves])
    print(max_calories_per_elf)
