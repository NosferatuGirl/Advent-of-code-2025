"Day 2"
#rts->range_texts/rt->range_text
#example: 24-46 
#X"-"
#first_id->24
#last_id->46
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

#start_id/end_id == inizio_id/fine_id

max_end = ranges[0][1]
for coppia in ranges:
    inizio_id = coppia[1]
    if inizio_id > max_end:
        max_end = inizio_id

max_digits = len(str(max_end))
max_half_len = max_digits // 2

total = 0
half_len = 1
while half_len <= max_half_len:
    start = 10 ** (half_len - 1)
    end = 10 ** half_len
    for number in range(start, end):
        text_id = str(number)
        number_id = int(text_id + text_id)
        if number_id <= max_end:
            count = 0
            for min_id, max_id in ranges:
                if min_id <= number_id <= max_id:
                    count += 1
            if count > 0:
                total += number_id
    half_len += 1
print(total)