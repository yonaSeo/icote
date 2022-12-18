#include <bits/stdc++.h>

using namespace std;

int n;
string plans;

int x = 1;
int y = 1;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
char moveTypes[4] = {'L', 'R', 'U', 'D'};

int main(void)
{
    cin >> n;
    cin.ignore(); // 정수 다음에 문자열이 주어질 때는 버퍼를 지워주어야 한다.
    getline(cin, plans);

    for (int i = 0; i < plans.size(); i++)
    {
        char plan = plans[i];
        int nx = 0;
        int ny = 0;
        for (int j = 0; j < 4; j++)
        {
            if (moveTypes[j] == plan)
            {
                nx = x + dx[j];
                ny = y + dy[j];
                break;
            }
        }
        if (nx < 1 || ny < 1 || nx > n || ny > n)
            continue;
        x = nx;
        y = ny;
    }
    cout << x << ' ' << y << endl;
    return 0;
}