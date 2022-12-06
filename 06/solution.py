INPUT_FILE = "06\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "06\\test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.readline()

def solve1(filename : str):
    kyuu: list[str]= []
    for i,char in enumerate(getInput(filename)):
        kyuu.append(char)
        if len(set(kyuu)) > 3: return i+1
        if len(kyuu) > 3: del kyuu[0]
    return -1    

def solve2(filename : str):
    kyuu: list[str]= []
    for i,char in enumerate(getInput(filename)):
        kyuu.append(char)
        if len(set(kyuu)) > 13: return i+1
        if len(kyuu) > 13: del kyuu[0]
    return -2

def main():
    assert solve1(TEST_FILE) == 7, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 19, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()