two = 0
three = 0
with open("input") as f:
    lines = f.readlines()
for line in lines:
    counts = []
    letters = set(line)
    for letter in letters:
        counts.append(line.count(letter))
    two += 2 in counts
    three += 3 in counts
print(two * three)
