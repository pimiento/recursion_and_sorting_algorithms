#!/usr/bin/env python3
import sys
import timeit
from typing import List

import time
import math
import random
import argparse
from multiprocessing import Pool


def merge(numbers, l1, r1, l2, r2):
    sorted_num = [0] * (r2 - l1 + 1)
    i = 0
    while (l1 <= r1 or l2 <= r2):
        if l1 > r1:
            sorted_num[i] = numbers[l2]
            l2 += 1
        elif l2 > r2:
            sorted_num[i] = numbers[l1]
            l1 += 1
        elif numbers[l1] < numbers[l2]:
            sorted_num[i] = numbers[l1]
            l1 += 1
        else:
            sorted_num[i] = numbers[l2]
            l2 += 1
        i += 1
    return sorted_num


def mergesort(numbers, l, r):
    if l == r:
        return

    m = (l + r) // 2

    mergesort(numbers, l, m)
    mergesort(numbers, m+1, r)

    numbers[l:r+1] = merge(numbers, l, m, m+1, r)
    return


def parallel_mergesort(numbers):
    mergesort(numbers, 0, len(numbers)-1)
    return numbers


def merge_lists(v1, v2):
    return merge(v1 + v2, 0, len(v1)-1, len(v1), len(v1)+len(v2)-1)


def parallel_merge(v):
    m = len(v) // 2 - 1
    return merge(v, 0, m, m + 1, len(v)-1)

def sort_alg(arr):
    n_cores = 4
    chunk_size = math.ceil(len(values) / n_cores)
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    # Start the parallel process
    pool = Pool(n_cores)
    chunks = pool.map(parallel_mergesort, chunks)
    while(len(chunks) > 2):
        data=[]
        i = 0
        while (i < len(chunks)):
            if i + 1 < len(chunks):
                data += [chunks[i] + chunks[i+1]]
            else:
                data += [chunks[i]]
            i += 2
        chunks = pool.map(parallel_merge, data)
    # We have to merge them separately because the sizes might be different and it that case
    # parallel_merge will not work.
    if (len(chunks) == 2):
        final = merge_lists(chunks[0], chunks[1])
    else:
        final = chunks[0]
    pool.close()

if __name__ == "__main__":
    int_count = sys.argv[1]
    with open(f"data/{int_count}ints.txt", "r") as data:
        arr: List[int] = [int(line.strip()) for line in data.readlines()]
        number:int = 2
        def to_call():
            return sort_alg(arr)
        result = timeit.timeit(to_call, number=number)
        print(
            f"{number} вызовов для {int_count} данных: лучший результат равен {result:.02f}"
        )
        result = sort_alg(arr)
        for i in range(len(result)-1):
            assert result[i] < result[i+1]
