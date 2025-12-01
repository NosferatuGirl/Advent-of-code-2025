"P1"
inFile = open("input1.txt", "r", encoding="utf-8");
lines = []
for line in inFile:
    line = line.strip()
    if line != "":
        lines.append(line)
inFile.close()
pi = 50 #posizione iniziale
count = 0 
for line in lines:
    direction = line[0]
    distance = int(line[1:])
    if direction == 'R':
        pi = pi + distance
        while pi >= 100:
            pi = pi - 100
    elif direction == 'L':
        pi = pi - distance
        while pi < 0:
            pi = pi + 100
    if pi == 0:
        count += 1
print(count)