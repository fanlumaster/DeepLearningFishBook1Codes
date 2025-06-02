import matplotlib.pyplot as plt
from matplotlib.image import imread
import os.path


lena_png_path = os.path.join(os.path.dirname(__file__), "images", "lena.png")
print(lena_png_path)

img = imread(lena_png_path)
plt.imshow(img)
plt.show()