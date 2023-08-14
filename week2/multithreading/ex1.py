from threading import Thread
from multiprocessing import Pool

from random import random
import time


def generate_number():
    return round(random() * 100)


def produce_lists(number_of_lists):
    my_list = []
    for i in range(number_of_lists):
        my_list.append([])
        for j in range(100):
            my_list[i].append(generate_number())
    return my_list


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def sort_half_list(half_list):
    for i in range(len(half_list)):
        half_list[i] = bubble_sort(half_list[i])
    return half_list


def calculate_concurrency(first_half, second_half):
    t1 = Thread(target=sort_half_list, args=[first_half])
    t2 = Thread(target=sort_half_list, args=[second_half])
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    return end - start


def calculate_parallel(first_half, second_half):
    pool = Pool(processes=2)
    start = time.time()
    p1 = pool.apply_async(sort_half_list, [first_half])
    p2 = pool.apply_async(sort_half_list, [second_half])
    pool.close()
    pool.join()
    end = time.time()
    return end - start


def main():
    nested_list = produce_lists(1000)
    mid_idx = round(len(nested_list) / 2)
    first_half = nested_list[:mid_idx]
    second_half = nested_list[mid_idx:]

    concurrency_time = calculate_concurrency(first_half, second_half)
    parallel_time = calculate_parallel(first_half, second_half)

    print(f"Time taken using threading module: {concurrency_time}")
    print(f"Time taken using multiprocessing module: {parallel_time}")


if __name__ == "__main__":
    main()
