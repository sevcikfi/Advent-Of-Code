DAY = 5  # change the number because conda runs in root of repo
INPUT_FILE = f"{DAY:02d}/input.txt" 
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = f"{DAY:02d}/test.txt" # test file

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

import psutil
from datetime import datetime
def solve2(filename : str):
    raw_seeds, mappings = getInput(filename)
    mins = []
    for i in range(0,len(raw_seeds), 2):
        seeds:list[int] = []
        seeds = list(range(raw_seeds[i], raw_seeds[i] + raw_seeds[i+1]))
        print(f"{i//2}: {datetime.now().strftime('%H:%M:%S')}: RAM Used: { psutil.virtual_memory()[3]/1000000000:.4f}GB, {psutil.virtual_memory()[2]}%")
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
        print(min(seeds))
        mins.append(min(seeds))

    print(mins)
    return min(mins)

def Testing(bool=True):
    if not bool: return

def main():
    assert solve1(TEST_FILE) == 35, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 46, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()