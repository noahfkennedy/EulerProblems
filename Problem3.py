# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def get_factors(i):
    # Runs through every single
    largest_prime = 1
    for j in range(i, 2, -1):
        if (i % j) == 0:
            if is_prime(j):
                return j
    return largest_prime


def is_prime(i):
    # Checks if a number if prime
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

print(get_factors(600851475143))