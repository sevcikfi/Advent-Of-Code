INPUT_FILE = "20\\input.txt" # change the number because conda runs in root of repo
TEST_FILE =  "20\\test2.txt" # test file
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[int]:
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file.read().strip().split("\n")]

        #orgPos = file.index(instr,i-1)
        #newPos = orgPos + instr
        #moveItem = file.pop(orgPos)
        #if newPos == 0:
        #    file.append(moveItem); continue
        #if newPos > length:
        #    newPos -= length-1
        #file.insert(newPos, moveItem)
        #file = file[:newPos] + [moveItem] + file[newPos:] reinventin the wheeel

def solve1(filename : str):
    instructions = getInput(filename) imported-openssh-key-
    from collections import deque
    file = deque(instructions)
    length = len(file)
    indices = [i for i in range(length)]

    for i,instr in enumerate(instructions):
        indcc = [ii for ii, xx in enumerate(indices) if xx == i]
        test = indices.index(i)
        print(f"{indcc} - {test}")
        if len(indcc) > 1:
            print(indices)

        location_of_index = indcc[0]
        indices.pop(location_of_index)
        insert_at = (location_of_index + instr) % (length - 1)
        indices.insert(insert_at, instr)
        #----- my
        orgPos = file.index(instr)
        file.rotate(-orgPos)
        moveItem = file.popleft()
        file.rotate(-instr)
        file.appendleft(moveItem)
        newPos = (orgPos + instr) % (length - 1)
        #if newPos < 0:
        #    file.rotate(-1)
        file.rotate(newPos)

        print(f"Index: {i}, num: {instr}")
        print(f"LoI:{location_of_index} - OrgPos:{orgPos}")
        print(f"Iat:{insert_at} - NewPos:{newPos}")
        print("----")
        #print(moveItem)
        #print(newPos)
        #print(file)
    if length < 100:
        print(indices)
        print(file)
    cords = []
    for pos in [1000, 2000, 3000]:
        pos = (file.index(0) + pos)  % length
        cords.append(file[pos])
    print(cords)
    print(sum(cords))

    cords = []
    for pos in [1000, 2000, 3000]:
        pos = (indices.index(0) + pos)  % length
        cords.append(file[pos])
    print(cords)
    print(sum(cords))
    return sum(cords)

def solve2(filename : str):
    return -2

def main():
    assert solve1(TEST_FILE) == -3, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE) == 2, "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
    #FIXME: not working quite just yet!

if __name__ == "__main__":
    main()