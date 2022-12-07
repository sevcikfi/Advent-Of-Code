INPUT_FILE = "07\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "07\\test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]


def parseCommand(command : str):
    return 0

def solve1(filename : str, fs=False):
    filesystem = {"/": 0}
    cwd = ""
    for command in getInput(filename):
        command = command.split()
        #listing stuff
        if command[0].isalpha():
            if cwd == "/":
                filesystem[cwd+command[1]] = 0
                continue
            filesystem[cwd+"/"+command[1]] = 0
            continue
        if command[0].isdigit():
            filesystem[cwd] += int(command[0])
            continue
        if not command[0].isalnum(): #parsing command
            if command[1] == "ls":
                continue
            if command[1] == "cd": #parsing cd
                if command[2] == "..": #backtracking
                    lower = cwd
                    if lower == '/':
                        break # root dir breaks stuff
                    cwd = cwd.rpartition("/")[0]
                    if not cwd: # root dir breaks stuff
                        cwd = "/"
                    filesystem[cwd] += filesystem[lower]
                elif cwd == "/": # root dir breaks stuff
                    cwd += command[2]
                elif command[2] == "/":
                    cwd = "/" # root dir breaks stuff
                else:
                    cwd += "/" + command[2]
    #cleaning back to root
    for i in range(len(cwd.split("/"))):
        lower = cwd
        if lower == '/':
            break
        cwd = cwd.rpartition("/")[0]
        if not cwd:
            cwd = "/"
        filesystem[cwd] += filesystem[lower]
        continue
    if fs: #returning FS to 2nd part
        return filesystem
    return sum([size for size in filesystem.values() if size <= 100000])

def solve2(filename : str):
    filesystem = solve1(filename, True)
    delete = 30000000 - (70000000 - filesystem["/"])
    dirs = [size for size in filesystem.values() if size > delete]
    return min(dirs)

def main():
    assert solve1(TEST_FILE) == (94853 + 584), "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 24933642, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()