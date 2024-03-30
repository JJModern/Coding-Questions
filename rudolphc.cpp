#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int t; cin >> t;
    vector<int> result(t); 

    for (int x = 0; x < t; x++) {
        int n = 0; cin >> n;

        string mystr; cin >> mystr;
        int curr = 0;

        for (int i = 0; i < n - 2; i++) {
            if (mystr[i] == 'm' && mystr[i + 1] == 'a' && mystr[i + 2] == 'p') {
                if (!(i <= n - 5 && mystr[i + 3] == 'i' && mystr[i + 4] == 'e')) {
                    curr++;
                } 
            } else if (mystr[i] == 'p' && mystr[i + 1] == 'i' && mystr[i + 2] == 'e') {
                curr++;
            }
        }
        result[x] = curr;
    }

    for (int i = 0; i < t; i++) {
        cout << result[i] << endl;
    }
}