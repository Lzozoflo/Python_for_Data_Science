import string
from sys import argv, stdin


def count_chars(text: str) -> None:
    """Count and display character categories in the given text."""
    print(f"The text contains {len(text)} characters:")
    print(f"{sum(c.isupper() for c in text)} upper letters")
    print(f"{sum(c.islower() for c in text)} lower letters")
    print(f"{sum(c in string.punctuation for c in text)} punctuation marks")
    print(f"{sum(c.isspace() for c in text)} spaces")
    print(f"{sum(c.isdigit() for c in text)} digits")


def main() -> None:
    """Parse arguments and run character counter."""
    try:
        assert len(argv) <= 2, "more than one argument is provided"
        if len(argv) == 2 and argv[1]:
            text = argv[1]
        else:
            print("What is the text to count?")
            text = stdin.read()
        count_chars(text)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

# The text contains 171 characters:
# 2 upper letters
# 121 lower letters
# 7 punctuation marks
# 26 spaces
# 15 digits
# "Python 3.0, released in 2008, was a major revision
# that is not completely backward compatible with earlier versions.
# Python 2 was discontinued with version 2.7.18 in 2020."
