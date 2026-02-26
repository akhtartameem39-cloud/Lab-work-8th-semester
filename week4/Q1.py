lst = [1,2,3,4,5,6,7,8,9,10]
lst_sum = sum(lst)
if len(lst) > 0:
    lst_avg = lst_sum / len(lst)
else:
    lst_avg = 0

print(f"list: {lst}")
print(f"sum: {lst_sum}")
print(f"avg: {lst_avg}")

