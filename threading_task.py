import threading
import time


def execute_io_task(filename, delay):
    """Simulates an I/O task for a specified duration."""
    print(f"Initiating I/O task for {filename}...")
    time.sleep(delay)
    print(f"I/O task for {filename} completed.")


def run_io_tasks():
    """Creates and runs multiple I/O tasks using threads."""
    task_list = [
        ("file_1.txt", 2),
        ("file_2.txt", 3),
        ("file_3.txt", 1),
    ]

    thread_pool = []

    for filename, delay in task_list:
        thread = threading.Thread(
            target=execute_io_task, args=(filename, delay))
        thread_pool.append(thread)
        thread.start()

    for thread in thread_pool:
        thread.join()

    print("All I/O tasks have been finished.")


if __name__ == "__main__":
    run_io_tasks()
