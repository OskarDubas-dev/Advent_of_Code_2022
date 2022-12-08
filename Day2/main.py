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


def follow_guide(string):
    # part 2
    # swap player 2 action to the one required by the guide
    p1 = string[0]
    p2 = string[2]

    if p2 == '2':
        p2 = p1
    elif p2 == '1':
        if p1 == '1':
            p2 = '3'
        elif p1 == '2':
            p2 = '1'
        elif p1 == '3':
            p2 = '2'
    elif p2 == '3':
        if p1 == '1':
            p2 = '2'
        elif p1 == '2':
            p2 = '3'
        elif p1 == '3':
            p2 = '1'
    output = f"{p1} {p2}"
    return output


strategy_guide = functions.get_data(strip=True)
strategy_guide_int = []
score = 0

for line in strategy_guide:
    newline = f"{mixer(line[0])} {mixer(line[2])}"
    strategy_guide_int.append(newline)

for i in strategy_guide_int:
    score += int(winner_check(i))
    score += int(i[2])

# What would your total score be if everything goes
# exactly according to your strategy guide?
# Part 1 answer
print(score)

#  X means you need to lose,
#  Y means you need to end the round in a draw,
#  and Z means you need to win
# Following the Elf's instructions for the second column,
# what would your total score be if everything goes
# exactly according to your strategy guide?
# Part 2 answer
score = 0
strategy_guide_int_fixed = []
for line in strategy_guide_int:
    newline = follow_guide(line)
    strategy_guide_int_fixed.append(newline)

for i in strategy_guide_int_fixed:
    score += int(winner_check(i))
    score += int(i[2])
print(score)