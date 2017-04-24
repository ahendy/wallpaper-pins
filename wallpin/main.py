from pin import get_board_for_user
from pin import get_random_wallpaper_pin
from wallpaper import set_wallpaper
from wallpaper import download_wallpaper

''' 
TODO:
Package app as a GUI which runs in background task?
Only download image if it isn't already downloaded
Move image to images/ folder
Remove wget/ switch to requests (if it works)
'''

board = get_board_for_user()
pin = get_random_wallpaper_pin(board)
path = download_wallpaper(pin['image']['original']['url'])
set_wallpaper(path)

print("Setting wallpaper complete!")
