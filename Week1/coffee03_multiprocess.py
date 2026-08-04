from time import sleep, ctime, time
import multiprocessing

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน 
def make_coffee(customer_name):
    print(f"{ctime()} [Process ID: {multiprocessing.current_process().pid}] making coffee for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} [Process ID: {multiprocessing.current_process().pid}] customer {customer_name}: coffee is ready!")

def main():
    queue = ["A", "B", "C"]
    print(f"{ctime()} === Multi-processing Coffee Machine ===")
    start_time = time()

    processes = []

    for customer in queue:
        p = multiprocessing.Process(target=make_coffee, args=(customer,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    duration = time() - start_time
    print(f"{ctime()} Done! All machine ready! Total time: {duration:.2f} seconds")

# สิ่งสำคัญที่สุดสำหรับ Multi-processing ใน Python: ต้องครอบด้วยบล็อกนี้เสมอ
if __name__ == "__main__":
    main()
    