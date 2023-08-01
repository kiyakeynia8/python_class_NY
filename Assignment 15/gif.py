import os
import imageio

IMAGES = []

for name in sorted(os.listdir("images")):
    IMAGES.append(imageio.imread("images/" + name))

imageio.mimsave("output.gif",IMAGES)