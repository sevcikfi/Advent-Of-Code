INPUT_FILE = "10\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "10\\test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[list[str]]:
    with open(filename, 'r') as file:
        return [line.strip().split() for line in file.read().strip().split("\n")]
#print(f'Dur:{cycle} - {regs["x"]}, TTL:{regs["TTL"]}')

def fetchInstr(instr, regs):
    if "add" in instr[0]: 
        regs["acc"] += int(instr[1])
        regs["TTL"] = 2
    if "noo" in instr[0]: regs["TTL"] = 1

def solve1(filename : str):
    program = iter(getInput(filename))
    regs = {"x": 1, "TTL": 1, "acc": 0}
    cycle = 0
    strengths: list[int] = []
    while cycle < 225:
        cycle += 1
        regs["TTL"] += -1
        if regs["TTL"] < 1:
            fetchInstr(next(program), regs)
        if cycle in [20, 60, 100, 140, 180, 220]:
            strengths.append(cycle * regs["x"])
        if regs["TTL"] == 1:
            regs["x"] += regs["acc"]
            regs["acc"] = 0
    return sum(strengths)

def solve2(filename : str):
    program = iter(getInput(filename))
    regs = {"x": 1, "TTL": 1, "acc": 0}
    cycle = 0
    row = 0
    position = -1
    display: list[str] = [""]*6
    while cycle < 240:
        cycle += 1
        position += 1
        regs["TTL"] += -1
        if regs["TTL"] < 1:
            fetchInstr(next(program), regs)
        if (regs["x"] - 1) <= position and position <= (regs["x"] + 1):
            display[row] += "#"
        else:
            display[row] += (".")
        if cycle % 40 == 0:
            row += 1
            position = -1
        if regs["TTL"] == 1:
            regs["x"] += regs["acc"]
            regs["acc"] = 0
        
    for r in display:
        print(''.join(r))
    return 2

def main():
    assert solve1(TEST_FILE) == 13140, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 2, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()