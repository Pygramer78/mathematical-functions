def is_prime(n, minor_primes):
    for p in minor_primes:
        # print(f'{n} and {p}')
        if n % p == 0:
            return False
    return True  # returns true or false depending if it's prime or not


def generate_primes(until):
    primes = []
    for i in range(2, until):
        if is_prime(i, primes) == True:
            primes.append(i)
    return primes


def factorial_descomposion(n):
    l = generate_primes(n)
    elements_factor_exponent = {}  # empty dict
    for c in l:
        while n % c == 0:
            if c in elements_factor_exponent:
                elements_factor_exponent[c] += 1
            else:
                elements_factor_exponent[c] = 1
    return elements_factor_exponent


def print_descom(n, mult=" * "):
    print_list = [f"{k}^{v}" for k, v in n.items()]  # WARNING! works only with dicts
    return f"{mult}".join(print_list)

def mcm(a, b):
    a, b = abs(a), abs(b)
    mcd_value = mcd(a, b)
    return abs(a * b) // mcd_value

def mcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    
    return a
