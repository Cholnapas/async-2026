from time import sleep, ctime, time

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    sleep(1)

def main():
    # คิวลูกค้า
    make_coffee("A")

# สั่งให้โปรแกรมทำงาน
if __name__ == "__main__":
    main()
    