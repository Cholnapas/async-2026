# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.
import asyncio

async def calculate_bill(customer, base_price):
    print(f"Calculating bill for Customer {customer}...")
    await asyncio.sleep(1)  # Simulate a long-running calculation
    total = base_price * 1.2  # Adding tax
    print(f"Total bill for Customer {customer}: ${total:.2f}")
    return final_price

async def main():

    task a = asyncio.create_task(calculate_bill("A", 50))
    task_b = asyncio.create_task(calculate_bill("B", 75))

    result_a = await task_a  # Wait for task A to complete and get the result
    result_b = await task_b  # Wait for task B to complete and get the result

    print(f"\nFinal Bill A: {result_a:.2f}")
    print(f"Final Bill B: {result_b:.2f}")
    print(f"Combined Total Revenue: ${result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())