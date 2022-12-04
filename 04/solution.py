INPUT_FILE = "04\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "04\\test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]

def isSubset(firstBe, firstEn, secondBe, secondEn):
    if(firstEn < secondBe or firstBe > secondEn): return 0
    if(firstBe <= secondBe and firstEn >= secondEn): return 1
    if(firstBe >= secondBe and firstEn <= secondEn): return 1
    return 2

def solve1(filename : str):
    total = 0
    for elves in getInput(filename): 
        firstBe, firstEn, secondBe, secondEn = list(map(int, [number for elf in elves.split(",") for number in elf.split("-")]))
        if isSubset(firstBe, firstEn, secondBe, secondEn) == 1: total += 1
    return total

def solve2(filename : str):
    total = 0
    for elves in getInput(filename): 
        firstBe, firstEn, secondBe, secondEn = list(map(int, [number for elf in elves.split(",") for number in elf.split("-")]))
        if isSubset(firstBe, firstEn, secondBe, secondEn) == 1: total += 1
        if isSubset(firstBe, firstEn, secondBe, secondEn) == 2: total += 1
    return total

def tests(bool=True):
    if not bool: return
    #print("False")
    assert isSubset(*[1,1,5,5]) == 0, "mimo1"
    assert isSubset(*[5,5,1,1]) == 0, "mimo2"
    assert isSubset(*[1,7,6,9]) == 2, "overlap1"
    assert isSubset(*[1,5,5,6]) == 2, "overlapmin"
    assert isSubset(*[3,5,1,4]) == 2, "overlap2"
    assert isSubset(*[4,6,2,4]) == 2, "overlapmin2"
    #print("True")
    assert isSubset(*[1,1,1,5]) == 1, "spodek1"
    assert isSubset(*[1,5,1,1]) == 1, "spodek2"
    assert isSubset(*[5,5,1,5]) == 1, "horek1"
    assert isSubset(*[1,5,5,5]) == 1, "horek2"
    assert isSubset(*[1,9,5,5]) == 1, "full1"
    assert isSubset(*[3,3,2,5]) == 1, "full2"

def main():
    tests()
    assert solve1(TEST_FILE) == 2, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 7, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()