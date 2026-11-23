from sys import argv


def filterstring(string: str, n: int) -> list[str]:
    return list(filter(lambda word: len(word) > n, string.split(' ')))


# def filterstring(text: str, n: int) -> list[str]:
#     """Return words from text whose length is strictly greater than n."""
#     is_longer = lambda word: len(word) > n  # noqa: E731
#     return [word for word in text.split(" ") if is_longer(word)]


def main() -> None:
    """Parse arguments and print filtered words."""
    try:
        assert len(argv) == 3, "the arguments are bad"
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~"
        text = ""
        n = 0
        text = argv[1]
        try:
            float(argv[1])
        except ValueError:
            try:
                n = int(argv[2])
            except ValueError:
                raise AssertionError("The arguments are bad")
            text = str(argv[1])
            if any(c in set(punctuation) for c in text):
                raise AssertionError("The arguments are bad")
        else:
            raise AssertionError("The arguments are bad")
        res = filterstring(text, n)
        print(res)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    # print(main.__doc__)
    main()

# python filterstring.py 'Hello the World'4
# ['Hello', 'World']
