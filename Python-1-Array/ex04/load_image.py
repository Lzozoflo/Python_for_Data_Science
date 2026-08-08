from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    SCRIPT_DIR = __file__.rsplit("/", 1)[0] if "/" in __file__ else "."
    IMAGE_PATH = f"{SCRIPT_DIR}/{path}"
    try:
        img = Image.open(IMAGE_PATH)
        ar = np.array(img)
        print(f"{np.shape(ar)}")
        return ar

    except FileNotFoundError:
        print(f"Error: Could not find image at {IMAGE_PATH}")
