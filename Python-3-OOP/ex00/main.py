from S1E9 import Stark

def main():
    """Start of the programme."""

    try:
        print("main")

        test = Stark("susso")
        print(test.is_alive())
        print(test.die())
        print(test.is_alive())

    except Exception as e:
        print(f"{type(e).__name__} : {e}")

if __name__ == '__main__':
    main()