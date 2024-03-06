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

n = 5
arr = [2, 4, 6, 8, 3]
insertionSort1(n, arr)