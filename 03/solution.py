INPUT_FILE = "03\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]

def solve1(filename : str):
    priorities: list[int] = [] #[int] didn't work xd
    for sack in getInput(filename):
        for item in sack[:int(len(sack)/2)]:
            if item in (sack[int(len(sack)/2):]):
                if item.islower():
                    priorities.append(ord(item) - 96)
                    break
                priorities.append(ord(item) - 38)
                break   
    return sum(priorities)

def solve2(filename : str):
    priorities: list[int] = []
    for group in zip(*[iter(getInput(filename))]*3):
        for item in group[0]:
            if item in group[1]:
                if item in group[2]:
                    if item.islower():
                        priorities.append(ord(item) - 96)
                        break
                    priorities.append(ord(item) - 38)
                    break   
    return sum(priorities)

def main():
    print(f"solution 1: {solve1(INPUT_FILE)}")
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()