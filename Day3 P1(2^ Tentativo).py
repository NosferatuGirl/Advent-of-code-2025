"DAY 3 P1"
total = 0
with open("input3.txt", "r", encoding="utf-8") as inFile:
    for joltage in inFile:
        joltage = joltage.strip()
        if joltage != "":
            max_val = 0
            len_joltgage = len(joltage)
            for i in range(len_joltgage):
                for j in range(i + 1, len_joltgage):
                    val = int(joltage[i]) * 10 + int(joltage[j])
                    if val > max_val:
                        max_val = val
            total += max_val
print(total)
