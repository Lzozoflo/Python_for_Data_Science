from sys import argv

def main():
    """
    Description
    -----------
        Start of the programme.
    """

    try:
        # assert len(argv) == 3, "the arguments are bad"

         print(filter.__doc__)
        
    except Exception as e:
        print(f"{type(e).__name__} : {e}")

if __name__ == '__main__':
    main()