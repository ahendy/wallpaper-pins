import ctypes
import os
import wget
# from PIL import Image
# from StringIO import StringIO

SPI_SETDESKWALLPAPER = 0x14
SPIF_UPDATEINFILE = 0x1 
system_params = ctypes.windll.user32.SystemParametersInfoW
base_path = os.getcwd()

def set_wallpaper(path: str=base_path + "\zebra.jpg"):
    if base_path not in path:
        path = base_path + '/' + path

    img_path = os.path.normpath(path)
    system_params(SPI_SETDESKWALLPAPER, 0, img_path, SPIF_UPDATEINFILE)
    print(f"Set wallpaper {path.split('/')[-1]}")

def download_wallpaper(url: str):
    "download img file to local path"
    print(f"Begin download of image: {url.split('/')[-1]}")
    filename = wget.download(url)
    print("Download Complete")
    return filename

if __name__ == "__main__":
    fpath = download_wallpaper("http://www.tokkoro.com/picsup/423245-cheetah-wallpaper-for-computer.jpg")
    set_wallpaper(fpath)
