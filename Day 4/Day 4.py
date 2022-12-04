def part1():
    overlaps = 0
    pairs = []
    for line in open("input.txt", "r"):
        line = line.strip("\n")

        pair1, pair2 = line.split(",")[0], line.split(",")[1]
        
        p1start, p1end = pair1.split("-")[0], pair1.split("-")[1]
        p2start, p2end = pair2.split("-")[0], pair2.split("-")[1]

        p1range = []
        for x in range(int(p1end) - int(p1start) + 1):
            p1range.append(int(p1start) + x)
        pairs.append(p1range)

        p2range = []
        for x in range(int(p2end) - int(p2start) + 1):
            p2range.append(int(p2start) + x)
        pairs.append(p2range)

        check1, check2 = all(x in pairs[0] for x in pairs[1]), all(x in pairs[1] for x in pairs[0])
        
        if check1 or check2:
            overlaps += 1
            print("overlapping {}".format(overlaps))

        pairs = []

def part2():
    overlaps = 0
    pairs = []
    for line in open("input.txt", "r"):
        line = line.strip("\n")

        pair1, pair2 = line.split(",")[0], line.split(",")[1]
        
        p1start, p1end = pair1.split("-")[0], pair1.split("-")[1]
        p2start, p2end = pair2.split("-")[0], pair2.split("-")[1]

        p1range = []
        for x in range(int(p1end) - int(p1start) + 1):
            p1range.append(int(p1start) + x)
        pairs.append(p1range)

        p2range = []
        for x in range(int(p2end) - int(p2start) + 1):
            p2range.append(int(p2start) + x)
        pairs.append(p2range)

        check1, check2 = any(x in pairs[0] for x in pairs[1]), any(x in pairs[1] for x in pairs[0])
        
        if check1 or check2:
            overlaps += 1
            print("overlapping {}".format(overlaps))

        pairs = []

if __name__ == "__main__":
    #part1()
    part2()