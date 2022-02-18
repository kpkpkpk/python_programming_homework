numbers = list(input().split(','))
higher_number = 1000
naturals = []
integers = []
rationals = []
reals = []
complexes = []
evens = []
odds = []
primes = []


def is_natural(number):
    for i in range(1, higher_number):
        if number == i:
            naturals.append(number)
            break


def is_integer(number):
    a = isinstance(number, int)
    if a:
        integers.append(number)


def is_rational(number):
    if str(number).__contains__('.') or str(number).__contains__('/'):
        rationals.append(number)


def is_real(number):
    if not str(number).__contains__('i'):
        reals.append(number)


def is_complex(number):
    if str(number).__contains__('i'):
        complexes.append(number)


def is_even(number):
    try:
        number = int(number)
        if number % 2 == 0:
            evens.append(number)
            return
    except ValueError:
        pass
    try:
        number = float(number)
        if number % 2 == 0:
            evens.append(number)
            return
    except ValueError:
        pass


def is_odd(number):
    try:
        number = int(number)
        if number % 2 == 1:
            odds.append(number)
            return
    except ValueError:
        pass
    try:
        number = float(number)
        if number % 2 == 1:
            odds.append(number)
            return
    except ValueError:
        pass


def is_prime(number):
    try:
        number = int(number)
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                primes.append(number)
    except ValueError:
        pass


for num in numbers:
    try:
        num = int(num)
    except ValueError:
        pass
    is_natural(num)
    is_integer(num)
    is_rational(num)
    is_real(num)
    is_complex(num)
    is_even(num)
    is_odd(num)
    is_prime(num)

print(naturals)
print(integers)
print(rationals)
print(reals)
print(complexes)
print(evens)
print(odds)
print(primes)
