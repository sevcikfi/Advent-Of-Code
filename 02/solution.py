#depth = [sublist for sublist in input if sublist[0] == "down" or sublist[0] == "up"]
path = r"C:\Github\Advent-Of-Code\02\input.txt"
with open(path, 'r') as file:
    input = file.readlines()
input = [x.split(' ') for x in input]

def solve1(): #triple iter could be reduced to only two
    forward = sum(list(map(int,[(f[1]) for f in input if f[0] == "forward"])))
    depths = [[sublist[0], int(sublist[1])] for sublist in input]
    depth = 0
    for x in depths:
        if(x[0] == "up"):
            depth = depth - x[1]
        if(x[0] == "down"):
            depth = depth + x[1]
    return forward * depth # 2073 * 850

def solve2():
    commands = [[sublist[0], int(sublist[1])] for sublist in input]
    horizontal, depth, aim = 0, 0, 0
    for x in commands:
        if(x[0] == "up"):
            aim = aim - x[1]
        if(x[0] == "down"): 
            aim = aim + x[1]
        if(x[0] == "forward"):
            horizontal = horizontal + x[1]
            depth = depth + aim * x[1]
    return horizontal * depth # 2073 * 895269
def main():
    print("solution 1: {}".format(solve1()))
    print("solution 2: {}".format(solve2()))
if __name__ == "__main__":
    main()