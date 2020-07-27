import requests
from bs4 import BeautifulSoup

def build_game_board(categories, clues, correct_responses):
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

    return game_board


def parse_html():
    r = requests.get("http://www.j-archive.com/showgame.php?game_id=6699")
    soup = BeautifulSoup(r.text, 'html.parser')

    category_html = soup.find(id="jeopardy_round").find_all("td", {"class":"category_name"})

    clue_html = soup.find(id="jeopardy_round").find_all("td", {"class": "clue_text"})

    correct_responses_html = soup.find(id="jeopardy_round").find_all(attrs={"onmouseover": True})

    return category_html, clue_html, correct_responses_html
