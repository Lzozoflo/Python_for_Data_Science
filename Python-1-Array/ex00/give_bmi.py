# def give_bmi(
#     height: list[int | float],
#     weight: list[int | float]
# ) -> list[int | float]:
#     return [w / (h ** 2) for h, w in zip(height, weight)]


# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#     return [value > limit for value in bmi]


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calculate BMI values from lists of heights (m) and weights (kg)."""
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Inputs must be lists.")
        if len(height) != len(weight):
            raise ValueError("Lists must have the same length.")

        bmi = []
        for h, w in zip(height, weight):
            if (
                isinstance(h, bool) or isinstance(w, bool)
                or not isinstance(h, (int, float))
                or not isinstance(w, (int, float))
            ):
                raise TypeError("Elements must be int or float.")
            if h <= 0 or w <= 0:
                raise ValueError("Height and weight must be positive.")
            bmi.append(w / (h ** 2))
        return bmi
    except Exception as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans indicating if each BMI exceeds the limit."""
    try:
        if not isinstance(bmi, list):
            raise TypeError("BMI input must be a list.")
        if isinstance(limit, bool) or not isinstance(limit, int):
            raise TypeError("Limit must be an integer.")

        res = []
        for value in bmi:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError("BMI elements must be int or float.")
            res.append(value > limit)
        return res
    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    """Main function for testing."""

    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


# Expected output:
# $> python tester.py
# [22.507863455018317, 29.0359168241966] <class 'list'>
# [False, True]

# w (kg)
# ------
# h (m)2


if __name__ == "__main__":
    main()
