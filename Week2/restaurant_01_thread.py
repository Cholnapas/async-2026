import asyncio
from time import sleep, ctime, time
import threading

def greet_diners(customers):
    print(f"{ctime()} Greeting for Customers-{customers} ...")
    sleep(1)  # Simulate a long-running task
    print(f"{ctime()} Greeting for Customers-{customers} ...Done!")

def customer_private_workflow(customer):
    print(f"{ctime()} [Thread-{customer}] Taking Order ...")
    sleep(1)  # Simulate a long-running task
    print(f"{ctime()} [Thread-{customer}] Taking Order ...Done!")

    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti...")
    sleep(1)  # Simulate a long-running task
    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti...Done!")

    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drink ...")
    sleep(1)  # Simulate a long-running task
    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drink ...Done!")
    print(f"{ctime()} [Thread-{customer}] All served!\n")

if __name__ == "__main__":
    customers = ["A", "B", "C"]
    start_time = time()

# -----------------------------------------------------------------------------------------
# PHASE 1: Greeting Customers
# -----------------------------------------------------------------------------------------

for customer in customers:
    greet_diners(customer)

# -----------------------------------------------------------------------------------------
# PHASE 2: Taking Orders, Cooking Spaghetti, and Managing Bar for Drinks
# -----------------------------------------------------------------------------------------
customer_threads = []
for customer in customers:
    t = threading.Thread(target=customer_private_workflow, args=(customer,))
    customer_threads.append(t)
    t.start()

for t in customer_threads:
    t.join()

duration = time() - start_time
print(f"{ctime()} Finished Cooking in {duration:0.2f} seconds")