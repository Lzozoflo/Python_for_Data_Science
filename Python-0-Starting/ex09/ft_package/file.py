from typing import Any


def count_in_list(lst: list[Any], item: Any) -> int:
    """Return the number of occurrences of item in lst."""
    return lst.count(item)
