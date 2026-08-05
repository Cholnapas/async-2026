import asyncio
import time
import httpx

# ==========================================
# 1. Configuration & Constants
# ==========================================
STUDENT_ID = "6710301051" 
BASE_URL = "http://172.16.2.177:8000"  # เปลี่ยนเป็น URL ของ API ที่ต้องการเรียกใช้งาน

# กำหนดลำดับชิ้นส่วนและหุ่นยนต์
PARTS = ["A", "B", "C"]
ROBOTS = ["robot_1", "robot_2", "robot_3"]

# ==========================================
# 2. Async Functions Development
# ==========================================


async def reset_factory(client: httpx.AsyncClient):
    """ส่ง Request เพื่อทำการ Reset สถานะของหุ่นยนต์ทั้งหมดของรหัสนักเรียนนี้"""
    # TODO: เติมโค้ดการส่ง POST request ไปยัง /student/{STUDENT_ID}/reset
    url = f"/student/{STUDENT_ID}/reset"
    resp = await client.post(url)
    print(f"Reset Factory -> {resp.status_code}")
    return resp.json()

async def grab_part(client: httpx.AsyncClient, robot_id: str, part: str):
    """สั่งให้หุ่นยนต์หยิบชิ้นส่วน 1 ชิ้น"""
    # TODO: เติมโค้ดส่ง POST request ไปยัง /student/{STUDENT_ID}/robot/{robot_id}/grab
    # พร้อมแนบ JSON Payload {"part": part}
    resp = await client.post(f"/student/{STUDENT_ID}/robot/{robot_id}/grab", json={"part": part})
    print(f"Grab Part -> {resp.status_code}")
    return resp.json()

async def run_robot_task(client: httpx.AsyncClient, robot_id: str):
    """สั่งให้หุ่นยนต์ 1 ตัว ทำการหยิบชิ้นส่วน A, B, และ C ตามลำดับ"""
    # TODO: วนลูปหยิบชิ้นส่วนใน PARTS ตามลำดับเรียงกัน (Sequential inside single robot)
    for part in PARTS:
        await grab_part(client, robot_id, part(A), part(B), part(C))
    return f"{robot_id} completed tasks."

        

async def main():
    """ฟังก์ชันหลักสำหรับเริ่มการทำงานของหุ่นยนต์ทั้ง 4 ตัวแบบ Async"""
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=10.0) as client:
        print("Resetting Factory...")
        await reset_factory(client)
        
        start_time = time.time()
        print("Starting Async Robot Operation...")
        
        # TODO: สั่งรัน run_robot_task ของหุ่นยนต์ทั้ง 4 ตัวพร้อมกันโดยใช้ asyncio.gather
        await asyncio.gather(*[run_robot_task(client, robot_id) for robot_id in ROBOTS])

        elapsed_time = time.time() - start_time
        print(f"Finished all tasks in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())