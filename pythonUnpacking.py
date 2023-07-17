# Unpacking
# 1. List unpacking
print("1. List unpacking")
numbers = [11, 22, 33]
x, y, z = numbers
print(x)  # 輸出：1
print(y)  # 輸出：2
print(z)  # 輸出：3
print()

print("2. Tuple unpacking")
# 2. Tuple unpacking
numbers = (10, 20, 30)
a, b, c = numbers
print(a)  # 輸出：1
print(b)  # 輸出：2
print(c)  # 輸出：3
print()

print("3. Unpacking specific elements")
# 3. Unpacking specific elements
numbers = [1, 2, 3, 4, 5, 6]
i, j, *k = numbers
print(i)  # 輸出：1
print(j)  # 輸出：2
print(k)  # 輸出：[3, 4, 5, 6]
