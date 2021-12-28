import queue


def find_prime_factors(number):
    arguments = queue.SimpleQueue()
    prime_factors = []
    arguments.put(number)
    number_to_check = arguments.get()
    for i in range(2, number_to_check):
        potential_divider = number_to_check % i
        if potential_divider == 0:
            arguments.put(i)
        else:
            prime_factors.append(potential_divider)
    return prime_factors


print (find_prime_factors(33))