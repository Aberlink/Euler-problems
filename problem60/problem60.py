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
            for j in range(pow(i, 2), upper_limit, i):
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


def get_first_pairs(chain):
    primes_matching_pairs = []
    for i in range(1, len(chain) >> 1):
        first = chain[i]
        for j in range(primes.index(first) + 1, len(chain)):
            second = chain[j]
            if check_primes_pair(first, second):
                primes_matching_pairs.append([first, second])
    return primes_matching_pairs


def extend_list(chain):
    results = []
    for i in range(0, len(chain)):
        temporary = chain[i].copy()
        for j in range(primes.index(temporary[-1]) + 1, len(primes)):
            third = primes[j]
            counter = 0
            for k in range(0, len(temporary)):
                if check_primes_pair(temporary[k], third):
                    counter = counter + 1
                else:
                    break
            if counter == len(temporary):
                temporary.append(third)
                if counter == 4:
                    sum_value = sum(temporary)
                    results.append(sum_value)
    return results


primes = erotosthenes_sieve(10000)
first_pairs = get_first_pairs(primes)
extended = extend_list(first_pairs)
print(extended)
