# https://www.codewars.com/kata/blackjack-scorer/
# Complete the function that determines the score of a hand in the card game Blackjack (aka 21).
#
# The function receives an array of strings that represent each card in the hand ("2", "3", ..., "10", "J", "Q",
# "K" or "A") and should return the score of the hand (integer).
#
# Scoring rules: Number cards count as their face value (2 through 10). Jack, Queen and King count as 10. An Ace can
# be counted as either 1 or 11.
#
# Return the highest score of the cards that is less than or equal to 21. If there is no score less than or equal to
# 21 return the smallest score more than 21.
#
# Examples
# ["A"]                           ==>  11
# ["A", "J"]                      ==>  21
# ["A", "10", "A"]                ==>  12
# ["5", "3", "7"]                 ==>  15
# ["5", "4", "3", "2", "A", "K"]  ==>  25


def score_hand(cards):
    total = 0
    ace_count = 0
    possible_totals = []
    values = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
              'K': 10, 'A': 11}
    for x in cards:
        total += values[x]
        if x == "A":
            ace_count += 1
    possible_totals.append(total)
    for i in range(ace_count):
        total -= 10
        possible_totals.append(total)
    # this is almost certainly overkill:
    try:
        best_total = max([t for t in possible_totals if t <= 21])
        return best_total
    except ValueError:
        best_total = min([t for t in possible_totals if t > 21])
    return best_total, possible_totals, ace_count


test_hand = ['9', '2', '10']
test_hand2 = ["A", "J"]

print(score_hand(test_hand))
