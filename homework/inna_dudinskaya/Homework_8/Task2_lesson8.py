def progression(limit):
    f0 = 0
    f1 = 1
    count1 = 1
    while count1 < limit:
        if count1 == 1:
            count1 += 1
            yield f0
        elif count1 == 2:
            count1 += 1
            yield f1
        else:
            sum = f0 + f1
            f0 = f1
            f1 = sum
            count1 += 1
            yield sum


count = 1
for number in progression(10000001):
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
        break
    count += 1
