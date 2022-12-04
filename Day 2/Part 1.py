# Rock Paper Scissors

# first column is what the opponent will play
# A: Rock
# B: Paper
# C: Scissors

# the second column is what you play in response
# X: Rock
# Y: Paper
# Z: Scissors

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
    "rock": ["A", "X"],
    "paper": ["B", "Y"],
    "scissors": ["C", "Z"]
}

wins = {
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

def returnWinned(opponent, player):
    # none: draw, false: loss, true: win for player
    if opponent == player:
        return "draw"
    
    # return if player wins
    if opponent == wins[player]:
        return "win"
    return "loss"

def addScores(player, state):
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
    opponent = players[0]
    player = players[1]

    opponentPlay = returnPlayedTool(opponent)
    playerPlay = returnPlayedTool(player)

    #print(opponentPlay, playerPlay)
    wonState = returnWinned(opponentPlay, playerPlay)
    addScores(playerPlay, wonState)
    #print(playerScore)

print(playerScore)
