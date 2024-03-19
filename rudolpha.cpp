#include <iostream>

int main() {
    std::cin >> n;
    std::cin.ignore(); // Ignore newline

    for (int i = 0; i < n; ++i) {
        std::getline(std::cin, grid[i]);
    }

}

//     // Read each line of the grid

