import asyncio
from time import sleep, ctime, time

def greet_diners(customers):
    print(f"{ctime()} Greeting for Customers-{customers} ...")
    sleep(1)  # Simulate a long-running task
    print(f"{ctime()} Greeting for Customers-{customers} ...Done!")

def take_orders(customers):
    print(f"{ctime()} Taking orders for Customers-{customers} ...")
    sleep(1)  # Simulate a long-running task
    print(f"{ctime()} Taking orders for Customers-{customers} ...Done!")

def do_cooking(customers):
    print(f"{ctime()} Cooking for Customers-{customers} ...")
    sleep(1)  # Simulate a long-running task
    print(f"{ctime()} Cooking for Customers-{customers} ...Done!")

def mini_bar(customers):
    print(f"{ctime()} Mini Bar for Customers-{customers} ...")
    sleep(1)  # Simulate a long-running task
    print(f"{ctime()} Mini Bar for Customers-{customers} ...Done!")

if __name__ == "__main__":
    customers = ["A", "B", "C"]

start_time = time()
for customer in customers:
    greet_diners(customer)
    take_orders(customer)
    do_cooking(customer)
    mini_bar(customer)

duration = time() - start_time
print(f"{ctime()} Finished Cooking in {duration:0.2f} seconds")