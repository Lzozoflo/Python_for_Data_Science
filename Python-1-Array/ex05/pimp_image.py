import numpy as np

# • invert  : =, +, -, *
# • red     : =, *
# • green   : =, -
# • blue    : =
# • grey    : =, /

# array[lignes, colonnes, canaux]

#   Index 0 (Lignes) : Position verticale (Y)

#   Index 1 (Colonnes) : Position horizontale (X)

#   Index 2 (Canaux) : Les composantes de couleur de chaque pixel :
#       [..., 0] = Bleu (BGR) ou Rouge (RGB)
#       [..., 1] = Vert
#       [..., 2] = Rouge (BGR) ou Bleu (RGB)

def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received"""
    return 255 - array
    pass


def ft_red(array) -> np.ndarray:
    res = array * 0
    res[:,:,0] = array[:,:,0]
    return res
    pass


def ft_green(array) -> np.ndarray:
    res = array - array
    res[:,:,1] = array[:,:,1]
    return res
    pass


def ft_blue(array) -> np.ndarray:
    res = array
    res[:,:,0] = 0
    res[:,:,1] = 0    
    res[:,:,2] = array[:,:,2]
    return res
    pass


def ft_grey(array) -> np.ndarray:
    gray = array.sum(axis=2) / 3

    res = array.copy()
    res[:, :, 0] = gray
    res[:, :, 1] = gray
    res[:, :, 2] = gray
    return res

    pass

