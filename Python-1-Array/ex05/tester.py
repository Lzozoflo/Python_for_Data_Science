from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


import matplotlib.pyplot as plt

array = ft_load("landscape.jpg")
# ar = ft_invert(array)
# ar =  ft_red(array)
# ar =  ft_green(array)
# ar = ft_blue(array)
ar = ft_grey(array)

plt.imshow(ar)
plt.show()
# print(ft_invert.__doc__)