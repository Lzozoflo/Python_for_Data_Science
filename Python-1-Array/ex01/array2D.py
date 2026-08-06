import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    lenrowfamily = len(family[0])
    for row in family:
        if len(row) != lenrowfamily:
            raise ValueError("Array 2D wasnt have a good shape.")

    ar = np.array(family)
    newar = ar[start:end]

    print(f"My shape is : {np.shape(ar)}")
    print(f"My new shape is : {np.shape(newar)}")
    return newar



family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
