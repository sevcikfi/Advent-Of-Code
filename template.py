path = r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
with open(path, 'r') as file:
    raw = file.readlines()
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def solve1():
    return 1    

def solve2():
    return 2

def main():
    print("solution 1: {}".format(solve1()))
    print("solution 2: {}".format(solve2()))
    
if __name__ == "__main__":
    main()