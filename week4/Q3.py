dict = {"ABC":65, "xyz":76, "klm":75, "pqr":79}
print(f"dictionary: {dict}")
for name, marks in dict.items():
    if marks > 75:
        print(f"{name}: {marks}")

