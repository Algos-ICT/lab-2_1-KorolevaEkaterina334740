import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()

def palindrome(string, k):
    n = len(string)
    j = -1
    x = 0
    for i in range(n//2):
        if string[i] != string[j]:
            x += 1
            if x > k:
                return False
        j -= 1
    return True

def subwords(word):
    allswords = []
    for i in range(len(word)):
        for n in range(i+1, len(word)+1):
            allswords.append(word[i:n])
    return allswords

if __name__=='__main__':
    with open('input1.txt') as file:
        ln = file.readline()
        k = int(ln.split()[-1])
        word = file.readline()

    swords = subwords(word)
    count = 0
    for word in swords:
        if palindrome(word, k):
            count += 1
    print(count)
    with open('output.txt', 'wt') as file:
        file.write(str(count))


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Runtime error :(
Создадим функцию, которая будет сравнивать слово по буквам с левого и правого концов. Также создадим вторую функцию,
в которой будет массив с хранящимися в нем подсловами. И если в ходе решения выясняется, что подслово - почти палиндром,
переменную count увеличиваем на 1.
'''

'''
5 1
abcde
'''

'''
3 3
aaa
'''