#include <bits/stdc++.h>

using namespace std;

int n, k;
int result;

int main(void) {
    cin >> n >> k;
    while (true) {
        // N이 K로 나눠지는 수가 될 때까지 빼기
        int target = (n / k) * k;
        result += n - target;
        n = target;
        // N이 K보다 작아지면 (더 이상 나눌 수 없으면) 탈출
        if (n < k) break;
        // N을 K로 나누기
        n /= k;
        result++;
    }
    // 마지막으로 남은 수에 대하여 1씩 빼기
    result += (n - 1);
    cout << result << '\n';
}