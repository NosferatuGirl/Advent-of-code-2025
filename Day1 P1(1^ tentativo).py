"P1"
pos = 50          # posizione iniziale
count_zero = 0    # quante volte finiamo su 0

inFile=open("input1.txt","r",encoding="utf-8");
for line in inFile:
    line = line.strip()
    # Se la riga non è vuota, la processiamo
    if line:
        direction = line[0]      # 'R' o 'L'
        steps = int(line[1:])    # il numero dopo la lettera
        if direction == "R":
            pos = pos + steps
            while pos >= 100:
                pos -= 100
        else: 
            pos = pos - steps
            while pos < 0:
                pos += 100
        if pos == 0:
            count_zero += 1
print(count_zero)