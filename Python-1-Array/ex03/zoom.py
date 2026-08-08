import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    array = ft_load("animal.jpeg")

    if array is None:
        return

    # tableau d'origine
    print(array)

    try:
        # slice le tableau d'origine
        zoomed_array = array[100:500, 450:850, 0:1]

        print(f"New shape after slicing: {zoomed_array.shape}")
        print(zoomed_array)
        # matplotlib pour display depuis un array https://matplotlib.org/stable/tutorials/images.html
        plt.imshow(zoomed_array, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"Error during zoom/slicing operation: {e}")


if __name__ == "__main__":
    main()