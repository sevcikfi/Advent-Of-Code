path = r"C:\Github\Advent-Of-Code\03\input.txt" #conda things
with open(path, 'r') as file:
    raw = file.readlines()
input = [list(map(int, (line.strip()))) for line in raw]
bitsize = len(input[0])

def solve1():
    max = [0] * bitsize
    for line in input:
        for i in range(bitsize):
            if line[i] == 0:
                max[i] += 1
            else:
                max[i] = max[i] - 1
    gamma = ""
    eps = ""
    for i in range(len(max)):
        if(max[i] > 0):
            gamma = gamma + "1"
            eps = eps + "0"
        else:
            gamma = gamma + "0"
            eps = eps + "1"
    return int(gamma,2) * int(eps,2)

def solve2():
    oxyNums = input 
    co2Nums = input
    for i in range(bitsize):
        oxyMost = int(sum([line[i] for line in oxyNums]) >= len(oxyNums)/2)
        co2Least = int(sum([line[i] for line in co2Nums]) < len(co2Nums)/2)
        if(len(oxyNums) > 1):
            oxyNums = [number for number in oxyNums if number[i] == oxyMost]
        if(len(co2Nums) > 1):
            co2Nums = [number for number in co2Nums if number[i] == co2Least]
    return int("".join([str(b) for b in oxyNums[0]]), 2) * int("".join([str(b) for b in co2Nums[0]]), 2)

def main():
    print("solution 1: {}".format(solve1()))
    print("solution 2: {}".format(solve2()))
if __name__ == "__main__":
    main()