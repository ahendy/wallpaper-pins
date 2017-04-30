import ctypes
import os
import wget
# from PIL import Image
# from StringIO import StringIO

SPI_SETDESKWALLPAPER = 0x14
SPIF_UPDATEINFILE = 0x1 
system_params = ctypes.windll.user32.SystemParametersInfoW
base_path = os.getcwd() + "/images/"

def set_wallpaper(path: str=base_path + "/zebra.jpg") -> None:    
    img_path = os.path.normpath(path)
    system_params(SPI_SETDESKWALLPAPER, 0, img_path, SPIF_UPDATEINFILE)
    print(f"Set wallpaper {img_path}")

def download_wallpaper(url: str) -> str: 
    "download img file to local path"
    filename = url.split('/')[-1]
    
    if "images" in os.listdir() and filename in os.listdir("images"):
        print("Image has already been downloaded")
        return base_path + filename        
    else:
        print(f"Begin download of image: {filename}")
        filepath = wget.download(url, os.path.normpath(base_path))
        print("Download Complete")
        return filepath

if __name__ == "__main__":
    fpath = download_wallpaper("http://www.tokkoro.com/picsup/423245-cheetah-wallpaper-for-computer.jpg")
    set_wallpaper(fpath)
