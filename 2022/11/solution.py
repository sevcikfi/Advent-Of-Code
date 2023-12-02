INPUT_FILE = "11/input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "11/test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]

def solve1(filename : str):
    #TODO: write parser, read input, throw it in and run the loop for 20 iterations.
    return 1    

def solve2(filename : str):
    return 2


class Monkey:
    def __init__(self, items, multiplier, divisible, throw):
        self.iter:int = 0
        self.items:list[int] = items
        self.multi:int = multiplier
        self.div:int = divisible
        self.throw:list[int] = throw
    
    def accept(self, item:int):
        self.items.append(item)
    

def Testing(bool=True):
    if not bool: return 1
    return 2

def main():
    Testing()
    assert solve1(TEST_FILE) == 1, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 2, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()