import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def coupons(prices):
    n = len(prices)
    arr = []
    for k in range(n + 1):
        arr.append([float('inf')] * (n + 1))
    arr[0][0] = 0
    prices.insert(0, 0)
    for i in range(1, n + 1):
        for j in range(0, n):
            if prices[i] > 100:
                arr[i][j] = min(arr[i - 1][j - 1] + prices[i], arr[i - 1][j + 1])
            else:
                arr[i][j] = min(arr[i - 1][j] + prices[i], arr[i - 1][j + 1])
    mn = min(arr[n])
    k1 = arr[n].index(mn)
    j = k1
    i = n
    k2 = 0
    days = []
    while i > 0 or j > 0:
        if prices[i] > 100:
            if arr[i - 1][j - 1] + prices[i] <= arr[i - 1][j + 1]:
                i -= 1
                j -= 1
            else:
                days.append(i)
                k2 += 1
                i -= 1
                j += 1
        else:
            if arr[i - 1][j] + prices[i] <= arr[i - 1][j + 1]:
                i -= 1
            else:
                days.append(i)
                k2 += 1
                i -= 1
                j += 1
    return mn, k1, k2, days


with open('input1.txt', 'r') as file1:
    n = int(file1.readline())
    prices = []
    for _ in range(n):
        prices.append(int(file1.readline()))

price, unused, used, days = coupons(prices)

with open('output.txt', 'w') as file2:
    file2.write(str(price) + '\n')
    file2.write(str(unused) + ' ' + str(used) + '\n')
    file2.write('\n'.join(map(str, days)))


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())


'''
Создадим функцию, в которой будем проверять стоимость обеда и, если обед стоит больше 100 рублей, добавлять купон. Далее
будем смотреть, сколько обедов и на какую сумму мы можем купить, и сколько купонов потратить. 
'''

'''
5
110
40
120
110
60
'''

'''
3
110
110
110
'''