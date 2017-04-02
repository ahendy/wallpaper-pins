import requests
import json
import random
from auth import ACCESS_TOKEN

BASE_API = "https://api.pinterest.com"

class NoFoundWallpaperBoard(Exception):
    pass

def get_request(path: str, params: dict=None):
    "Given path retrieve the data into dictionary"
    token = {'access_token': ACCESS_TOKEN}
    if params:
        params.update(token)
    else:
        params = token
    
    url = f"{BASE_API}{path}"
    result = requests.get(url, params=params)

    return result.json()

def get_board_for_user(user_id: str="me"):
    "Return user's board which contains their wallpapers"
    boards = get_request(f"/v1/{user_id}/boards")
    wallpaper_boards = [board for board in boards['data'] if 'wallpaper' in board['name'].lower()] 

    if wallpaper_boards:
        wallpaper_board = random.choice(wallpaper_boards) 
        return wallpaper_board
    else:
        raise NoFoundWallpaperBoard("No boards containing the word 'Wallpaper' were found")

pinjection = dict(
    url="https://www.pinterest.com/pin/663788432548423423/",
    note="download free leopard wallpaper",
    link="https://www.pinterest.com/r/pin/663788432548423423/4779055074072594921/214f0b54d34475ee6852fc9f046756cc34eb5076e99c982d5dfd567210dd3491",
    id="663788432548423423",
)
def get_random_wallpaper_pin(board: dict, pin=None):
    "Given a wallpaper board retrieve a random wallpaper pin."
    pins = get_request(f"/v1/boards/{board['id']}/pins")
    return pin or random.choice(pins['data'])
    
if __name__ == '__main__':
    assert(get_request("/v1/me/boards"))
    assert(get_board_for_user()['name'] == "Desktop Wallpapers")
    assert(get_random_wallpaper_pin(get_board_for_user(), pin=pinjection) == pinjection)
    print("Tests passed.")