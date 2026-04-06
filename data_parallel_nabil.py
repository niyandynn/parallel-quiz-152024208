from multiprocessing import Pool
import os

def scale_nilai(nilai):
    pid = os.getpid()
    hasil = nilai * 1.1
    print(f"[PID {pid}] memproses nilai {nilai} -> {hasil}")
    return round(hasil, 2)

if __name__ == "__main__":
    data_nilai = [65, 70, 75, 80, 85, 90, 95]

    print("NRP 152024208 - DATA PARALLELISM RUNNING\n")

    with Pool(processes=3) as worker:
        output = worker.map(scale_nilai, data_nilai)

    print("\nHasil akhir:", output)