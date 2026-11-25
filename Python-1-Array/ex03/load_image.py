from PIL import Image
# uv pip install Pillow
import numpy as np
#  uv pip install numpy


def ft_load(path: str) -> np.ndarray:
    SCRIPT_DIR = __file__.rsplit("/", 1)[0] if "/" in __file__ else "."
    IMAGE_PATH = f"{SCRIPT_DIR}/{path}"
    try:
        img = Image.open(IMAGE_PATH)
        ar = np.array(img)
        print(f"The shape of image is: {np.shape(ar)}")
        return ar

    except FileNotFoundError:
        print(f"Error: Could not find image at {IMAGE_PATH}")
