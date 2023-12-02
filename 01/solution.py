INPUT_FILE = "01\\input.txt" # change the number because conda runs in root of repo
#if above not work, use r"C:\Github\Advent-Of-Code\<Number>\input.txt" #conda things
TEST_FILE = "01\\test.txt" # test file
TEST_FILE2 = "01\\test2.txt" # test file
#input = [list(map(int, (line.strip()))) for line in raw] #Read comp for number

def getInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]

def solve1(filename : str):
    numbers: list = []
    for line in getInput(filename):
        digits = "".join([dig for dig in line if dig.isdigit()])
        numbers.append(int("".join([digits[0], digits[-1]])))

    return sum(numbers)

def solve2(filename : str):
    numbers: list = []
    """
    #parsing sux ass
    conversion = {"one": 1, "two": 2, "three": 3,
                   "four": 4, "five": 5, "six": 6,
                   "seven": 7, "eight": 8, "nine": 9}
    for raw in getInput(filename):
        digits: list[str] = []
        for i, char in enumerate(raw):
            if char.isdigit(): digits.append(char); continue
            slice = raw[i:i+5]
            for k in conversion:
                if k in slice:
                    digits.append(str(conversion[k]))
            print(digits)
    """            
    #fuck it, we ball
    for line in getInput(filename):
        line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three")
        line = line.replace("four", "four4four").replace("five", "five5five").replace("six", "six6six")
        line = line.replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")

        digits = "".join([dig for dig in line if dig.isdigit()])
        numbers.append(int("".join([digits[0], digits[-1]])))
    return sum(numbers)

def Testing(bool=True):
    if not bool: return

def main():
    assert solve1(TEST_FILE) == 142, "something is wrong xd"
    print(f"solution 1: {solve1(INPUT_FILE)}")
    assert solve2(TEST_FILE2) == (281+22), "something is wrong 2 xd"
    print(f"solution 2: {solve2(INPUT_FILE)}")
    
if __name__ == "__main__":
    main()