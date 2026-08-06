from sys import argv

# print(sys.version)


def main():
    """
    Description
    -----------
    This time you have to make a real autonomous program, with a main,
    which takes a single string argument and displays the sums of its
    upper-case characters, lower-case characters, punctuation characters,
    digits, and spaces
    •If none or nothing is provided, the user is prompted to provide a string.
    •If more than one argument is provided to the program, print an
    AssertionError.

    """
    try:
        assert len(argv) <= 2, "more than one argument is provided"

        punctuation = "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~"
        str = argv[1]

        print(f"The text contains {len(str)} characters:")
        print(f"{sum(int(c.isupper()) for c in str)} upper letters")
        print(f"{sum(int(c.islower()) for c in str)} lower letters")
        # print(f"{len([c for c in str if c.islower()])} lower letters")
        # print(f"{sum(1 for let in str if let.islower())} lower letters")
        print(f"{sum(c in set(punctuation) for c in str)} punctuation marks")
        print(f"{sum(int(c.isspace()) for c in str)} spaces")
        print(f"{sum(int(c.isdigit()) for c in str)} digits")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == '__main__':
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
