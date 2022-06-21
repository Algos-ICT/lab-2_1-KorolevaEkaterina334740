import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


with open("input1.txt") as file:
    N, M, R = map(str, file.readline().split())
    my = list(map(str, file.readline().split()))
    enemy = list(map(str, file.readline().split()))

actions = {'6': ['7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
           '7': ['8', '9', '10', 'J', 'Q', 'K', 'A'],
           '8': ['9', '10', 'J', 'Q', 'K', 'A'],
           '9': ['10', 'J', 'Q', 'K', 'A'],
           '10': ['J', 'Q', 'K', 'A'],
           'J': ['Q', 'K', 'A'],
           'Q': ['K', 'A'],
           'K': ['A'],
           'A': [None],
           'trump': ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']}

N, M = int(N), int(M)
S = []
C = []
D = []
H = []
for i in range(N):
    if my[i][1] == 'S':
        S.append(my[i][0])
    elif my[i][1] == 'C':
        C.append(my[i][0])
    elif my[i][1] == 'D':
        D.append(my[i][0])
    else:
        H.append(my[i][0])
for i in range(M):
    beaten = False
    suit = enemy[i][1]
    card = enemy[i][0]
    if suit == 'S':
        for j in actions[card]:
            if beaten == False:
                if j in S:
                    S.remove(j)
                    beaten = True
    elif suit == 'C':
        for j in actions[card]:
            if beaten == False:
                if j in C:
                    C.remove(j)
                    beaten = True
    elif suit == 'D':
        for j in actions[card]:
            if beaten == False:
                if j in D:
                    D.remove(j)
                    beaten = True
    else:
        for j in actions[card]:
            if beaten == False:
                if j in H:
                    H.remove(j)
                    beaten = True
    if beaten==False:
        if suit==R:
            with open('output.txt', 'w') as file:
                file.write('NO')
            exit()
        else:
            if R=='S':
                for j in actions['trump']:
                    if beaten == False:
                        if j in S:
                            S.remove(j)
                            beaten = True
            if R=='C':
                for j in actions['trump']:
                    if beaten == False:
                        if j in C:
                            C.remove(j)
                            beaten = True
            if R=='D':
                for j in actions['trump']:
                    if beaten == False:
                        if j in D:
                            D.remove(j)
                            beaten = True
            else:
                    for j in actions['trump']:
                        if beaten == False:
                            if j in H:
                                H.remove(j)
                                beaten = True
            if beaten==False:
                with open('output.txt', 'w') as file:
                    file.write('NO')
                exit()
with open('output.txt', 'w') as file:
    file.write('YES')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Runtime error:(
Создадим словарь, в котором укажем, какие карты (значения) какую могут крыть (ключ). Далее, создадим 4 массива, 
соответствующие 4 мастям в колоде карт. В цикле for проверяем, можем ли мы отбить карту. Если нет, выводим в ответ False,
если да - Yes.
'''

'''
6 2 C
KD KC AD 7C AH 9C
6D 6C
'''

'''
4 1 D
9S KC AH 7D
8D
'''