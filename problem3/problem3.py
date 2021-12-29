import math
import queue
import random


def find_prime_factors(number):
    arguments = queue.SimpleQueue()
    prime_factors = dict()
    arguments.put(number)
    while not arguments.empty():
        number_to_check = arguments.get()
        for i in range(2, int(math.sqrt(number_to_check)) + 1):
            if number_to_check % i == 0:
                divider = number_to_check // i
                if miller_rabin_test(i):
                    prime_factors[i] = prime_factors.get(i, 0) + 1
                else:
                    arguments.put(i)
                if miller_rabin_test(divider):
                    prime_factors[divider] = prime_factors.get(divider, 0) + 1
                else:
                    arguments.put(divider)
                break

    return prime_factors


def miller_rabin_test(n):
    if n == 2 or n == 3 or n == 5:
        return True
    elif n <= 1 or n == 4:
        return False
    else:
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


print(find_prime_factors(333))
print(max(find_prime_factors(600851475143)))
