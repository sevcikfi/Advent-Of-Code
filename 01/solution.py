
path = r"C:\Github\Advent-Of-Code\01\input.txt"
#path = r".\input.txt"
input = 0
with open(path, 'r') as file:
    raw = file.readlines()
    input = [int(x) for x in raw ]
    input
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
    
    incerases = 0
    before = input[0] + input[1] + input[2]
    next = 0

    for i in range(0, len(input)-2):
        next = input[i] + input[i+1] + input[i+2]
        if before < next:
            incerases = incerases + 1
        before = next
    print(incerases)

def main():
    solve1()
    solve2()


main()