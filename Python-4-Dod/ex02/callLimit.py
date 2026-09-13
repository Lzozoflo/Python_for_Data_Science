def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count == limit:
                def errorp():
                    print(f"Error: {function} called too many times")
                return errorp()
            count += 1
            return function()
        return limit_function
    return callLimiter