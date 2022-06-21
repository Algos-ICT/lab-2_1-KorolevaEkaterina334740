import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def result(amount, number, left, right, line):
    if amount[left][right] == right - left + 1:
        return 0
    elif amount[left][right] == 0:
        file2.write(line[left:right + 1])
        return 0
    elif number[left][right] == -1:
        file2.write(line[left])
        result(amount, number, left + 1, right - 1, line)
        file2.write(line[right])
        return 0
    else:
        result(amount, number, left, number[left][right], line)
        result(amount, number, number[left][right] + 1, right, line)


def bracket_sequence(line):
    d = {'(': ')', '{': '}', '[': ']'}
    n = len(line)
    amount = []
    number = []
    for _ in range(n):
        amount.append([0] * n)
        number.append([0] * n)
    for right in range(n):
        for left in range(right, -1, -1):
            if left == right:
                amount[left][right] = 1
            else:
                mn = float('inf')
                mk = -1
                if line[left] in ['(', '[', '{'] and line[right] == d[line[left]]:
                    mn = amount[left + 1][right - 1]
                for k in range(left, right):
                    if amount[left][k] + amount[k + 1][right] < mn:
                        mn = amount[left][k] + amount[k + 1][right]
                        mk = k
                amount[left][right] = mn
                number[left][right] = mk
    result(amount, number, 0, n - 1, line)


with open('input1.txt', 'r') as file1:
    s = file1.readline()

with open('output.txt', 'w') as file2:
    bracket_sequence(s)


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())


'''
ОШИБКА В ВЫВОДЕ - NONE
'''

'''
([)]
'''