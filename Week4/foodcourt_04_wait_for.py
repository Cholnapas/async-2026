# foodcourt_04_wait_for.py
import asyncio
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301051"
    print(f"{ctime()} | --- [Task 4] Practice using wait_for to queue multiple orders ---")

    try:
        # 1. Order a steak (takes4) Order
        print(f"{ctime()} | [System] Order sent. Monitoring 2.0s timeout limit...")

        result = await asyncio.wait_for(
            send_order_to_kitchen(MY_STUDENT_ID, "steak", "T-bone Steak"), 
            timeout=2.0
        )

        print(f"{ctime()} | Success: {result}")

    except asyncio.TimeoutError:
        print(f"{ctime()} | Timeout occured: Steak took too long! Leaving the food court now.")


if __name__ == "__main__":
    asyncio.run(main())