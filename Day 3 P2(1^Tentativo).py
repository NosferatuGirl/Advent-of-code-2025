"DAY 3 P2"
total = 0
batteries = 12
with open("input3.txt", "r", encoding="utf-8") as inFile:
    for joltage in inFile:
        joltage = joltage.strip()
        if joltage != "":
            len_joltage = len(joltage)
            start = 0
            result = ""
            for pos in range(batteries):
                best_digit = "0"
                remaining_pos = batteries - pos
                last = len_joltage - remaining_pos
                best = start
                for i in range(start, last + 1):
                    if joltage[i] > best_digit: 
                        best_digit = joltage[i]
                        best = i
                result += best_digit
                start = best + 1
            total += int(result)
print(total)