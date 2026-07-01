# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> start cooking for Customer {ctime()}")
    await asyncio.sleep(1)  # Simulate a long-running task
    print(f"{ctime()} -> finished cooking for Customer {customer}!")

async def main():
    start_time = time()

    task_a = asyncio.create_task(cook_spaghetti("A"))

    print(f"{ctime()} -> Main program can do other things while task A runs in background.")

    await task_a  # Wait for task A to complete
    