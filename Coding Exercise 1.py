"""
Task: In this problem, we've provided you with a set of lottery numbers:

lottery_numbers = {13, 21, 22, 5, 8}
You must define a list of two players, each with a name and another set of numbers.

Players in your list should be dictionaries following this format:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}
Printing out their luck

Then for each player, print out a nice string that contains their name and how many numbers they got right (as we've done before, you can intersect their numbers with the lottery_numbers  variable provided). You'll then need to calculate the length of the resulting set to get how many numbers they got right.

This string doesn't have to have a particular format, it just must include both the name and how many numbers they got right.
"""

lottery_numbers = {13, 21, 22, 5, 8}

players  = [
  {
    'name': 'Messi',
    'numbers': {5,8,4,13}
  },
  {
    'name': 'ronaldo',
    'numbers': {21,7,5,22}
  },
]
player1 = len(players[0]['numbers'].intersection(lottery_numbers))

player2 = len(players[1]['numbers'].intersection(lottery_numbers))

print(f"{players[0]['name']} has got {player1} right numbers")
print(f"{players[1]['name']} has got {player2} right numbers")
