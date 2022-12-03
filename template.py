INPUT_FILE = "<number>\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]

def solve1(filename : str):
    return 1    

def solve2(filename : str):
    return 2

def main():
    print(f"solution 1: {solve1(INPUT_FILE)}")
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()