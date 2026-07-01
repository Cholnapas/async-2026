# Program 7: Dual Tasks Concurrency
# Concept: Scheduling two distinct tasks concurrently and awaiting them individually without gather.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> start cooking for Customer {customer}")
    await asyncio.sleep(1)  # Simulate a long-running task
    print(f"{ctime()} -> finished cooking for Customer {customer}!")

async def main():
    start_time = time()

    task_a = asyncio.create_task(cook_spaghetti("A"))
    task_b = asyncio.create_task(cook_spaghetti("B"))

    print(f"{ctime()} -> Main program can do other things while tasks A and B run in background.")

    await task_a  # Wait for task A to complete
    await task_b  # Wait for task B to complete

    end_time = time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())