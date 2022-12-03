INPUT_FILE = "<number>\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(name: str) -> list[str]:
    with open(INPUT_FILE, 'r') as file:
        raw_input = file.readlines()
    return raw_input
    #return [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def solve1():
    return 1    

def solve2():
    return 2

def main():
    print(f"solution 1: {solve1()}")
    print(f"solution 2: {solve2()}")
    
if __name__ == "__main__":
    main()