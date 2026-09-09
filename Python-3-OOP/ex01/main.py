from S1E7 import Baratheon, Lannister

def main():
    """Start of the programme."""

    try:
        print("main")

        test = Baratheon("susso")
        print(test.is_alive)
        print(test.die())
        print(test.is_alive)

    except Exception as e:
        print(f"{type(e).__name__} : {e}")

if __name__ == '__main__':
    main()

# var = {c: "caca" for c in range(0,10)}
# print(var)