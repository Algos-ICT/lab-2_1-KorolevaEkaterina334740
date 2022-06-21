import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def InsertionSort (arr, check, w, p):
    for i in range(1, check):
        j = i-1
        while j >=0 and arr[j+1] > arr[j] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
            w[j], w[j+1] = w[j+1], w[j]
            p[j], p[j+1] = p[j+1], p[j]
            j -= 1
    return arr, w, p

def Knapsack(W, w, p):
    A = [0]*l
    V = 0
    for i in range(l):
        if W == 0:
            return V, A
        a = min(w[i], W)
        V = V + a*(p[i]/w[i])
        w[i] = w[i] - a
        A[i] = A[i] + a
        W = W - a
    return V, A

def toFixed(num, digits=0):
    return f"{num:.{digits}f}"


if __name__=='__main__':
	with open('input1.txt') as file:
		first = list(map(int, file.readline().split()))
		l = first[0]
		v = first[1]
		things = []
		weights, price = [], []
		for i in range(1, l+1):
			line = list(map(int, file.readline().split()))
			price.append(line[0])
			weights.append(line[1])
			things.append(price[i-1]/weights[i-1])

	InsertionSort(things, l, weights, price)
	v, a = Knapsack(v, weights, price)
	otvet = toFixed(v, digits=4)

	with open('output.txt', 'wt') as f:
		f.write(otvet)

print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
1. Отсортировать список предметов по их стоимости на единицу веса.
2. Добавлять в "рюкзак" самые ценные предметы, пока не достигнется максимальный вес.
'''

'''
1 10
500 30
'''

'''
3 50
60 20
100 50
120 30
'''