def square(x: int | float) -> int | float:
    """
    Squares a number.
    """
    return x**2


def pow(x: int | float) -> int | float:
    """
    Raises a number to the power of itself.
    """
    return x**x


def outer(x: int | float, function) -> object:
    """
    Decorator that applies a function to a number.
    """

    def inner() -> float:
        nonlocal x
        x = function(x)
        return x

    return inner


def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())


if __name__ == "__main__":
    main()
