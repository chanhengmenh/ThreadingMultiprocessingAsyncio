import random


def create_random_numbers_file(file_name, count, min_val, max_val):
    """Creates a file containing a specified number of random integers."""
    with open(file_name, "w") as file:
        random_numbers = [random.randint(min_val, max_val)
                          for _ in range(count)]
        file.write('\n'.join(map(str, random_numbers)) + '\n')

    print(f"Generated '{file_name}' with {count} random numbers.")
