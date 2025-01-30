from sorts import *
import matplotlib.pyplot as plt
import numpy as np
import random
import time


def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(size))

def generate_reversed_sorted_array(size):
    return list(range(size, 0, -1))

def generate_nearly_sorted_array(size):
    arr = list(range(size))
    for _ in range(size // 20):
        idx1, idx2 = random.randint(0, size-1), random.randint(0, size-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr


def test(sort_type, generated_array_type, plot_title):
    time_arr = []
    size_arr = []
    for i in range(0, 10001, 125):
        arr = generated_array_type(i)

        start_time = time.time()
        sort_type(arr)
        finish_time = time.time()

        time_arr.append(finish_time - start_time)
        size_arr.append(i)

    p = np.polyfit(size_arr, time_arr, 2)

    plt.figure(figsize=(10, 6))
    plt.scatter(size_arr, time_arr)

    plt.title(plot_title)
    plt.xlabel('Размер входных данных n')
    plt.ylabel('Время выполнения T(n)')
    plt.legend()
    plt.grid()

    plt.plot(size_arr, np.polyval(p, size_arr), color='red')

    plt.tight_layout()
    plt.show()
