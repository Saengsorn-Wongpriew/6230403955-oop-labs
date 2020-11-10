from functools import reduce
import sys


def main():
    n = int(sys.argv[1])
    numbers = range(1, n + 1)
    print(f"With the argument as {n}, the input list is", list(numbers))
    fac_lst = list(
        map(
            lambda i: reduce(lambda x, y: x * y, range(1, i + 1)), numbers
        )
    )
    print("The factorial numbers are", fac_lst)


if __name__ == "__main__":
    main()
