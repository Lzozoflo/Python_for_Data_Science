from load_image import ft_load
from pathlib import Path
from PIL import Image
import numpy as np


ar = ft_load("animal.jpeg")

print(np.shape(ar))
print(ar[400:400:1])