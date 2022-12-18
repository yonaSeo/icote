#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> arr;

int main(void) {
    cin >> n;
    for (int i=0; i<n; i++) {
        int x;
        cin >> x;
        arr.push_back(x);
    }
    
    sort(arr.begin(), arr.end());

    int result;
    int cnt;

    for (int i=0; i<n; i++) {
        cnt++;
        if (cnt >= arr[i]) {
            result++;
            cnt = 0;
        }
    }

    cout << result << endl;
}