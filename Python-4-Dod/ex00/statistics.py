def ft_statistics(*args: any, **kwargs: any) -> None:
    for val in kwargs.values():
        if len(args) == 0:
            print("ERROR")
            continue
        lenargs = len(args)
        match val:
            case "mean":
                res = sum(args) / lenargs
                print("mean : ",res)
            case "median":
                lenargs //= 2
                alllist = list(args)
                alllist.sort()
                print("median : ", alllist[lenargs])
            case "quartile":
                alllist = list(args)
                alllist.sort()
                print(f"quartile : [{alllist[int(lenargs * 0.25)]:.1f}, {alllist[int(lenargs * 0.75)]:.1f}]")

            case "var":
                mean = sum(args) / lenargs
                squared_diffs = [(x - mean)**2 for x in args]
                variance = sum(squared_diffs) / lenargs
                print(f"var: {variance}")
                pass

            case "std":
                mean = sum(args) / lenargs
                squared_diffs = [(x - mean)**2 for x in args]
                std = (sum(squared_diffs) / lenargs) ** 0.5
                print(f"std: {std}")
                pass

            case _:
                pass
