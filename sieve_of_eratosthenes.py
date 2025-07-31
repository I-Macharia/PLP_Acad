def sieve_of_eratosthenes(n):
    """Return a list of primes up to n (inclusive). """
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False] # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
                
    return [i for i, is_prime in enumerate(sieve) if is_prime]


primes_up_to_5000000000000 = sieve_of_eratosthenes(5000000)
print("Primes up to 50:", primes_up_to_5000000000000)  # Print first 50 primes for brevity
