from time import sleep, ctime, time

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Customer {customer_name} coffee is ready!")

def main():
    # คิวลูกค้า
    queue = ["A", "B", "C"]
    print(f"{ctime()} | === Synchronous Coffee Machine ===")
    start_time = time()

    for customer in queue:
        make_coffee(customer)

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:.2f} seconds")

# สั่งให้โปรแกรมทำงาน
if __name__ == "__main__":
    main()
    