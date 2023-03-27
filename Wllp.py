# Changes Wallpaper, Just mention The proper location of the image file.

import ctypes
import os
image_file = "E:\Desktop Wallpapers\jesus.jpg"
print("Setting the wallpaper")
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,  os.path.abspath(image_file) , 0)