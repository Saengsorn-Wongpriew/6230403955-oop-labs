from functools import reduce
import sys


def main():
    n = int(sys.argv[1])
    numbers = range(n)
    numbers = map(lambda x: x + 1, numbers)
    fac = reduce(lambda x, y: x * y, numbers)
    print(f'Factorial of ({n}) is', fac)


if __name__ == "__main__":
    main()
