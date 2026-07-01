# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} -> start serving Customer {name}")
    await asyncio.sleep(1)  # Simulate a long-running task
    print(f"{ctime()} -> finished serving Customer {name}!")

async def main():
    start_time = time()
    customers = ["A", "B", "C", "D"]
    task_list = []

    for name in customers:
        task = asyncio.create_task(serve_customer(name))
        task_list.append(t)

    for t in task_list:
        await t  # Wait for each task to complete

    print(f"Served all {len(customers)} customers in {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())