import time
N = 10**8

x=0
start = time.perf_counter()
for _ in range(N):
    x += 1
end = time.perf_counter()

elapsed = end - start
ops_per_sec = N / elapsed


print(f"total operations: {N:.2e}")
print(f"elapsed time: {elapsed:.3f} seconds")
print(f"operations per second: {ops_per_sec:.2fe} ops/sec")