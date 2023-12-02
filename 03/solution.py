INPUT_FILE = "03\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "03\\test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]

import re
def solve1(filename : str):
    raw = getInput(filename)
    digits = []
    for ln, line in enumerate(raw):
        searched = []
        for match in re.finditer(r'[^\.\d\s]', line):
            sympolPos = match.start()
            outskirt = [(ln-1, sympolPos-1), (ln-1, sympolPos), (ln-1, sympolPos+1),
                       (ln, sympolPos-1), (ln, sympolPos), (ln, sympolPos+1),
                       (ln+1, sympolPos-1), (ln+1, sympolPos), (ln+1, sympolPos+1)]
            for place in outskirt:
                number = []
                if place in searched: 
                    continue
                if raw[place[0]][place[1]] == ".":
                    searched.append((place[0],place[1]))
                    continue
                #fuck it, hardcode
                number.append((place[0],place[1]))
                if raw[place[0]][place[1]-1].isdigit():
                    print()

                if raw[place[0]][place[1]+1].isdigit():
                    print()

                i = place[0]
                for j in range(place[1]-2,place[1]-2):
                    if (i,j) in searched: continue

                    char = raw[i][j]
                    if char == ".":
                        searched.append((i,j))
                        continue

                    if char.isdigit(): 
                        number.append(raw[i][j])
                    searched.append((i,j))

            print(sympolPos)
    return 1    

def solve2(filename : str):
    return 2

def Testing(bool=True):
    if not bool: return

def main():
    assert solve1(TEST_FILE) == 4361, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 2, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()