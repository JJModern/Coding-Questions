#include <iostream>
#include <vector>

using namespace std;


int mod3(int n) {
    int remainder = n % 3;
    int total = n / 3;
    if (remainder != 0) {
        total++;
    }
    return total;
}

int main() {
    int t; cin >> t;

    vector<int> result(t);

    for (int i = 0; i < t; i++) {
        int a, b, c; cin >> a >> b >> c;
        int total = 0;

        total += a + (b / 3);
        int remainder = b % 3;
        if (remainder == 0) {
            //function to figure out
            total += mod3(c);
            result[i] = total;
        } else if (remainder != 0 && (c < (3 - remainder))) {
            result[i] = -1;
        } else {
            //same function to figure out
            total += 1 + mod3(c - (3 - remainder));
            result[i] = total;
        }
    }
    
    for (int num : result) {
        cout << num << endl;
    }


}

