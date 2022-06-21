import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


file1=open('output.txt', 'w')
file2=open('input1.txt', 'r')
str1 = file2.readline()
if not (len(str1) >= 0 and len(str1) <= 14):
    raise ValueError
numbers = []
operators=[]
m=[]
M=[]
for i in str1:
    if i=="+" or i=="-" or i=="*":
        operators.append(i)
    else:
        numbers.append(int(i))


def minimax(i, j, m, M, operators):
    min1 = float("+inf")
    max1 = float("-inf")
    for k in range(i, j):
        if operators[k] == '*':
            a = M[i][k] * M[k + 1][j]
            b = M[i][k] * m[k + 1][j]
            c = m[i][k] * M[k + 1][j]
            d = m[i][k] * m[k+1][j]
        elif operators[k] == '+':
            a = M[i][k] + M[k + 1][j]
            b = M[i][k] + m[k + 1][j]
            c = m[i][k] + M[k + 1][j]
            d = m[i][k] + m[k + 1][j]
        else:
            a = M[i][k] - M[k + 1][j]
            b = M[i][k] - m[k + 1][j]
            c = m[i][k] - M[k + 1][j]
            d = m[i][k] - m[k + 1][j]
        min1 = min(min1, a, b, c, d)
        max1 = max(max1, a, b, c, d)
    return min1, max1


def maxvalue(numbers, operators):
    n = len(numbers)
    m = []
    M = []
    for i in range(len(numbers)):
        m.append([])
        M.append([])
        for j in range(len(numbers)):
            m[i].append(0)
            M[i].append(0)
    for i in range(n):
        m[i][i] = numbers[i]
        M[i][i] = numbers[i]
    for s in range(1, n):
        for i in range(n-s):
            j = i+s
            m[i][j], M[i][j] = minimax(i, j, m, M, operators)
    return M[0][n - 1]


sum = maxvalue(numbers, operators)
file1.write(str(sum))
file1.close()


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())


'''
В функции minimax находим минимальное и максимальное значение для каждого оператора. В функции maxvalue заполняем 
массивы m и M и ищем максимальный результат при выставлении скобок.
'''

'''
1+5
'''

'''
5-8+7*4-8+9
'''