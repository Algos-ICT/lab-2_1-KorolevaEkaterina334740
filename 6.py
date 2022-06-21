import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()

def Largestnumber(a):
    a.sort(reverse=True)
    num = [str(x) for x in range(9, 1, -1)]
    otvet = ''
    for k in num:
        for i in a:
            if k == str(i)[0]:
                otvet += str(i)
    return otvet


f=open('input1.txt','r')
a=open('output.txt', 'w')
vivod = int(f.readline())
numbers = list(map(int, f.readline().split()))


if 1 <= vivod <= 10**2 and min(list(map(int, numbers))) >= 1 and max(list(map(int, numbers))) < 10**3:
    a.write(str(Largestnumber(numbers)))
else:
    a.write('ошибка')

f.close()
a.close()

print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
ОШИБКА С ВЫВОДОМ ЧИСЕЛ
'''

'''

'''

'''
2
21 2
'''

'''
3
23 39 92
'''
