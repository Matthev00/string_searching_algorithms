import sys
import time
import gc
import random
import matplotlib.pyplot as plt
#from naive import .... as naive_search
from kmp import kmp_search
from KR import searchKR


def read():
    with open('pan-tadeusz-unix.txt') as filehandle:
        words = []
        for line in filehandle:
            line_words = line.split(' ')
            for word in line_words:
                if '\n' in word:
                    word = word[:-1]
                if word != '':
                    words.append(word)
    return words


def plot(n, naive_times, kmp_times, kr_times):
    plt.plot(n, naive_times, color='r', label='Naive search',
             marker='o')
    plt.plot(n, kmp_times, color='g', label='KMP search',
             marker='o')
    plt.plot(n, kr_times, color='b', label='KR search',
             marker='o')
    plt.xlabel("Number of words")
    plt.ylabel("Time in sec")
    plt.title("Search algorithms time comparison")
    plt.legend()
    plt.savefig('wykres.png')


def naive_search_time_measure(words, text):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for word in words:
        naive_search(word, text)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def kmp_search_time_measure(words, text):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for word in words:
        kmp_search(word, text)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def kr_search_time_measure(words, text):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for word in words:
        searchKR(word, text)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


N = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

def main():
    naive_times = []
    kmp_times = []
    kr_times = []
    split_text = read()
    with open('pan-tadeusz-unix.txt') as filehandle:
        text = filehandle.read()
    for n in N:
        #naive_times.append(naive_search_time_measure(split_text[:n], text))
        kmp_times.append(kmp_search_time_measure(split_text[:n], text))
        kr_times.append(kr_search_time_measure(split_text[:n], text))
    #plot(n, naive_times, kmp_times, kr_times)
    placeholder = [0] * 10
    plot(N, placeholder, kmp_times, kr_times)


if __name__ == '__main__':
    main()
