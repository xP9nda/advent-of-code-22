import string
chars = string.ascii_lowercase + string.ascii_uppercase

def part1():
    shared = []
    totalPriority = 0
    
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip("\n")
            compA = slice(0, len(line)//2)
            compB = slice(len(line)//2, len(line))
            A, B = line[compA], line[compB]
            for letter in A:
                if letter in B and letter not in shared:
                    shared.append(letter)

            for letter in shared:
                priority = chars.find(letter) + 1
                totalPriority += priority

            shared = []
    print(totalPriority)

def part2():
    totalPriority = 0
    shared = []

    with open("input.txt", "r") as f:
        index = 0
        lines = []
        for line in f:
            line = line.strip("\n")
                
            index += 1
            lines.append(line)

            if index == 3:
                for letter in lines[0]:
                    if letter in lines[1] and letter in lines[2]:
                        if letter not in shared:
                            shared.append(letter)
                            priority = chars.find(letter) + 1
                            totalPriority += priority
                index = 0
                lines = []
                shared = []
    print(totalPriority)

if __name__ == "__main__":
    part2()
