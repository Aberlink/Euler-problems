def find_pythagorean_triplet(sum_value):
    for c in range(sum_value - 3, 3, -1):
        a = 1
        b = 1000 - a - c
        while a < b:
            arms = pow(a, 2) + pow(b, 2)
            hypotenuse = pow(c, 2)
            if arms == hypotenuse:
                return [a, b, c, a * b * c]
            else:
                a = a + 1
                b = b - 1
    return 'triplet not found'


print(find_pythagorean_triplet(1000))



