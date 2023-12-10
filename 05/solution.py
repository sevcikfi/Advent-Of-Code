DAY = 5  # change the number because conda runs in root of repo
INPUT_FILE = f"{DAY:02d}\\input.txt" 
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = f"{DAY:02d}\\test.txt" # test file

def getInput(filename: str):
    with open(filename, 'r') as file: #pre split/process input here
        seeds = [int(seed) for seed  in file.readline().split(":")[1].split(" ") if seed]
        mappings = [line.strip().split(":")[1].strip().split("\n") for line in file.read().strip().split("\n\n")]
        return seeds, mappings

def solve1(filename : str):
    seeds, mappings = getInput(filename)
    for conversion in mappings:
        new_seeds:list[int] = []
        to_search:list[int] = []
        for con in conversion:
            to_search.clear()
            dest, sos, lang = [int(c) for c in con.split(" ")]
            offset = dest - sos
            for seed in seeds:
                if sos <= seed and seed < sos + lang:
                    new_seeds.append(seed + offset)
                else:
                    to_search.append(seed)
            seeds = to_search.copy()
        
        seeds = to_search + new_seeds
    return min(seeds)

def solve2(filename : str):
    raw_seeds, mappings = getInput(filename)
    seeds:list[int] = []
    for i in range(0,len(raw_seeds), 2):
        new = list(range(raw_seeds[i], raw_seeds[i] + raw_seeds[i+1]))
        print(new)
        seeds.extend(new)

    print(seeds)
    for conversion in mappings:
        new_seeds:list[int] = []
        to_search:list[int] = []

        for con in conversion:
            to_search.clear()
            dest, sos, lang = [int(c) for c in con.split(" ")]
            offset = dest - sos
            for seed in seeds:
                if sos <= seed and seed < sos + lang:
                    new_seeds.append(seed + offset)
                else:
                    to_search.append(seed)
            seeds = to_search.copy()
        seeds = to_search + new_seeds
    return min(seeds)

def Testing(bool=True):
    if not bool: return

def main():
    assert solve1(TEST_FILE) == 35, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 46, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()