INPUT_FILE = "07\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "07\\test.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]

# Ideally the spaghetti bellow is split into two new functions:
# 1) parsing one line in and deciding for behaviour
# 2) other executing command (= extracting "cd" behaviour)

# edit: did both in parseLine, parseCD, used in solve1_alt

# possible ways to implement Filesystem are 
# 1) Basic tree 2) @dataclass/fancier object
# 3) Pathlib simulation of real fs 4) dictionary of abs paths

def parseLine(command : str, fs : dict[str,int], cwd : str):
    cmd = command.split()
    if cmd[0].isalpha():
        if cwd == "/":
            fs[cwd+cmd[1]] = 0
        else:
            fs[cwd+"/"+cmd[1]] = 0
    if cmd[0].isdigit():
            fs[cwd] += int(cmd[0])
    if not cmd[0].isalnum(): #parsing command
        if cmd[1] == "cd":
            cwd = parseCD(cmd[2], fs, cwd)
    return cwd

def parseCD(option : str, fs : dict[str,int], cwd : str):
    if option == "..": #backtracking
        lower = cwd
        if lower == '/':
            return cwd # root dir breaks stuff
        cwd = cwd.rpartition("/")[0]
        if not cwd: # root dir breaks stuff
            cwd = "/"
        fs[cwd] += fs[lower]
    elif cwd == "/": # root dir breaks stuff
        cwd += option
    elif option == "/":
        cwd = "/" # root dir breaks stuff
    else:
        cwd += "/" + option
    return cwd

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

def solve1_alt(filename :str, fs=False):
    filesystem = {"/": 0}
    cwd = ""
    for command in getInput(filename):
        cwd = parseLine(command, filesystem, cwd)
    #cleaning back to root
    for i in range(len(cwd.split("/"))):
        if cwd == "/": break
        cwd = parseCD("..", filesystem, cwd)
    if fs: #returning FS to 2nd part
        return filesystem
    return sum([size for size in filesystem.values() if size <= 100000])

def solve2_alt(filename : str):
    filesystem = solve1(filename, True)
    return min([size for size in filesystem.values() if size > 30000000 - (70000000 - filesystem["/"])])

def main():
    assert solve1_alt(TEST_FILE) == (94853 + 584), "something is wrong xd"
    print(f"solution 1: {solve1_alt(INPUT_FILE)}")
    assert solve2_alt(TEST_FILE) == 24933642, "something is wrong 2 xd"
    print(f"solution 2: {solve2_alt(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()