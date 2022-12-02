INPUT_FILE = "02\input.txt" # change the number because conda runs in root of repo
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(name: str) -> list[str]:
    with open(INPUT_FILE, 'r') as file:
        raw_input = file.readlines()

    return raw_input

# A - rock, B - paper, C - scissors
# X - rock, Y - paper, Z - scissors
def solve1():
    raw = getInput(INPUT_FILE)
    total = 0
    for round in raw:
        if "X" in round:
            total += 1
            if "A" in round: total += 3
            if "B" in round: total += 0
            if "C" in round: total += 6
            continue
        if "Y" in round:
            total += 2
            if "A" in round: total += 6
            if "B" in round: total += 3
            if "C" in round: total += 0
            continue
        if "Z" in round:
            total += 3
            if "A" in round: total += 0
            if "B" in round: total += 6
            if "C" in round: total += 3
            continue
    return total
    
# A - rock 1, B - paper 2, C - scissors 3
# X - lose 0, Y - draw 3, Z - win 6
def solve2():
    raw = getInput(INPUT_FILE)
    total = 0
    for round in raw:
        if "X" in round:
            total += 0
            if "A" in round: total += 3
            if "B" in round: total += 1
            if "C" in round: total += 2
            continue
        if "Y" in round:
            total += 3
            if "A" in round: total += 1
            if "B" in round: total += 2
            if "C" in round: total += 3
            continue
        if "Z" in round:
            total += 6
            if "A" in round: total += 2
            if "B" in round: total += 3
            if "C" in round: total += 1
            continue
    return total

def main():
    print("solution 1: {}".format(solve1()))
    print("solution 2: {}".format(solve2()))
    
if __name__ == "__main__":
    main()
