from threading import Thread
from multiprocessing import Pool

from random import random
import time


def generate_number():
    return round(random() * 100)


def split_list(data, pieces):
    chunk_size = len(data) // pieces
    remain = len(data) % pieces

    result = []
    starter = 0
    for i in range(pieces):
        slicer = starter + chunk_size + (1 if i < remain else 0)
        result.append(data[starter:slicer])
        starter = slicer
    return result


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


def sort_chunk_list(chunk_list):
    for i in range(len(chunk_list)):
        chunk_list[i] = bubble_sort(chunk_list[i])
    return chunk_list


def calculate_concurrency(nested_list, N):
    splited_list = split_list(nested_list, N)
    results = []
    for i, arr in enumerate(splited_list):
        results.append(Thread(target=sort_chunk_list, args=[arr]))
    start = time.time()
    for result in results:
        result.start()
    for result in results:
        result.join()
    end = time.time()
    return end - start


def calculate_parallel(nested_list, n):
    pool = Pool(processes=n)
    splited_list = split_list(nested_list, n)
    start = time.time()
    for i, arr in enumerate(splited_list):
        pool.apply_async(sort_chunk_list, [arr])
    pool.close()
    pool.join()
    end = time.time()
    return end - start


def main():
    nested_list = produce_lists(20000)

    concurrency_time = calculate_concurrency(nested_list, 2)
    parallel_time = calculate_parallel(nested_list, 2)

    print(f"Time taken using threading module: {concurrency_time}")
    print(f"Time taken using multiprocessing module: {parallel_time}")


if __name__ == "__main__":
    main()
