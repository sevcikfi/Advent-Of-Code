INPUT_FILE = "05\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "05\\test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]

def move(times: int, origin: str, dest: str, ship: dict[str,list[str]]):
    if times > 1: move(times-1, origin, dest, ship)
    ship[dest].append(ship[origin].pop())

def solve1(filename : str):
    ship: dict[str,list[str]]= {}
    for  line in getInput(filename):
        if not line: continue
        if line[0].isdigit(): ship[line[0]] = line[2:].split(" "); continue
        times, origin, dest = line.split(" ")[1::2]
        move(int(times), origin, dest, ship)
    return ''.join([v[-1] for v in ship.values()])

def solve2(filename : str):
    ship: dict[str,list[str]]= {}
    for  line in getInput(filename):
        if not line: continue
        if line[0].isdigit(): ship[line[0]] = line[2:].split(" "); continue
        times, origin, dest = line.split(" ")[1::2]
        ship[dest].extend((list(reversed([ship[origin].pop() for i in range(int(times))]))))
    return ''.join([v[-1] for v in ship.values()])

def main():
    assert solve1(TEST_FILE) == "CMZ", "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == "MCD", "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()