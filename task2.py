numbers = list(input().split(','))
higher_number = len(numbers)
# 1, 2, 3
naturals = []
# 1, -1, 2, 0.0, 1/1, 2/1
integers = []
# 1/2, 2.1
rationals = []
# pi, sqrt(2)
reals = []
# sqrt(-1)
complexes = []
evens = []
odds = []
primes = []


def is_even(number):
    if str(number).isnumeric():
        number = int(number)
        if number % 2 == 0:
            evens.append(number)
            return


def is_odd(number):
    if str(number).isnumeric():
        number = int(number)
        if number % 2 == 1:
            odds.append(number)
            return


def is_prime(number):
    try:
        number = int(number)
        if number > 1:
            for el in range(2, number):
                if (number % el) == 0:
                    break
            else:
                primes.append(number)
    except ValueError:
        pass


def get_number(number):
    if number[0] == '-':
        number = number[1:]
    if str(number).isnumeric():
        return int(number)
    elif str(number).__contains__('.'):
        index = str(number).find('.')
        if len(number) - 1 == index:
            return int(number[:index])
        else:
            n = number[index + 1:]
            for char_after_point in n:
                if char_after_point != '0':
                    return number
            number = float(number)
            return int(number)
    elif str(num).__contains__('/'):
        index = str(number).find('/')
        left = number[:index]
        right = number[index + 1:]
        if left == right or int(left) % int(right) == 0:
            return 1
        else:
            return number


for num in numbers:
    complexes.append(num)

    if not str(num).__contains__('j'):
        reals.append(num)

    if str(num).__contains__('.') or str(num).__contains__('/'):
        rationals.append(num)

    a = get_number(num)
    if type(a) is int:
        integers.append(num)

    for i in range(1, higher_number):
        if num == str(i):
            naturals.append(num)

    is_even(num)
    is_odd(num)
    is_prime(num)

print("Naturals: " + str(naturals))
print("Integers: " + str(integers))
print("Rationals: " + str(rationals))
print("Reals: " + str(reals))
print("Complexes: " + str(complexes))
print("Evens: " + str(evens))
print("Odds: " + str(odds))
print("Primes: " + str(primes))
