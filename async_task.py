import asyncio
import aiofiles


async def write_to_file_async(file_name, content, delay):
    """Asynchronously writes data to a file after a specified delay."""
    print(f"Initiating async write to {file_name}...")

    await asyncio.sleep(delay)
    async with aiofiles.open(file_name, 'w') as file:
        await file.write('\n'.join(map(str, content)))

    print(f"Completed async write to {file_name}.")


async def execute_async_tasks(prime_numbers):
    """Handles the creation and execution of asynchronous write tasks for prime numbers."""
    file_names = ["prime1.txt", "prime2.txt", "prime3.txt"]
    tasks = []
    total_primes = len(prime_numbers)
    num_files = len(file_names)

    # Determine chunk sizes for the prime numbers
    chunk_size = total_primes // num_files
    extra_primes = total_primes % num_files

    current_index = 0
    for i in range(num_files):
        if i < extra_primes:
            chunk = prime_numbers[current_index:current_index + chunk_size + 1]
            current_index += chunk_size + 1
        else:
            chunk = prime_numbers[current_index:current_index + chunk_size]
            current_index += chunk_size

        if chunk:
            file_name = file_names[i]
            delay = 0.5
            tasks.append(write_to_file_async(file_name, chunk, delay))

    await asyncio.gather(*tasks)

    print("All asynchronous file writing tasks have been completed.")
