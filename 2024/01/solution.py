YEAR = 2024  # change number for the correct year
DAY  = 1  # change the number because conda runs in root of repo
INPUT_FILE = f"{YEAR}\\{DAY:02d}\\input.txt" 
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = f"{YEAR}\\{DAY:02d}\\test.txt" # test file

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file: #pre split/process input here
        return [line.strip() for line in file.read().strip().split("\n")]

def solve1(filename : str):
    firsts, seconds = [], []
    
    for line in getInput(filename):
        a, b = line.split()
        firsts.append(int(a))
        seconds.append(int(b))
    
    firsts.sort()
    seconds.sort()
    
    sum = 0
    for a, b in zip(firsts, seconds):
        sum += abs(a - b)
    
    return sum

def solve2(filename : str):
    left = []
    right = []
    for line in getInput(filename):
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    print(left)
    print(right)
    
    sum = 0
    for l in left:
        n = 0
        for r in right:
            if l == r:
                n += 1
        print(l, n)
        sum += n * l

    
    return sum

def Testing(bool=True):
    if not bool: return

def main():
    assert solve1(TEST_FILE) == 11, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 31, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()