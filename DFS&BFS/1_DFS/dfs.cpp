#include <bits/stdc++.h>

using namespace std;

bool visited[9];
vector<int> graph[9];

void dfs(int x)
{
    visited[x] = true;
    cout << x << ' ';
    for (int i = 0; i < graph[x].size(); i++)
    {
        int y = graph[x][i];
        if (!visited[y])
            dfs(y);
    }
}

int main(void)
{
    graph[0].push_back(0);
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);
    graph[2].push_back(1);
    graph[2].push_back(7);
    graph[3].push_back(1);
    graph[3].push_back(4);
    graph[3].push_back(5);
    graph[4].push_back(3);
    graph[4].push_back(5);
    graph[5].push_back(3);
    graph[5].push_back(4);
    graph[6].push_back(7);
    graph[7].push_back(2);
    graph[7].push_back(6);
    graph[7].push_back(8);
    graph[8].push_back(1);
    graph[8].push_back(7);

    visited[0] = false;
    visited[1] = false;
    visited[2] = false;
    visited[3] = false;
    visited[4] = false;
    visited[5] = false;
    visited[6] = false;
    visited[7] = false;
    visited[8] = false;

    dfs(1);
}