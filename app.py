import requests
import json
import random

ACCESS_TOKEN = "AWcpcVrdFgpMpQRvC07ZnA-piWSUFLFh2gy5KRRDdGN_LyBAyAAAAAA"
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
    
if __name__ == '__main__':
    assert(get_request("/v1/me/boards"))
    assert(get_board_for_user()['name'] == "Desktop Wallpapers")
