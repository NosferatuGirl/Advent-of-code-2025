"DAY 4 P2"
def main():
    def read_map(filename):
        map_rolls = []
        with open(filename, "r", encoding="utf-8") as inFile:
            for line in inFile:
                line = line.strip()
                if line != "":
                    map_rolls.append(line)
        return map_rolls

    def close_rolls(map_rolls, r, c):
        rows = len(map_rolls)
        col = len(map_rolls[0])
        count = 0
        if r > 0:
            if map_rolls[r-1][c] == "@":
                count += 1
            if c > 0 and map_rolls[r-1][c-1] == "@":
                count += 1
            if c < col - 1 and map_rolls[r-1][c+1] == "@":
                count += 1
        if c > 0 and map_rolls[r][c-1] == "@":
            count += 1
        if c < col - 1 and map_rolls[r][c+1] == "@":
            count += 1
        if r < rows - 1:
            if map_rolls[r+1][c] == "@":
                count += 1
            if c > 0 and map_rolls[r+1][c-1] == "@":
                count += 1
            if c < col - 1 and map_rolls[r+1][c+1] == "@":
                count += 1
        return count

    # P1
    def availabable_rolls(map_rolls):
        rows = len(map_rolls)
        col = len(map_rolls[0])
        available_rolls = 0
        for r in range(rows):
            for c in range(col):
                if map_rolls[r][c] == "@":
                    close_count = close_rolls(map_rolls, r, c)
                    if close_count < 4:
                        available_rolls += 1
        return available_rolls

    def remove_available(map_rolls):
        rows = len(map_rolls)
        col = len(map_rolls[0])
        new_map_rolls = []
        removed = 0
        for r in range(rows):
            line = ""
            for c in range(col):
                if map_rolls[r][c] == "@":
                    close_count = close_rolls(map_rolls, r, c)
                    if close_count < 4:
                        line = line + "."
                        removed += 1
                    else:
                        line = line + "@"
                else:
                    line = line + map_rolls[r][c]
            new_map_rolls.append(line)
        return new_map_rolls, removed

    # P2
    def tot_removed_rolls(map_rolls):
        tot_removed = 0
        map_rolls, removed = remove_available(map_rolls)
        tot_removed += removed
        while removed > 0:
            map_rolls, removed = remove_available(map_rolls)
            tot_removed += removed
        return tot_removed
    
    map_rolls = read_map("input4.txt")
    # P1
    print(availabable_rolls(map_rolls))
    # P2
    print(tot_removed_rolls(map_rolls))

main()