def NULL_not_found(object: any) -> int:
    t = type(object)

    match t.__name__:
        case "NoneType":
            print(f"Nothing: {object} {t}")

        case "float" if object != object:
            print(f"Cheese: {object} {t}")

        case "int" if object == 0:
            print(f"Zero: {object} {t}")

        case "str" if len(object) == 0:
            print(f"Empty: {object} {t}")

        case "bool" if object is False:
            print(f"Fake: {object} {t}")
            
        case _:
            print(f"Type not Found")
            return 1

    return 0
