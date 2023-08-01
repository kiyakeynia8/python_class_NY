import os
import shutil

cwd = os.getcwd()
a = os.listdir()
ad = cwd+"\os_image"
f = ["jpeg", "jpg", "png", "tiff", "heif", "raw", "psd", "gif"]

if "os_image" not in a:
    os.mkdir(ad)

for i in a:
    if len(i.split(".")) > 1:
        for j in f:
            if i.split(".")[1] == j:
                shutil.copy(i, ad)