

def add(n1, n2):
    return n1+n2


add(1, 2)


def add2(*args):
    # IT'S A TUPLE:
    print(args)
    sum = 0
    for n in args:
        sum += n
    return sum


print(add2(1, 2, 3, 4, 5, 6))


def calculate(n, **kwargs):
    # IT'S A DICTIONARY:
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["mult"]
    print(n)


calculate(2, add=3, mult=5)
