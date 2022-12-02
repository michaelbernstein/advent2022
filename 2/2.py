lines = open('input2.txt', 'r').readlines()

scores_one = {
    "A X": 3, "A Y": 6, "A Z": 0,
    "B X": 0, "B Y": 3, "B Z": 6,
    "C X": 6, "C Y": 0, "C Z": 3
}

# Part 1
count = 0
for l in lines:
    count += scores_one[l.strip()] + (ord(l[2]) - 87)
print(count)


# Part 2
shape_score = {"A": 1, "B": 2, "C": 3}

counters = {
    "A": "B",
    "B": "C",
    "C": "A"
}
reverse_counters = dict(zip(counters.values(), counters.keys()))


def score(shape, result):
    match result:
        case "X":
            return shape_score[reverse_counters[shape]]
        case "Y":
            return shape_score[shape] + 3
        case "Z":
            return shape_score[counters[shape]] + 6
        case _:
            raise Exception("Shape doesn't exist")

count = 0
for l in lines:
    t = l.strip().split()
    count += score(t[0], t[1])
print(count)
