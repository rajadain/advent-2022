with open("../1a/input.txt") as input:
    txt = input.read()
    elves = [
        [int(calories) for calories in elf.splitlines()] for elf in txt.split("\n\n")
    ]
    calories_per_elf = [sum(calories) for calories in elves]
    top3 = sorted(calories_per_elf, reverse=True)[:3]
    print(sum(top3))
