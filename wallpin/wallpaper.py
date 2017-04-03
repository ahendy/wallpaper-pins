import ctypes
import os

img_path = os.path.normpath("C:/Users/AUSTIN/Developer/wallpaper-pins/wallpin/zebra.jpg")

SPI_SETDESKWALLPAPER = 0x14
SPIF_UPDATEINFILE = 0x1 
system_params = ctypes.windll.user32.SystemParametersInfoW
system_params(SPI_SETDESKWALLPAPER, 0, img_path, SPIF_UPDATEINFILE)


print("Ran wallpaper")