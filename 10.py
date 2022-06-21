import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


with open('input1.txt') as file:
    n, s = map(int, file.readline().split())
    apples = []

    for i in range(n):
        a, b = map(int, file.readline().split())
        apples.append([a, b, i + 1])
    apples.sort(key=lambda a: [-(a[1] - a[0]), a[0]])
    j = 0
    truth = True
    order = []
    while truth and j < n:
        found = False
        a = 0
        while a < n and not found:
            if s - apples[a][0] > 0 and apples[a][2] != 0:
                found = True
                s += apples[a][1] - apples[a] [0]
                order.append(apples[a][2])
                apples[a][2] = 0
            a += 1
        truth = found
        j += 1
    if truth:
        print(*order)
    else:
        print(-1)


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Для этой задачи создадим массив apples, отсортируем его с помощью лямбда функции. С помощью цикла while будем смотреть, 
можно ли Алисе съесть яблоки так, чтобы ее рост не стал равным 0. Если можно, выводим порядок номеров яблок. Если нет,
пишем -1.
'''

'''
3 5
2 3
10 5
5 10
'''

'''
3 5
2 3
10 5
5 6
'''