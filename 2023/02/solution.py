INPUT_FILE = "02\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "02\\test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number
import re

def getInput(filename: str):
    with open(filename, 'r') as file:
        #return {i:[item.strip().split(", ") for item in line.split(":")[1].strip().split(";")] for i, line in enumerate(file.readlines())}
        #return [line.strip().split(":")[1].strip().split("; ") for line in file.read().strip().split("\n")]
        return [line.strip().split(":")[1].strip() for line in file.read().strip().split("\n")]

def solve1(filename : str):
    ids = []
    for i,line in enumerate(getInput(filename)):
        for r,g,b in re.findall(r"(\d+) red|(\d+) green|(\d+) blue", line):
            if r:
                if int(r) > 12: break
            if g:
                if int(g) > 13: break
            if b:
                if int(b) > 14: break
        else:
            ids.append(i+1)
    return sum(ids)

def solve2(filename : str):
    powers = []
    for line in getInput(filename):
        minR, minG, minB = 0,0,0
        for r,g,b in re.findall(r"(\d+) red|(\d+) green|(\d+) blue", line):
            if r:
                if int(r) > minR: minR = int(r)
            if g:
                if int(g) > minG: minG = int(g)
            if b:
                if int(b) > minB: minB = int(b)
        powers.append(minR * minG * minB)
    return sum(powers)

def Testing(bool=True):
    if not bool: return

def main():
    assert solve1(TEST_FILE) == 8, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 2286, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()