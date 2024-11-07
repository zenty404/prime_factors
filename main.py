def prime_factors(n, div=2):
    # Condition d'arrêt : Si n = 1, on a fini la factorisation
    if n == 1:

        return []

    # Si n est divisible par le diviseur actuel
    if n % div == 0:

        return [div] + prime_factors(n // div, div)

    # Sinon on augmente le diviseur et continue la récursion
    return prime_factors(n, div + 1)

print(prime_factors(60))