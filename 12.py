import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def func(values: list):
    sum_elem_div_two = sum(values) // 2
    first_set = list()
    second_set = list()
    for value in values:
        if (sum(first_set) + value) <= sum_elem_div_two:
            first_set.append(value)
        else:
            second_set.append(value)
    if sum(first_set) == sum(second_set) == sum_elem_div_two:
        return str(second_set.__len__()) + "\n" + second_set.__str__()
    else:
        return -1


if __name__ == '__main__':
    list_of_value = list(map(int, input().split()))
    print(func(list_of_value))


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Узнаем половину суммы всех множеств. Создадим два подмножества. В цикле for заполним их при условии, что сумма каждого 
из этих подмножеств не больше половины суммы всех подмножеств. И если в конечном итоге подмножества равны, то возвращаем
количество элементов в любом (в данном случае втором) подмножестве и номера элементов в этом подмножестве. Иначе - 
возвращаем  -1.
'''

'''
3
1 2 3
'''