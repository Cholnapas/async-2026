import asyncio
from time import sleep, ctime, time

async def greet_diners(customer):
    print(f"{ctime()} Greeting for Customers-{customer} ...")
    await asyncio.sleep(1)  # Simulate a long-running task
    print(f"{ctime()} Greeting for Customers-{customer} ...Done!")

async def customer_private_workflow(customer):
    print(f"{ctime()} [Task-{customer}] Taking Order ...")
    await asyncio.sleep(1)  # Simulate a long-running task
    print(f"{ctime()} [Task-{customer}] Taking Order ...Done!")

    print(f"{ctime()} [Task-{customer}] Cooking Spaghetti...")
    await asyncio.sleep(1)  # Simulate a long-running task
    print(f"{ctime()} [Task-{customer}] Cooking Spaghetti...Done!")

    print(f"{ctime()} [Task-{customer}] Manage Bar for Drink ...")
    await asyncio.sleep(1)  # Simulate a long-running task
    print(f"{ctime()} [Task-{customer}] Manage Bar for Drink ...Done!")
    print(f"{ctime()} [Task-{customer}] All served!\n")

async def main():
    customers = ["A", "B", "C"]
    start_time = time()

    await greet_diners("A")
    await greet_diners("B")
    await greet_diners("C")

    print(f"{ctime()} --- All customers greeted. Scheduling independent Async Tasks! ---\n")

    await asyncio.gather(*(customer_private_workflow(customer) for customer in customers))
    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in {duration:0.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())