import multiprocessing as mp
import asyncio
import generate_numbers
import multiprocessing_task
import threading_task
import async_task


def generate_and_read_numbers(filename, count, start, end):
    """Generates numbers and reads them from a file."""
    print("Creating numbers file...")
    generate_numbers.create_random_numbers_file(
        filename, count, start, end)  # Updated function name
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]


def execute_multiprocessing(numbers):
    """Executes the multiprocessing task to find prime numbers."""
    print("Initiating multiprocessing for prime number search...")
    chunk_size = len(numbers) // mp.cpu_count()
    primes = multiprocessing_task.find_primes_in_range(numbers, chunk_size)
    print(f"Total prime numbers identified: {len(primes)}")
    return primes


def execute_threading_io():
    """Executes threading tasks for I/O simulation."""
    print("Starting threading I/O tasks...")
    threading_task.run_io_tasks()


async def execute_async_tasks(primes):
    """Executes asynchronous tasks."""
    print("Starting async I/O tasks...")
    await async_task.run_async_tasks(primes)


def main():
    # Step 1: Define parameters for generating numbers
    numbers_file = "numbers.txt"  # Define filename for the numbers
    numbers_count = 10000          # Define the number of random numbers to generate
    numbers_start = 100000         # Define the minimum value for random numbers
    numbers_end = 1000000          # Define the maximum value for random numbers

    # Step 2: Generate numbers file
    numbers = generate_and_read_numbers(
        numbers_file, numbers_count, numbers_start, numbers_end)

    # Step 3: Find primes using multiprocessing
    primes = execute_multiprocessing(numbers)

    # Step 4: Run threading tasks
    execute_threading_io()

    # Step 5: Run async tasks
    print("Running async I/O tasks...")
    asyncio.run(async_task.execute_async_tasks(primes))


if __name__ == "__main__":
    main()
