from time import sleep, ctime, time, process_time
import os
import threading
import psutil


# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คนแบบซิงโครนัส
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] Making coffee for customer {customer_name}...")
    sum(i * i for i in range(1000000))
    sleep(1)
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] Customer {customer_name} Coffee is ready!")

def main():
    queue = ["A", "B", "C"]
    main_pid = os.getpid()
    main_thread_id = threading.current_thread().native_id

    print(f"{ctime()} | Main")

if __name__ == "__main__":
    main()
    