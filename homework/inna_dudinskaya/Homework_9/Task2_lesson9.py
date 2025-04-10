temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

is_month_hot = list(filter(lambda x: True if x > 28 else False, temperatures))
print(is_month_hot)
print(max(is_month_hot))
print(min(is_month_hot))
average = sum(is_month_hot) / len(is_month_hot)
print(average)
