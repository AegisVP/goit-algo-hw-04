import timeit
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort


def benchmark_algorythm(algorythm):
    data_small = [random.randint(0, 100) for _ in range(100)]
    data_medium = [random.randint(0, 1_000) for _ in range(1_000)]
    data_large = [random.randint(0, 10_000) for _ in range(10_000)]

    if algorythm == '.sort()':
        time_small = timeit.timeit(lambda: data_small[:].sort(), number=10)
        time_medium = timeit.timeit(lambda: data_medium[:].sort(), number=10)
        time_large = timeit.timeit(lambda: data_large[:].sort(), number=10)
    else:
        time_small = timeit.timeit(lambda: algorythm(data_small[:]), number=10)
        time_medium = timeit.timeit(lambda: algorythm(data_medium[:]), number=10)
        time_large = timeit.timeit(lambda: algorythm(data_large[:]), number=10)

    return (time_small, time_medium, time_large)


def benchmark_searches():

    print(f"{'| Algorithm': <20} | {'Time (s) small data': <20} | {'Time (s) medium data': <20} | {'Time (s) large data': <20}")
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19} | :{'-'*19}")

    (time_small_insertion, time_medium_insertion, time_large_insertion) = benchmark_algorythm(insertion_sort)
    print(f"{'| Insertion sort': <20} | {time_small_insertion:<20.5f} | {time_medium_insertion:<20.5f} | {time_large_insertion:<20.5f}")

    (time_small_merge, time_medium_merge, time_large_merge) = benchmark_algorythm(merge_sort)
    print(f"{'| Merge sort': <20} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f} | {time_large_merge:<20.5f}")

    (time_small_sorted, time_medium_sorted, time_large_sorted) = benchmark_algorythm(sorted)
    print(f"{'| sorted function': <20} | {time_small_sorted:<20.5f} | {time_medium_sorted:<20.5f} | {time_large_sorted:<20.5f}")

    (time_small_sort, time_medium_sort, time_large_sort) = benchmark_algorythm('.sort()')
    print(f"{'| .sort method': <20} | {time_small_sort:<20.5f} | {time_medium_sort:<20.5f} | {time_large_sort:<20.5f}")


if __name__ == '__main__':
    benchmark_searches()
