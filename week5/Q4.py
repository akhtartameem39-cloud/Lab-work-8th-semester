import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("1D Array:", arr)

print("\n1D Indexing:")
print("First element:", arr[0])
print("Fourth element:", arr[3])
print("Last element:", arr[-1])

print("\n1D Slicing:")
print("arr[1:5] ->", arr[1:5])
print("arr[:4]  ->", arr[:4])
print("arr[4:]  ->", arr[4:])
print("arr[::2] ->", arr[::2])
print("arr[::-1] ->", arr[::-1])

