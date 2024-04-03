def selectionSort(arr):
    for i in range(0, len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx = j
    arr[j], arr[i+1] = arr[i+1], arr[j]

arr=[4, 9, 3, 6, 2]
selectionSort(arr)
print(arr)
