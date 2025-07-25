x = 5
y = 3

print("Before swapping: x =", x, "y =", y)

x = x ^ y
y = x ^ y
x = x ^ y

print("After swapping: x =", x, "y =", y)
