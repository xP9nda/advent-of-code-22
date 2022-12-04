def p1():
    calorieList = []

    with open("input.txt", "r") as f:
        temporaryList = []
        for line in f:
            if line.strip("\n") == "":
                calorieList.append(temporaryList)
                temporaryList = []
            else:
                temporaryList.append(int(line.strip("\n")))
        calorieList.append(temporaryList)

    totals = []

    for l in calorieList:
        t = 0
        for x in l:
            t += x
        totals.append(t)

    print(totals)
    print(max(totals))
    return totals

def p2(totals):
    top3Total = 0
    for x in range(3):
        highest = max(totals)
        print(highest)
        top3Total += highest
        totals.remove(highest)

    print(top3Total)

if __name__ == "__main__":
    t = p1()
    p2(t)