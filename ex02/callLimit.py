def callLimit(limit: int):
    """
    Decorator that limits the number of calls to a function.
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            try:
                nonlocal count
                if count < limit:
                    count += 1
                    return function(*args, **kwds)
                else:
                    raise AssertionError(
                        f"Error: {function} called too many times"
                    )
            except Exception as e:
                print(e)

        return limit_function

    return callLimiter


def main():

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
