from sys import argv

# print(sys.version)

def EvenOdd(arg):
    if arg % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    try:
        assert len(argv) <= 2, "more than one argument is provided"

        for arg in argv[1:]:
            try:
                EvenOdd(int(arg))
            except ValueError as e:
                raise AssertionError("argument is not an integer")
        
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

main()


# if __name__ == '__main__':
#     main()



# > python whatis.py 14
# I'm Even.
# $>

# $> python whatis.py -5
# I'm Odd.
# $>

# $> python whatis.py
# $>

# $> python whatis.py 0
# I'm Even.
# $>

# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>

# $> python whatis.py 13 5
# AssertionError: more than one argument is provided
# $>