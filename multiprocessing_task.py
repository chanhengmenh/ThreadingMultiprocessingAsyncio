import multiprocessing as mp


def is_prime(number):
    """Checks if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def filter_primes(numbers_chunk):
    """Filters prime numbers from a given chunk of numbers."""
    return [num for num in numbers_chunk if is_prime(num)]


def find_primes_in_range(numbers, chunk_size):
    """Divides the numbers into chunks and finds primes using multiprocessing."""
    number_chunks = [numbers[i:i + chunk_size]
                     for i in range(0, len(numbers), chunk_size)]

    with mp.Pool() as pool:
        prime_results = pool.map(filter_primes, number_chunks)

    # Flatten the list of lists into a single list of primes
    primes = [prime for sublist in prime_results for prime in sublist]
    return primes
