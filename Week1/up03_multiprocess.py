from time import sleep, ctime, time
import multiprocessing

def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")
 
def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")
 
def serve_customer(customer_name):
    make_coffee(customer_name)
    update_cup_number(customer_name)
 
def main():
    start = time()
    print(f"{ctime()} | === Multi-processing Coffee Machine ===")
 
    processes = [
        multiprocessing.Process(target=serve_customer, args=(customer_name,))
        for customer_name in ("A", "B", "C")
    ]
 
    for p in processes:
        p.start()
 
    for p in processes:
        p.join()
 
    elapsed = time() - start
    print(f"{ctime()} | Total time: {elapsed:.2f} seconds")

 

if __name__ == "__main__":
    main()