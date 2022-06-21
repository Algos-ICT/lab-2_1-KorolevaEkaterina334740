import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


with open('input1.txt', 'r') as file:
    destination = int(file.readline())
    distance = int(file.readline())
    number_of_stations = int(file.readline())
    gas_statinon = [int(i) for i in file.readline().split()]
    gas_statinon.insert(0, 0)
    gas_statinon.append(destination)


def min_gas(x, n, l):
     gas_refill = 0
     gas_current = 0
     while gas_current <= n:
           gas_last = gas_current
           while gas_current <= n and (x[gas_current + 1] - x[gas_last]) <= l:
                gas_current += 1
           if gas_current == gas_last:
                return -1
           if gas_current <= n:
                gas_refill += 1
     return gas_refill


with open('output.txt', 'w') as file:
    file.write(str(min_gas(gas_statinon, number_of_stations, distance)))


print(min_gas(gas_statinon, number_of_stations, distance))
print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())


'''
Создадим функцию, в которой будем проходить до города В, текущая заправка будет последней заправкой, 
и мы будем обновлять ее значение. Внутренний цикл while будет проверкой - достаточно ли этой заправки, чтобы доехать. 
Будем делать так до тех пор, пока расстояние между заправками можно преодолеть «безопасно» с нашим бензобаком. 
Если значение заправки не обновляется - добраться до пункта назначения невозможно.
'''

'''
950
400
4
200 375 550 750
'''

'''
10
3
4
1 2 5 9
'''

'''
200
250
2
100 150
'''