from sys import argv
import re


def encode_morse(text: str) -> str:
    """Encode an alphanumeric string into Morse code."""
    nested_morse = {
        " ": "/", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
        "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
        "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
        "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
        "2": "..---", "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----."
    }
    assert all(c in nested_morse for c in text.upper()), \
        "the arguments are bad"
    return " ".join(nested_morse[c] for c in text.upper())


def main() -> None:
    """Validate arguments and print Morse encoding."""
    try:
        assert len(argv) == 2 and \
                re.fullmatch(r"[A-Za-z0-9 ]*", argv[1]), "the arguments are bad"
        print(encode_morse(argv[1]))
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
