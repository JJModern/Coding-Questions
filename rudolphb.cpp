#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t; cin >> t;

    cin.ignore();
    vector<string> result;

    while (t--) {
        int n; cin >> n;

        vector<int> alist(n);
        for (int i = 0; i < n; i++) {
            cin >> alist[i];
        }
        string curr_result = "YES";
        for (int i = 0; i < n - 2; i++) {
            alist[i + 1] -= 2 * alist[i];
            alist[i + 2] -= alist[i];
            alist[i] = 0;
            if (alist[i + 1] < 0 || alist[i + 2] < 0) {
                curr_result = "NO";
                break;
            }
        }
        if (alist[n - 2] > 0 || alist[n - 1] > 0) {
            curr_result = "NO";
        }

        result.push_back(curr_result);

    }

    for (string num : result) {
        cout << num << endl;
    }


}