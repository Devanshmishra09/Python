def sum_and_average(lst):
    total = sum(lst)
    average = total / len(lst)
    return total, average

print(sum_and_average([1, 2, 3, 4, 5]))