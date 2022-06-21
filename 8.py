import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()

with open('input1.txt', 'r') as file:
    number_of_lec = int(file.readline())
    schedule = [int(i) for i in file.read().split()]

start = schedule[0::2]
end = schedule[1::2]

prev_time = 0
min_time = 0
num_of_lec_max = 0

while min_time < 1440:
    min_time = 1440
    for i in range(0, number_of_lec):
        if start[i] >= prev_time and end[i] < min_time:
            min_time = end[i]
    if min_time < 1440:
        prev_time = min_time
        num_of_lec_max += 1


with open('output.txt', 'w') as file:
    file.write(str(num_of_lec_max))


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Для этой задачи удобно использовать цикл while. Создадим два массива, в которых будут храниться время начала лекций и 
время их окончания. Далее, заядя в цикл, находим минимальное время начала из всех лекций. И если такое есть, 
а максимальное время еще не достигнуто, делаем найденное минимальное время минимальным для начала следующей лекции. 
Переменную, в которой хранится количество принятых заявок, увеличиваем на 1. 
'''

'''
1
5 10
'''

'''
3
1 5
2 3
3 4
'''