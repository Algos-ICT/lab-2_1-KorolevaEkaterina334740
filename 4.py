import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


with open('input1.txt', 'r') as file:
    n=int(file.readline())
    array=[]
    for i in range(n):
         array.append([int(i) for i in file.readline().split()])
array.sort(key = lambda x: x[1])
votes=[]
while len(array)>0:
     vote=array[0][1]
     votes.append(vote)
     array.pop(0)
     i=0
     while i<len(array):
           if array[i][0] <= vote:
                array.pop(i)
           else:
                i+=1
print(votes)
print(len(votes))
print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Мы сортируем массив с помощью встроенной функции,  которая вернет тот элемент, чьё второе значение [1] больше. Далее мы
уложим в «голоса» промежутки, считанные из файла и в конце сравним значения списка «голосов» с соответствующим значением
промежутка, и, если значение промежутка окажется меньше - то удалим уго (в противном случае увеличим i, чтобы продолжить
сравнивать)
'''

'''
3
1 3
2 5
3 6
'''

'''
4
4 7
1 3
2 5
5 6
'''