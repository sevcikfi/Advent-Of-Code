
path = r"C:\Github\Advent-Of-Code\01\input.txt"
#path = r".\input.txt"
input = []
with open(path, 'r') as file:
    raw = file.readlines()
    input = [int(x) for x in raw ]

def solve1():
    print("solution 1")
    #print(input)
    increases = 0
    temp = input[0]
    for x in input:
        if x > temp:
            increases = increases + 1
        temp = x
    print(increases)

def solve2():
    print("solution 2")
    


def main():
    solve1()
    solve2()


main()