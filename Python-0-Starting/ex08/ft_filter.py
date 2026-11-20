def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        for item in iterable:
            if item:
                yield item
    else:
        for item in iterable:
            if function(item):
                yield item


def main():
    """
    Description
    -----------
        Start of the programme.
    """

    try:
        # assert len(argv) == 3, "the arguments are bad"

        # print(filter.__doc__)

        # print(ft_filter.__doc__))

        # def myFunc(x):
        #     return x >= 18

        def myFunc(x):
            return x is not None and x >= 18

        ages = (5, 12, 17, None, 18, 24, 32)
        # print(f"ages {type(ages)}")

        # REAL filter
        adults = filter(myFunc, ages)
        print(f"filter {type(adults)}")

        for x in adults:
            print(f"filter {x}")
        # REAL filter

        # --------------------------------

        # MY filter
        adults = ft_filter(myFunc, ages)
        print(f"ft_filter {type(adults)}")

        for x in adults:
            print(f"ft_filter {x}")
        # MY filter

        # --------------------------------

        # REAL filter
        adults = filter(None, ages)
        print(f"filter {type(adults)}")

        for x in adults:
            print(f"filter {x}")
        # REAL filter

        # --------------------------------

        # MY filter
        adults = ft_filter(None, ages)
        print(f"ft_filter {type(adults)}")

        for x in adults:
            print(f"ft_filter {x}")
        # MY filter

    except Exception as e:
        print(f"{type(e).__name__} : {e}")


# def fibo(n):
#     n1 = 0
#     n2 = 1
#     yield n1
#     yield n2
#     while n:
#         temp = n1 + n2
#         n1 = n2
#         n2 = temp
#         n -= 1
#         yield n2

if __name__ == '__main__':
    main()
    # for c in fibo(3):
    #     print(c)
