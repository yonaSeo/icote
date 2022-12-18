#include <bits/stdc++.h>

int n, cnt;

bool check(int h, int m, int s)
{
    if (h % 10 == 3 || m % 10 == 3 || m / 10 == 3 || s % 10 == 3 || s / 10 == 3)
    {
        return true;
    }
    return false;
}

int main(void)
{
    std::cin >> n;
    for (int i = 0; i < n + 1; i++)
    {
        for (int j = 0; j < 60; j++)
        {
            for (int k = 0; k < 60; k++)
            {
                if (check(i, j, k)) cnt++;
            }
        }
    }
    std::cout << cnt << std::endl;
}