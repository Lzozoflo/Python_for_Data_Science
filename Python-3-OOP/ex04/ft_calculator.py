class calculator:

    # @staticmethod
    # def dotproduct(v1: list[float], v2: list[float]) -> None:


    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        print([val1 + val2 for val1, val2 in zip(v1, v2)])


    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        print([val1 - val2 for val1, val2 in zip(v1, v2)])

