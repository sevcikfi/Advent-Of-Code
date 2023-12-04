INPUT_FILE = "04\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "04\\test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]
import re
def solve1(filename : str):
    score: list[int] = []
    for line in getInput(filename):
        points = 0
        split = re.split(":|\|", line)
        print(split)
        c, wins, mine = split
        for win in tuple(int(wins[i:i+3].strip()) for i in range(0,len(wins.strip()), 3)):
            if win in tuple(int(mine[i:i+3].strip()) for i in range(0,len(mine.strip()), 3)):
                points = points + 1
        print(points)
        if points < 1:
            continue
        score.append(2**(points-1))
    print(score)
    return sum(score)

def solve2(filename : str):
    return 2

def Testing(bool=True):
    if not bool: return

def main():
    assert solve1(TEST_FILE) == 13, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 2, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()