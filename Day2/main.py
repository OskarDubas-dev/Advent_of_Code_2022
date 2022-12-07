import functions


# A = rock B = paper C = scissors
# X = rock Y = paper Z = scissors

# score: shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors
#        outcome of the round
#        (0 if you lost, 3 if the round was a draw, and 6 if you won)


def mixer(string):
    # bad name but ok
    # it swap rock paper scissors to 1 2 3, so it's easier to find winner
    if string == 'A' or string == 'X':
        return 1
    elif string == 'B' or string == 'Y':
        return 2
    else:
        return 3


def winner_check(string):
    # check points for player 2
    p1 = string[0]
    p2 = string[2]

    if p1 == p2:
        return 3
    elif p1 == '1' and p2 == '2':
        return 6
    elif p1 == '2' and p2 == '3':
        return 6
    elif p1 == '3' and p2 == '1':
        return 6
    else:
        return 0


strategy_guide = functions.get_data()
strategy_guide_stripped = [s.strip() for s in strategy_guide]
strategy_guide_int = []
score = 0

for line in strategy_guide_stripped:
    newline = f"{mixer(line[0])} {mixer(line[2])}"
    strategy_guide_int.append(newline)

for i in strategy_guide_int:
    score += int(winner_check(i))
    score += int(i[2])

# What would your total score be if everything goes
# exactly according to your strategy guide?
# Part 1 answer
print(score)