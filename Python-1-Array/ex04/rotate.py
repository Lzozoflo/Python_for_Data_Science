import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def main():
    array = ft_load("animal.jpeg")

    if array is None:
        return

    # tableau d'origine
    print(array)

    try:
        # slice le tableau d'origine# Mettre le canal Bleu à 255
        array[100:500, 450:850, 0] = 255

        # Mettre les canaux Vert et Rouge à 0
        array[100:500, 450:850, 1:] = 0
        m = array[100:500, 450:850, 1:]
        res = [[m[j][i][0] for j in range(len(m))] for i in range(len(m[0]))]
        zoomed_array_rotate = np.array(res)
        print(f"New shape after slicing: {zoomed_array_rotate.shape}")
        print(zoomed_array_rotate)
        # matplotlib pour display depuis un array https://matplotlib.org/stable/tutorials/images.html
        plt.imshow(zoomed_array_rotate)
        plt.show()

    except Exception as e:
        print(f"Error during zoom/slicing operation: {e}")


if __name__ == "__main__":
    main()

# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12],
# ]

# for row in m:
#     print(row)

# res = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

# for row in res:
#     print(row)


# def main():
#     array = ft_load("animal.jpeg")

#     if array is None:
#         return

#     try:
#         # 1. Découpage d'une zone carrée de 400x400 en canal gris (400, 400, 1)
#         sliced = array[100:500, 450:850, 0:1]
#         print(f"The shape of image is: {sliced.shape} or {sliced.squeeze().shape}")
#         print(sliced)

#         # 2. Conversion/Aplatissement en 2D (400, 400) pour simplifier la transposition
#         h, w, _ = sliced.shape
#         transposed = np.zeros((w, h), dtype=sliced.dtype)

#         # 3. Transposition manuelle : echange des indices i et j
#         for i in range(h):
#             for j in range(w):
#                 transposed[j][i] = sliced[i][j][0]

#         print(f"New shape after Transpose: {transposed.shape}")
#         print(transposed)

#         # 4. Affichage
#         plt.imshow(transposed, cmap='gray')
#         plt.show()

#     except Exception as e:
#         print(f"Error during zoom/slicing operation: {e}")


# if __name__ == "__main__":
#     main()