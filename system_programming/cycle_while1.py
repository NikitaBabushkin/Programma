total = 100
print(total)
while total > 0:
    n = int(input())
    if n <= total:
        total -= n
        print(total)
    else:
        print('ошибка')
print('ресурс исчерпан')