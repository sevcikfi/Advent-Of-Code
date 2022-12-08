INPUT_FILE = "08\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "08\\test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[list[int]]:
    with open(filename, 'r') as file:
        return [[int(tree) for tree in line] for line in file.read().strip().split("\n")]

def isVisible(forest: list[list[int]], y : int, x : int):
    rr, lr, hc, lc = True, True, True, True
    for rrow in [tree for tree in forest[y][x-1::-1]]:
        if rrow >= forest[y][x]:
            rr = False; break
    for lrow in [tree for tree in forest[y][x+1:]]:
        if lrow >= forest[y][x]:
            lr = False; break
    for hiColumn in [line[x] for line in forest[y-1::-1]]:
        if hiColumn >= forest[y][x]:
            hc = False; break
    for loColumn in [line[x] for line in forest[y+1:]]:
        if loColumn >= forest[y][x]:
            lc = False; break
    return int(rr or lr or hc or lc)

def solve1(filename : str):
    forest = getInput(filename)
    total = 0
    for irow, row in enumerate(forest):
        for icolumn in range(len(row)):
            if icolumn == 0 or irow == 0 or (icolumn == len(row)-1) or (irow == len(row)-1): 
                total += 1
            else:
                total += isVisible(forest, irow, icolumn)
    return total

def scenicScore(forest, y : int, x : int):
    from itertools import takewhile
    rr, lr, hc, lc = 0, 0, 0, 0
    for rrow in [tree for tree in forest[y][x-1::-1]]:
        rr += 1
        if rrow >= forest[y][x]: break
    for lrow in [tree for tree in forest[y][x+1:]]:
        lr += 1
        if lrow >= forest[y][x]: break
    for hiColumn in [line[x] for line in forest[y-1::-1]]:
        hc += 1
        if hiColumn >= forest[y][x]: break
    for loColumn in [line[x] for line in forest[y+1:]]:
        lc += 1
        if loColumn >= forest[y][x]: break
    return rr * lr * hc * lc

def solve2(filename : str):
    forest = getInput(filename)
    totals = []
    for irow, row in enumerate(forest):
        for icolumn in range(len(row)):
            if icolumn == 0 or irow == 0 or (icolumn == len(row)-1) or (irow == len(row)-1): 
                continue
            totals.append(scenicScore(forest, irow, icolumn))
    return max(totals)

def main():
    assert solve1(TEST_FILE) == 21, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 8, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    exit()
    #testing snipets
    rrow = [tree for tree in forest[y][x-1::-1]]
    lrow = [tree for tree in forest[y][x+1:]]
    hiColumn = [tree for line in forest[y-1::-1] for tree in line[x]]
    loColumn = [tree for line in forest[y+1:] for tree in line[x]]
    print(f"{irow},{icolumn}")
    if forest[y][x] == "4":
        print(f"{forest[y][x]} - {y},{x}")
        print(rrow)
        print(rr)
        print(lrow)
        print(lr)
        print(hiColumn)
        print(hc)
        print(loColumn)
        print(lc)
        print(final)

if __name__ == "__main__":
    main()