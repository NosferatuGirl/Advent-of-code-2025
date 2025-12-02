"Day 2 P2"
# rts -> range_texts / rt -> range_text
# example: 24-46
# X"-"
# first_id -> 24
# last_id  -> 46

with open("input2.txt", "r", encoding="utf-8") as inFile:
    text = inFile.read().strip()

rts = text.split(",")
ranges = []
for rt in rts:
    rt = rt.strip()
    if rt != "":
        start_id, end_id = rt.split("-")
        first_id = int(start_id)
        last_id = int(end_id)
        if first_id > last_id:
            first_id, last_id = last_id, first_id
        ranges.append((first_id, last_id))

# start_id/end_id == inizio_id/fine_id

max_end = ranges[0][1]
for coppia in ranges:
    fine_id = coppia[1]
    if fine_id > max_end:
        max_end = fine_id

max_digits = len(str(max_end))
max_half_len = max_digits // 2

total = 0
#repeated_Ranges->rr
rr = set() 

half_len = 1
while half_len <= max_half_len:
    start = 10 ** (half_len - 1)
    end = 10 ** half_len
    max_repeats = max_digits // half_len
    for number in range(start, end):
        text_id = str(number)
        repeat = 3
        while repeat <= max_repeats:
            full_text = text_id * repeat
            number_id = int(full_text)
            if number_id not in rr:
                count = 0
                for min_id, max_id in ranges:
                    if min_id <= number_id <= max_id:
                        count += 1
                if count > 0:
                    total += number_id
                    rr.add(number_id)
            repeat += 1
    half_len += 1

print(total)