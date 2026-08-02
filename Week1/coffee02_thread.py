from time import sleep, ctime, time
import threading

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")

def main():
    # คิวลูกค้า
    pass 

# สั่งให้โปรแกรมทำงาน
if __name__ == "__main__":
    main()    