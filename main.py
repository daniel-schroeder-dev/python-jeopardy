"""
http://www.j-archive.com/
"""

from utils import build_game_board, parse_html

category_html, clue_html, correct_responses_html = parse_html()

correct_responses = []
for correct_response in correct_responses_html:
    res = correct_response.get('onmouseover')
    # There's gotta be a better way to do this, I'm just tired and dumb.
    correct_responses.append(res.split('em')[1].split('>')[1].split('<')[0])

categories = [category.string.extract() for category in category_html]
clues = [clue.getText() for clue in clue_html]

game_board = build_game_board(categories, clues, correct_responses)

for category, questions in game_board.items():
    print(category)
    for money, qa in questions.items():
        print(money, qa)


import pprint

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(game_board)

# I'll take Celebrity Exes for 200 Alex

print(game_board['CELEBRITY EXES'][200])
