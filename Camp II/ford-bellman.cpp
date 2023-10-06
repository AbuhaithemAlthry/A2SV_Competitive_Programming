#include <iostream>
#include <vector>
using namespace std;

struct edge {
    int u, v, w;
};

const int inf = 5e5 + 5;

void Ford_Bellman() {
    int n, m;
    cin >> n >> m;
    vector<edge> e(m);

    for (int i = 0; i < m; ++i) {
        cin >> e[i].u >> e[i].v >> e[i].w;
    }

    vector<int> dist(n + 1, inf);
    dist[1] = 0;
    bool updated;

    for (int i = 1; i < n; ++i) {
        updated = false;

        for (edge temp : e) {
            updated = true;

            if (dist[temp.u] != inf && dist[temp.v] > dist[temp.u] + temp.w) {
                dist[temp.v] = dist[temp.u] + temp.w;
            }
        }

        if (!updated) {
            break;
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << (dist[i] == inf ? 30000 : dist[i]) << " ";
    }

    cout << endl;
}

int main() {
    Ford_Bellman();
    return 0;
}
