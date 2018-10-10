f = open("result/htop_result.txt", "r")

mode = 0
single_left = []
single_right = []
random_left = []
random_right = []
mixed_left = []
mixed_right = []

for line in f.readlines():
    lines = line.split()
    if len(lines) == 1:
        mode += 1
        continue
    if (mode == 1):
        single_left.append(float((lines[0])))
        single_right.append(float(lines[1]))
    if (mode == 2):
        random_left.append(float((lines[0])))
        random_right.append(float(lines[1]))
    if (mode == 3):
        mixed_left.append(float((lines[0])))
        mixed_right.append(float(lines[1]))

f.close()
print single_left