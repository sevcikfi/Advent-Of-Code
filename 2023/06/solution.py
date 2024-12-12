DAY = 6  # change the number because conda runs in root of repo
INPUT_FILE = f"{DAY:02d}\\input.txt" 
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = f"{DAY:02d}\\test.txt" # test file

def distance(press_t, limit_t):
    return (limit_t - press_t) * press_t

def getInput(filename: str):
    with open(filename, 'r') as file: #pre split/process input here
        times = [int(number) for number  in file.readline().split(":")[1].split()]
        distances = [int(number) for number  in file.readline().split(":")[1].split()]
        return times, distances

def number_solutions(limit, record):
    lower = math.ceil(( limit - (limit*limit - 4*record)**0.5)/2)
    upper = math.floor((limit + (limit*limit - 4*record)**0.5)/2)
    print(f"{lower}: {upper}")
    return upper - lower - 1

def solve1(filename: str): #this one doesn't work for some reason, off by 2 for odd intervals (10,20) -> (11,19)
    even = [number_solutions(limit, record) - 2 for limit, record in zip(*getInput(filename)) if limit % 2 == 0]
    odd = [number_solutions(limit, record) for limit, record in zip(*getInput(filename)) if limit % 2 != 0]
    return functools.reduce(lambda x, y: int(x*y), odd + even)

def solve2(filename: str):
    limit, record = [int("".join(list(map(str, td)))) for td in getInput(filename)]
    return number_solutions(limit, record)

import functools, math
def solve1_old(filename : str):
    permutations = []
    for limit, record in zip(*getInput(filename)):
        i = 0
        for t in range(limit//2+1):
            d = distance(t,limit)
            if d > record: i = i + 1
        if limit % 2 == 0: i = i - 0.5
        permutations.append(i*2)
    return functools.reduce(lambda x, y: int(x*y), permutations)

def solve2_old(filename : str): #second part could be made into "find number of ways func" and make both solutions much shorter
    limit, record = [int("".join(list(map(str, td)))) for td in getInput(filename)]
    r1 = lambda b,c, r=True: (- b + (b*b - 4*(-1)*c)**(1/2))/(-2) if r else (- b - (b*b - 4*(-1)*c)**(1/2))/(-2)
    return abs((math.ceil(r1(limit, -record)) - math.floor(r1(limit, -record, False)))) + 1

def Testing(bool=True):
    if not bool: return

def main():
    assert solve1(TEST_FILE) == 4*8*9, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 71503, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()