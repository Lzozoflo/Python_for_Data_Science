def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [value > limit for value in bmi]
