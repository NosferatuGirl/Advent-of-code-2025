"P2"
inFile = open("input1.txt", "r", encoding="utf-8")
lines = []
for line in inFile:
    line = line.strip()
    if line != "":
        lines.append(line)
inFile.close()
pi = 50 # posizione iniziale
totPassZero = 0 # passaggi totali dallo 0
for line in lines:
    direction = line[0]
    distance = int(line[1:])
    if direction == 'R':
        passZero = (pi+distance)// 100
        pi = (pi+distance)%100
    elif direction == 'L':
        if pi == 0:
            shiftPi = 0
        else:
            shiftPi = 100 - pi
        passZero = (shiftPi + distance) // 100
        pi = (pi-distance)%100
    totPassZero += passZero

print(totPassZero)