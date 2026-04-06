from multiprocessing import Process
import time
import os

def input_data():
    print(f"[PID {os.getpid()}] Input data mahasiswa...")
    time.sleep(2)
    print("Input selesai")

def hitung_ipk():
    print(f"[PID {os.getpid()}] Menghitung IPK...")
    time.sleep(3)
    print("Perhitungan selesai")

def generate_laporan():
    print(f"[PID {os.getpid()}] Membuat laporan...")
    time.sleep(1)
    print("Laporan selesai")

if __name__ == "__main__":
    print("NRP 152024208 - TASK PARALLELISM RUNNING\n")

    p1 = Process(target=input_data)
    p2 = Process(target=hitung_ipk)
    p3 = Process(target=generate_laporan)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("\nSemua proses selesai")