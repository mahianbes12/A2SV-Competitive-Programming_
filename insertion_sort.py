#Insertion Sort - Part 1 - HackerRank
def insertionSort1(n, arr):
    value = arr[n-1]
    i = n - 2

    while i >= 0 and arr[i] > value:
        arr[i+1] = arr[i]
        i -= 1
        print(*arr)

    arr[i+1] = value
    print(*arr)

n = 14
arr = [1, 3, 5, 9, 13, 22, 27, 35, 46, 51, 55, 83, 87,23]
insertionSort1(n, arr)