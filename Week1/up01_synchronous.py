from time import sleep, ctime, time

def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")
 
def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")
 
def main():
    start = time()
    print(f"{ctime()} | === Synchronous Coffee Machine ===")
 
    for customer_name in ("A", "B", "C"):
        make_coffee(customer_name)
        update_cup_number(customer_name)
 
    elapsed = time() - start
    print(f"{ctime()} | Total time: {elapsed:.2f} seconds")
 
if __name__ == "__main__":
    main()