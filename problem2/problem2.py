def fibonacci(max_value):
    fibonacci_values = [1, 2]
    while fibonacci_values[-1] < max_value:
        fibonacci_values.append(fibonacci_values[-1] + fibonacci_values[-2])
    fibonacci_values.pop()
    return fibonacci_values


def find_even(chain):
    result = 0
    for i in chain:
        if i % 2 == 0:
            result = result + i
    return result


print(find_even(fibonacci(4000000)))
