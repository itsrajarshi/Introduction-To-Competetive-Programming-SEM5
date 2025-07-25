import time

def multiply(a: int, b: int) -> int:
    result = 0
    is_negative = (a < 0) ^ (b < 0)
    a, b = abs(a), abs(b)

    while b > 0:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1

    return -result if is_negative else result

# 👇 Example with timing
a, b = 2, -3
start_time = time.time()
product = multiply(a, b)
end_time = time.time()

print(f"{a} * {b} = {product}")
print(f"Time taken: {end_time - start_time:.10f} seconds")
