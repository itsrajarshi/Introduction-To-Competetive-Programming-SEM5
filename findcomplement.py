import time

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        mask = n
        mask |= (mask >> 1)
        mask |= (mask >> 2)
        mask |= (mask >> 4)
        mask |= (mask >> 8)
        mask |= (mask >> 16)
        return n ^ mask

n = int(input("Enter an integer: "))

start_time = time.time()
sol = Solution()
result = sol.bitwiseComplement(n)
end_time = time.time()

print("Input:", n)
print("Complement:", result)
print("Time Taken: {:.10f} seconds".format(end_time - start_time))
