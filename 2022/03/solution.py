INPUT_FILE = "03\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]

##first solution
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

##first rewrite
def priority(item : str) -> int:
    if item.islower():
        return ord(item) - 96
    return ord(item) - 38

def solve1_alt(filename):
    priorities: list[int] = []
    for sack in getInput(filename):
        right, left = sack[:len(sack)//2], sack[len(sack)//2:]
        priorities.append(priority(set(right).intersection(set(left)).pop()))
    return sum(priorities)

def solve2_alt(filename):
    priorities: list[int] = []
    for group in zip(*[iter(getInput(filename))]*3):
        priorities.append(priority(set(group[0]).intersection(set(group[1]).intersection(set(group[2]))).pop()))
    return sum(priorities)

##completely final solution
def priority_alt(item : str) -> int:
    if item.islower():return ord(item) - ord("`")
    else: return ord(item) - ord("&")

def solve1_alt2(filename):
    return sum(priority_alt(set(sack[:len(sack)//2]).intersection(set(sack[len(sack)//2:])).pop()) for sack in getInput(filename))

def solve2_alt2(filename):
    return sum(priority_alt(set(group[0]).intersection(set(group[1]).intersection(set(group[2]))).pop()) for group in zip(*[iter(getInput(filename))]*3))

##completely final solution
def priority_alt2(item : str) -> int:  
    return ord(item) - ord("`") if item.islower() else ord(item) - ord("&")

def solve1_alt3(filename):
    return sum(priority_alt2(set(sack[:len(sack)//2]).intersection(set(sack[len(sack)//2:])).pop()) for sack in getInput(filename))

def solve2_alt3(filename):
    return sum(priority_alt2(set(elf1).intersection(set(elf2).intersection(set(elf3))).pop()) for elf1,elf2,elf3 in zip(*[iter(getInput(filename))]*3))

##oneliners babyyyyyyyy
def solve1_oneline(filename):
        return sum(map(lambda x: ord(x) - ord("`") if x.islower() else ord(x) - ord("&"),((set(sack[:len(sack)//2]).intersection(set(sack[len(sack)//2:])).pop()) for sack in getInput(filename))))

def solve2_oneline(filename):
        return sum(map(lambda x: ord(x) - ord("`") if x.islower() else ord(x) - ord("&"),((set(elf1).intersection(set(elf2).intersection(set(elf3))).pop()) for elf1,elf2,elf3 in zip(*[iter(getInput(filename))]*3))))


def main():
    print(f"solution 1: {solve1_oneline(INPUT_FILE)}")
    print(f"solution 2: {solve2_oneline(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()