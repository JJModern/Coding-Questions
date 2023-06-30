#include <iostream>
#include <vector>
#include <string>
#include <sstream>

int main() {
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        int length, insert_num;
        std::cin >> length >> insert_num;

        std::vector<int> num_list(length);
        for (int j = 0; j < length; j++) {
            std::cin >> num_list[j];
        }

        int return_i = length;

        for (int num_i = 0; num_i < length; num_i++) {
            if (insert_num >= num_list[num_i]) {
                std::vector<int> second_half(num_list.begin() + num_i, num_list.end());
                std::stringstream would_be_str, without_str;
                would_be_str << insert_num;
                without_str << insert_num;
                for (int x : second_half) {
                    would_be_str << x;
                    without_str << x;
                }
                without_str << insert_num;

                int would_be, without;
                would_be_str >> would_be;
                without_str >> without;

                if (would_be > without) {
                    return_i = num_i;
                    break;
                }
            }
        }

        num_list.insert(num_list.begin() + return_i, insert_num);

        for (int num : num_list) {
            std::cout << num;
        }
        std::cout << std::endl;
    }

    return 0;
}
