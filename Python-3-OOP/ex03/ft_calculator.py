class calculator:

    def __init__(this, li: list):
        this.li = li

    def __add__(this, object) -> None:
        this.li = [nb + object for nb in this.li]
        print(this.li)

    def __mul__(this, object) -> None:
        this.li = [nb * object for nb in this.li]
        print(this.li)
        pass

    def __sub__(this, object) -> None:
        this.li = [nb - object for nb in this.li]
        print(this.li)
        pass

    def __truediv__(this, object) -> None:
        if object == 0:
            return
        this.li = [nb / object for nb in this.li]
        print(this.li)
        pass
