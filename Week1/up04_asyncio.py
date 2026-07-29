import asyncio
from time import ctime, time

async def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

async def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")

async def serve_customer(customer_name):
    await make_coffee(customer_name)
    await update_cup_number(customer_name)

async def main():
    start = time()
    print(f"{ctime()} | === Asyncio Coffee Machine ===")
 
    await asyncio.gather(
        *(serve_customer(customer_name) for customer_name in ("A", "B", "C"))
    )
 
    elapsed = time() - start
    print(f"{ctime()} | Total time: {elapsed:.2f} seconds")
 
if __name__ == "__main__":
    asyncio.run(main())