import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def func(x: list):
    if sum(x) % 3 == 0:
        tmp = sum(x) / 3
        x.sort()
        x.reverse()
        elems = list()
        for i in range(3):
            subelements = []
            j = 0
            while (sum(subelements) != tmp):
                if j >= len(x):
                    return 0
                if ((sum(subelements) + x[j]) <= tmp):
                    subelements.append(x[j])
                    del (x[j])
                else:
                    j += 1
            print(subelements)
            elems.append(subelements)
        return int(sum(elems[0]) == sum(elems[1]) == sum(elems[2]))
    else:
        return 0


if __name__ == '__main__':
    print(func([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]))


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())


'''
Создадим функцию, в которой будем проверять, можно ли разделить сувениры на троих. Сначала проверим, делится ли сумма
на три в принципе. Если нет, возвращаем 0. Если да, то в цикле for разбиваем множество сувениров на три подмножества, 
равных по сумме. 
'''

'''
1
40
'''

'''
4
3 3 3 3
'''

'''
11
17 59 34 57 17 23 67 1 18 2 59
'''

'''
13
1 2 3 4 5 5 7 7 8 10 12 19 25
'''