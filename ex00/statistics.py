import numpy as np


def mean(nums):
    """
    Calculates the mean of a list of numbers.
    """
    return sum(nums) / len(nums)


def median(nums):
    """
    Calculates the median of a list of numbers.
    """
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]


def percentile(nums, p):
    """
    Calculates the percentile of a list of numbers.
    """
    n = len(nums)
    if p == 1:
        return nums[n // 4]
    else:
        return nums[n // 4 * 3]


def std(nums):
    """
    Calculates the standard deviation of a list of numbers.
    """
    return var(nums) ** 0.5


def var(nums):
    """
    Calculates the variance of a list of numbers.
    """
    return sum((x - mean(nums)) ** 2 for x in nums) / len(nums)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Prints the mean, median, quartile, standard deviation,
    and variance of a list of numbers.
    """
    nums = sorted(np.array(args))

    for kwarg in kwargs:
        if len(args) == 0:
            print("Error")
            continue
        key = kwargs[kwarg]
        if key == "mean":
            print("mean : ", mean(nums))
        elif key == "median":
            print("median : ", median(nums))
        elif key == "quartile":
            print("quartile : ", percentile(nums, 1), percentile(nums, 3))
        elif key == "std":
            print("std : ", std(nums))
        elif key == "var":
            print("var : ", var(nums))


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean")


if __name__ == "__main__":
    main()
