from time import sleep, ctime, time
import threading

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")

def main():
    # คิวลูกค้า
    queue = ["A", "B", "C"]
    print(f"{ctime()} === Multi-threading Coffee Machine ===")
    start_time = time()

    threads = []
    for customer in queue:
        t = threading.Thread(target=make_coffee, args=(customer,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time() - start_time
    print(f"{ctime()} Customer {len(queue)} coffee ready! Total time: {duration:.2f} seconds")

# สั่งให้โปรแกรมทำงาน
if __name__ == "__main__":
    main()    