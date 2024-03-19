#include <iostream>
#include <vector>
#include <utility>

int n;
std::vector<std::string> grid;
std::vector<std::pair<int, int>> queue;

bool inc_win_check(std::pair<int, int> row_cols) {
    int row = row_cols.first;
    int col = row_cols.second;
    
    if (grid[row][col] == 'O') {
        return false;
    }

    bool row_win = true;
    for (int new_col = 0; new_col < n; ++new_col) {
        if (grid[row][new_col] != 'X') {
            row_win = false;
            break;
        }
    }
    if (row_win) {
        return true;
    }

    bool col_win = true;
    for (int new_row = 0; new_row < n; ++new_row) {
        if (grid[new_row][col] != 'X') {
            col_win = false;
            break;
        }
    }
    if (col_win) {
        return true;
    }

    // Additional checks for diagonal wins only if necessary
    if (row != col && n - 1 - col != row) {
        return false;
    }

    bool downright = true;
    bool upright = true;
    for (int i = 0; i < n; ++i) {
        if (grid[i][i] != 'X') {
            downright = false;
        }
        if (grid[n - 1 - i][i] != 'X') {
            upright = false;
        }
    }

    return downright || upright;
}

int dfs(std::pair<int, int> row_cols, bool dont_check = false) {

    // // Grid Print
    // for (const auto& row : grid) {
    //     std::cout << row << std::endl;
    // }

      // // Print Queue 
    // for (const auto& p : queue) {
    //     std::cout << "Row: " << p.first << ", Col: " << p.second << std::endl;
    // }

    if (!dont_check && inc_win_check(row_cols)) {
        // std::cout << "This is mathematical" << (1 << queue.size());
        return 1 << queue.size();
    } else {
        if (queue.empty()) {
            // std::cout << "Empty Queue";
            return 0;
        }

        // Get the last element in the queue
        auto [row, col] = queue.back(); queue.pop_back();

        grid[row][col] = 'X';
        int xtotal = dfs({row, col});

        grid[row][col] = 'O';
        int ototal = dfs({row, col}, true);

        grid[row][col] = '.';
        queue.push_back({row, col});

        // std::cout << "This is ototal + xtotal" << ototal << xtotal << std::endl;

        return ototal + xtotal;
    }
}


int main() {

    std::cin >> n; // Read the size of the grid
    std::cin.ignore(); // Ignore the newline character after the integer input

    grid.resize(n); 

    // Read each line of the grid
    for (int i = 0; i < n; ++i) {
        std::getline(std::cin, grid[i]);
    }

    // Update Queue
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < n; ++col) {
            if (grid[row][col] == '.') {
                queue.push_back(std::make_pair(row, col));
            }
        }
    }


    // // Print Queue 
    // for (const auto& p : queue) {
    //     std::cout << "Row: " << p.first << ", Col: " << p.second << std::endl;
    // }

    // TODO: make check_win
    if (queue.empty() && true) {
    // if (queue.empty() && check_win()) {
        std::cout << "1";
    } else {
        std::cout << dfs({0, 0}, true);
    }

    return 0;
}


