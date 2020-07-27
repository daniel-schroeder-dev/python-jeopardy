"""
http://www.j-archive.com/
"""

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.j-archive.com/showgame.php?game_id=6699")

soup = BeautifulSoup(r.text, 'html.parser')

category_html = soup.find(id="jeopardy_round").find_all("td", {"class":"category_name"})

clue_html = soup.find(id="jeopardy_round").find_all("td", {"class": "clue_text"})

correct_responses_html = soup.find(id="jeopardy_round").find_all(attrs={"onmouseover": True})

correct_responses = []
for correct_response in correct_responses_html:
    res = correct_response.get('onmouseover')
    correct_responses.append(res.split('em')[1].split('>')[1].split('<')[0])


categories = [category.string.extract() for category in category_html]
clues = [clue.getText() for clue in clue_html]

game_board = {}

clue_index = 0
for row, money in zip(range(5), range(200, 1200, 200)):
    for column in range(6):
        if not game_board.get(categories[column]):
            game_board[categories[column]] = []
        
        game_board[categories[column]].append({
            money: (clues[clue_index], correct_responses[clue_index])
        })
        clue_index += 1


for category, questions in game_board.items():
    print(category)
    for question in questions:
        for money, qa in question.items():
            print(money, qa)





# categories = [
#     "Hello, World",
#     "Name That Tune",
#     "Bookworm",
# ]

# questions = {
#     "Hello, World": [
#         ("Released in 1972, this programming language has a single-letter name and is the basis for many other languages such as Java, Python, and JavaScript.", "C"),
#         ("One of the most popular languages on the planet, this langauge's name pays hommage to a favorite programmer beverage.", "Java"),
#     ],
#     "Name That Tune": [
#         ()
#     ],
#     "Bookworm": [

#     ],
# }

# for category in categories:
#     for amount in range(200, 1200, 200):
#         print(amount, category)

# if __name__ == "__main__":
#     pass
