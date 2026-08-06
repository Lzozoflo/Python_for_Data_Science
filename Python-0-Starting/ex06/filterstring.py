from ft_filter import ft_filter
from sys import argv


def filterstring(string: str, n: int):
    """
    Description
    -----------
    Create a program that accepts two arguments: a string (S) and an
    integer (N).
    The program should output a list of words from S that have a length greater
    than N.

    Parameters
    ----------
        arg : str
            Description
        n : int
            Description

    Returns
    -------
        List
            A list of words from str(string) have a lenth greater than N.
    """
    return list(ft_filter(lambda word: len(word) > n, string.split(' ')))
    pass


def main():
    """
    Description
    -----------
        Start of the programme.

    Parameters
    ----------
        arg1 : str
            A String.
        arg2 : int
            Minimal lenght of a word.

    Print
    -------
        the List of words from str(arg1) have a lenth greater than N.
    """

    try:

        assert len(argv) == 3, "he arguments are bad"

        punctuation = "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~"
        arg1 = ""
        arg2 = 0

        # Le premier argument (argv[1]) doit être un string (pas un int)
        try:
            float(argv[1])
        except ValueError:
            arg1 = str(argv[1])
            if any(c in set(punctuation) for c in arg1):
                raise AssertionError("The arguments are bad")
        else:
            raise AssertionError("The arguments are bad")

        # Le second argument (argv[2]) doit être un int
        try:
            arg2 = int(argv[2])
        except ValueError:
            raise AssertionError("The arguments are bad")

        # print(arg1)
        # print(arg2)
        res = filterstring(arg1, arg2)
        print(res)

    except Exception as e:
        print(f"{type(e).__name__} : {e}")


if __name__ == '__main__':
    # print(main.__doc__)
    main()
