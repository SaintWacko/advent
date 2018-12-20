freq = 0
past_freq = []
with open("input") as f:
    lines = f.readlines()
while True:
    for line in lines:
        freq += int(line)
        if freq in past_freq:
            print(freq)
            quit()
        else:
            past_freq.append(freq)
