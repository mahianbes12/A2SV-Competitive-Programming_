#Insertion Sort - Part 1 - HackerRank
def insertionSort1(n, arr):
    value = arr[n-1]  # Store the value to be inserted
    i = n - 2  # Start comparing from the second-to-last element

    while i >= 0 and arr[i] > value:
        arr[i+1] = arr[i]  # Shift elements to the right
        i -= 1
        print(*arr)  # Print the array after each shift

    arr[i+1] = value  # Insert the stored value at the correct position
    print(*arr)  # Print the final sorted array


# Example usage
n = 5
arr = [2, 4, 6, 8, 3]
insertionSort1(n, arr)