import copy
import time
import random
import matplotlib.pyplot as plt


def insertion_sort(arr):
    """
    Insertion sort implementation from https://www.geeksforgeeks.org/python-program-for-insertion-sort/
    """
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key


def merge(arr, l, m, r):
    """
    Merge implementation from https://www.geeksforgeeks.org/python-program-for-merge-sort/
    """
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    """
    Merge sort implementation from https://www.geeksforgeeks.org/python-program-for-merge-sort/
    """
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def time_sorting_algorithms():
    insertion_sort_timings = {}
    merge_sort_timings = {}
    intersect = None

    for i in range(150):
        # Create a random list in range i
        # This list will be identical for both sorting algorithms to ensure fairness
        nums = [random.randint(0, 100) for j in range(i)]

        # Time and run insertion sort 2000 times
        total_time = 0
        for _ in range(2000):
            insertion_sort_nums = copy.deepcopy(nums)
            start = time.time()
            insertion_sort(insertion_sort_nums)
            end = time.time()
            total_time += end - start

        insertion_sort_timings[i] = total_time / 2000

        # Time and run merge sort 2000 times
        total_time = 0
        for _ in range(2000):
            merge_sort_nums = copy.deepcopy(nums)
            start = time.time()
            merge_sort(merge_sort_nums, 0, i - 1)
            end = time.time()
            total_time += end - start

        merge_sort_timings[i] = total_time / 2000

        # Find last intersection point
        if merge_sort_timings[i] > insertion_sort_timings[i]:
            intersect = i

    print("Finished run of sorting algorithms!")
    print(f"Insertion sort became less efficient at n = {intersect}")
    return insertion_sort_timings, merge_sort_timings


def display_plot(insertion_sort_timings, merge_sort_timings):
    insertion_sort_n_values, insertion_sort_times = zip(*sorted(insertion_sort_timings.items()))
    merge_sort_n_values, merge_sort_times = zip(*sorted(merge_sort_timings.items()))

    plt.figure(figsize=(10, 6))
    plt.plot(insertion_sort_n_values, insertion_sort_times, label='Insertion Sort')
    plt.plot(merge_sort_n_values, merge_sort_times, label='Merge Sort')
    plt.title('Algorithm Comparison')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    insertion_sort_timings, merge_sort_timings = time_sorting_algorithms()
    display_plot(insertion_sort_timings, merge_sort_timings)


if __name__ == "__main__":
    main()
    print()
