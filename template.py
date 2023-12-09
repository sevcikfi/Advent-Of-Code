DAY = 0  # change the number because conda runs in root of repo
INPUT_FILE = f"{DAY:02d}\\input.txt" 
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = f"{DAY:02d}\\test.txt" # test file

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file: #pre split/process input here
        return [line.strip() for line in file.read().strip().split("\n")]

def solve1(filename : str):
    return 1    

def solve2(filename : str):
    return 2

def Testing(bool=True):
    if not bool: return

def main():
    assert solve1(TEST_FILE) == 1, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 2, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()