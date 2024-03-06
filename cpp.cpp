#include <iostream>

void insertionSort1(int n, int* arr) {
    int value = arr[n - 1];
    int i = n - 2;

    while (i >= 0 && arr[i] > value) {
        arr[i + 1] = arr[i];
        i--;
        for (int j = 0; j < n; j++) {
            std::cout << arr[j] << " ";
        }
        std::cout << std::endl;
    }

    arr[i + 1] = value;
    for (int j = 0; j < n; j++) {
        std::cout << arr[j] << " ";
    }
    std::cout << std::endl;
    
    delete[] arr;
}

int main() {
    int n;
    std::cin >> n;

    int* arr = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    insertionSort1(n, arr);

    return 0;
}