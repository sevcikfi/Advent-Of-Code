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
        for win in tuple(int(split[1][i:i+3].strip()) for i in range(0, len(split[1].strip()), 3)):
            if win in tuple(int(split[2][i:i+3].strip()) for i in range(0, len(split[2].strip()), 3)):
                points = points + 1
        if points > 0:
            score.append(2**(points-1))
    return sum(score)

def solve2(filename : str):
    score = [0]*200
    for i, card in enumerate(getInput(filename)):
        score[i] = score[i] + 1
        split = re.split(":|\|", card)
        hits = 0
        for win in tuple(int(split[1][i:i+3].strip()) for i in range(0, len(split[1].strip()), 3)):
            if win in tuple(int(split[2][i:i+3].strip()) for i in range(0, len(split[2].strip()), 3)):
                hits = hits + 1
                score[i + hits] = score[i + hits] + score[i]
    return sum(score)

def Testing(bool=True):
    if not bool: return

def main():
    assert solve1(TEST_FILE) == 13, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 30, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()