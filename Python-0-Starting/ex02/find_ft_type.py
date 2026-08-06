def all_thing_is_obj(object: any) -> int:
    t = type(object)

    match t.__name__:
        case "str":
            print(f"{object} is in the kitchen : {t}")
        case "int":
            print("Type not found")
        case _:
            print(f"{t.__name__.capitalize()} : {t}")
    return 42