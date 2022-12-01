INPUT_FILE = "01\input.txt" # change the number because conda runs in root of repo
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(name: str):
    with open(INPUT_FILE, 'r') as file:
        raw_input = file.read()
    return raw_input

def solve1():
    raw = getInput(INPUT_FILE)
    elves = raw.split("\n\n")
    return sorted([sum(int(calorie) for calorie in elf.split("\n")) for elf in elves], reverse=True)
    
    elves = []
    for group in groups:
        x = group.split("\n")
        elves.append(sum([int(y) for y in x]))
    return sorted(elves, reverse=True)

def solve2():
    return sum(solve1()[0:3])

def main():
    print("solution 1: {}".format(solve1()[0]))
    print("solution 2: {}".format(solve2()))
    
if __name__ == "__main__":
    main()
