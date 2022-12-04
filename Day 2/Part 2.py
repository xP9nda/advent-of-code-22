# Rock Paper Scissors

# first column is what the opponent will play
# A: Rock
# B: Paper
# C: Scissors

# the second column is the result of the match
# X: loss
# Y: draw
# Z: win

# Winner is the player with highest score
# Score = sum of score in each round
# score per round =
# # 1: rock
# # 2: scissors
# # 3: paper
# (winning every time would be suspicious so responses must be carefully chosen)

# score per round +=
# # 0: if you lost
# # 3: if there was a draw
# # 6: if you win

playerScore = 0

tools = {
    "rock": "A",
    "paper": "B",
    "scissors": "C"
}

wins = {
    "X": "loss",
    "Y": "draw",
    "Z": "win"
}

winScenarios = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

scores = {
    "tools": {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
        },
    "wins": {
        "loss": 0,
        "draw": 3,
        "win": 6
        }
}

def returnPlayedTool(toolCode):
    for x in tools:
        if toolCode in tools[x]:
            return x

def returnWinned(winCode):
    return wins[winCode]

def returnPlayerTool(opponentTool, result):
    if result == "draw":
        return opponentTool
    if result == "loss":
        for x in winScenarios:
            if x == opponentTool:
                return winScenarios[x]
    else:
        for x in winScenarios:
            if opponentTool == winScenarios[x]:
                return x

def addScores(player, state):
    # player: players choice, state: win/loss/draw
    global playerScore
    
    for x in scores["tools"]:
        if x == player:
            playerScore += scores["tools"][x]
            break

    for x in scores["wins"]:
        if x == state:
            playerScore += scores["wins"][x]
            return

strategyGuide = []

with open("input.txt", "r") as f:
    for line in f:
        strategyGuide.append(line.strip("\n"))

for entry in strategyGuide:
    players = entry.split(" ")
    opponentCode = players[0]
    resultCode = players[1]

    opponentPlay = returnPlayedTool(opponentCode)
    result = returnWinned(resultCode)
    playerPlay = returnPlayerTool(opponentPlay, result)

    addScores(playerPlay, result)

    print("{} vs {} = {} = {}".format(opponentPlay, playerPlay, result, playerScore))
