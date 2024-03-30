#include <tuple>
#include <vector>
#include <iostream>
#include <string>
#include <deque>
#include <set>


using namespace std;

int main() {
    int t; cin >> t;

    vector<set<int> > result(t);

    for (int i = 0; i < t; i++) {
        int n, m, x; cin >> n >> m >> x;
        // # players, # throws, # of the starting player 
        deque<tuple <int, int> > myqueue(1, make_tuple(0, x));
        set<int> myset;
        myset.insert(x);

        for (int j = 0; j < m; j++) {
            int distance = 0; string direction; cin >> distance >> direction;
            // check if myqueue is empty. 
            set<int> currset; 
            for (int num : myset) {
                if (direction == "?") {
                    int first = (num + distance + n) % n;
                    int second = (num - distance + n) % n;
                    if (first == 0) {
                        first += n;
                    }
                    if (second == 0) {
                        second += n;
                    }
                    currset.insert(first);
                    currset.insert(second);
                } else if (direction == "0") {
                    int first = (num + distance + n) % n;
                    if (first == 0) {
                        first += n;
                    }
                    currset.insert(first);
                } else {
                    int first = (num - distance + n) % n;
                    if (first == 0) {
                        first += n;
                    }
                    currset.insert(first);
                }

            }
            myset = currset;
        }

        result[i] = myset;
    }

    // this can be optimized
    for (set<int> myset : result) {
        cout << myset.size() << endl;
        for (int num : myset) {
            cout << num << " ";
        }
        cout << endl;
    }


}

