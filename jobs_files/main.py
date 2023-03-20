number = int(input())

count = 0
total = number
while total != 1:
    if total % 2 == 0:
        total /= 2
        count += 1
    else:
        total = total * 3 + 1
        count += 1

print(count)
