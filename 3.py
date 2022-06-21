import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def f(first_list: list, second_list: list):
    sum = 0
    first_list.sort()
    second_list.sort()
    for i in range(len(first_list)):
        sum += first_list[i] * second_list[i]
    return sum


if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f(a, b))

print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())


'''
Создадим функцию, которая будет отдельно сортировать прибыль за клик и количество кликов. Далее будем последовательно 
умножать значение прибыли на колиечество кликов и добавлять полученное произведение в переменную sum.
'''

'''
1
23
39
'''

'''
3
1 3 -5
-2 4 1
'''
