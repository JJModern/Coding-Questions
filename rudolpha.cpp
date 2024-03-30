#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t; std::cin >> t;f
    int tempT = t;

    vector<int> result;
    while (tempT--) {
        int n, m, k; cin >> n >> m >> k;
        vector<int> nlist(n), mlist(m);
        int i = 0;
        while (n--) {
            cin >> nlist[i];
            i++;
        }
        i = 0;
        while (m--) {
            cin >> mlist[i];
            i++;
        }

        sort(nlist.begin(), nlist.end());
        sort(mlist.begin(), mlist.end());

        i = 0;
        int total = 0;
        int j = mlist.size() - 1;
        while (j >= 0) {
            if (i == nlist.size()) {
                total += (j + 1) * i;
                break;
            } else {
                while (i < nlist.size() && nlist[i] + mlist[j] <= k) {
                    i++;
                }
                total += i;
            }
            j--;
        }

        result.push_back(total);
        
        // // printing out 
        // cout << "nlist: ";
        // for (int num : nlist) {
        //     cout << num;
        // }
        // cout << endl;

        // cout << "mlist: ";
        // for (int num : mlist) {
        //     cout << num;
        // }
        // cout << endl;
    }
    // // printing out results
    for (int num : result) {
        cout << num << endl;
    }

}

//     // Read each line of the grid

