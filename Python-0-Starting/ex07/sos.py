from sys import argv
import re

morse = {
    ',': '--..--', '.': '.-.-.-', '?': '..--..', ' ': '/',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}


morse_inv = {}
for cle, valeur in morse.items():
    morse_inv[valeur] = cle


def sos(string: str, mode: int):
    """
    Description
    -----------
        Make a program that takes a string as an argument and encodes it into
        Morse Code.

        Mode 1 str to morse
        Mode 2 morse to str

    Parameters
    ----------
        param1 : type
            Description
        param2 : type
            Description

    Returns
    -------
        type
            Description
    """
    if mode == 1:
        strToMorse = [morse[c] for c in string.upper()]
         
        print(" ".join([morse[c] for c in string.upper()]))
    else:
        morseToStr = [morse_inv[c] for c in string]
        print(" ".join(morseToStr))


def main():
    """
    Description
    -----------
        Start of the programme.
            •The program supports space and alphanumeric characters.
            •An alphanumeric character is represented by dots . and dashes -.
            •Complete Morse characters are separated by a single space.
            •A space character is represented by a slash /.
    """

    try:

        # THIS

        assert len(argv) <= 2 and \
                re.fullmatch(r"[A-Za-z0-9 ]*", argv[1]), "he arguments are bad"

        sos(argv[1], 1)

        # OR

        if len(argv) != 2 or not re.fullmatch(r"[A-Za-z0-9 ]*", argv[1]):
            raise AssertionError("he arguments are bad")

        sos(argv[1], 1)


    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == '__main__':
    main()
