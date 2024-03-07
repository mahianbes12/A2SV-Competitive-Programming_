#include <iostream>

void countSwaps(int a[], int n) {
    int numSwaps = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1; j++) {
            if (a[j] > a[j + 1]) {
                std::swap(a[j], a[j + 1]);
                numSwaps++;
            }
        }
    }

    std::cout << "Array is sorted in " << numSwaps << " swaps." << std::endl;
    std::cout << "First Element: " << a[0] << std::endl;
    std::cout << "Last Element: " << a[n - 1] << std::endl;
}

int main() {
    int n;
    std::cin >> n;

    int a[n];
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    countSwaps(a, n);

    return 0;
}