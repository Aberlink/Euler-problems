import itertools
import math
import random


def get_numbers_in_range(upper_limit):
    numbers = list()
    for number in range(0, upper_limit):
        numbers.append(True)
    return numbers


def erotosthenes_sieve(upper_limit):
    argument = get_numbers_in_range(upper_limit)
    temporary_primes = list()
    for i in range(2, upper_limit):
        if argument[i]:
            temporary_primes.append(i)
            for j in range(i * i, upper_limit, i):
                argument[j] = False
    return temporary_primes


def miller_rabin_test(n):
    r = 0
    d = (n - 1)
    if d % 2 == 0:
        r = r + 1
        d = d / 2
    for a in random.sample(range(2, n - 2), 4):
        x = pow(a, int(d), n)
        if (x != 1) and (x + 1 != n):
            for rr in range(1, r):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            return False
    return True


def check_primes_pair(first, second):
    temporary1 = str(first) + str(second)
    temporary2 = str(second) + str(first)
    if miller_rabin_test(int(temporary1)) and miller_rabin_test(int(temporary2)):
        return True
    else:
        return False


def extend_list(n):
    temporary = options.copy()
    options.clear()
    for i in range(primes.index(primes[n + 1]), len(primes)):
        temporary.append(primes[i])
        combinations = list(itertools.permutations(temporary, 2))
        counter = 0
        for j in range(0, len(combinations)):
            if check_primes_pair(combinations[j][0], combinations[j][1]):
                counter = counter + 1
            else:
                temporary.pop()
                break
        if counter == len(combinations):
            copy_array = temporary.copy()
            options.append(copy_array)
            temporary.pop()




#
# def find_next_in_order():
#     for i in range(0, len(primes)):
#         numbers_in_order = len(order)
#         extend_list(primes[i])
#         if len(order) != numbers_in_order:
#             break

options = [7, 1237, 2341]
primes = erotosthenes_sieve(30000)
extend_list(1)
print(options)
