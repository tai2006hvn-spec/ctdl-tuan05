#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string>

using namespace std;

pair<int, vector<int>> doi_tien_tham_lam(vector<int> coins, int S) {
    sort(coins.rbegin(), coins.rend());
    vector<int> res;
    int rem = S;
    for (int c : coins) {
        while (rem >= c) {
            res.push_back(c);
            rem -= c;
        }
    }
    if (rem != 0) return {-1, {}};
    return {(int)res.size(), res};
}

pair<int, vector<int>> doi_tien_qhd(vector<int> coins, int S) {
    const int INF = 1e9;
    vector<int> f(S + 1, INF);
    vector<int> vet(S + 1, -1);
    f[0] = 0;

    for (int c : coins) {
        for (int j = c; j <= S; j++) {
            if (f[j - c] + 1 < f[j]) {
                f[j] = f[j - c] + 1;
                vet[j] = c;
            }
        }
    }

    if (f[S] >= INF) return {-1, {}};

    vector<int> res;
    int cur = S;
    while (cur > 0) {
        int c = vet[cur];
        res.push_back(c);
        cur -= c;
    }
    sort(res.rbegin(), res.rend());
    return {f[S], res};
}

string format_way(const vector<int> &way) {
    string s = "";
    for (size_t i = 0; i < way.size(); i++) {
        s += to_string(way[i]);
        if (i + 1 < way.size()) s += " + ";
    }
    return s;
}

struct Dataset {
    int id;
    vector<int> coins;
    int S;
};

int main() {
    vector<Dataset> datasets = {
        {1, {1, 4, 6, 9}, 12},
        {2, {1, 5, 10, 20, 50}, 85},
        {3, {1, 3, 7, 12}, 20},
        {4, {1, 2, 5, 10}, 38},
        {5, {1, 6, 10}, 12},
        {6, {1, 4, 5, 15, 20}, 23}
    };

    cout << string(80, '=') << "\n";
    cout << "BANG 4.1. THAM LAM SO VOI QUY HOACH DONG TREN SAU BO MENH GIA\n";
    cout << string(80, '=') << "\n";
    cout << left << setw(4) << "Bo" << " | "
         << setw(8) << "TL (to)" << " | "
         << setw(22) << "Cach tra tham lam" << " | "
         << setw(8) << "QHD (to)" << " | "
         << setw(20) << "Cach tra toi uu" << " | "
         << "Tham lam dung?\n";
    cout << string(80, '-') << "\n";

    for (const auto &d : datasets) {
        auto g = doi_tien_tham_lam(d.coins, d.S);
        auto dp = doi_tien_qhd(d.coins, d.S);
        string is_correct = (g.first == dp.first) ? "Dung" : "Sai";

        cout << left << setw(4) << d.id << " | "
             << setw(8) << g.first << " | "
             << setw(22) << format_way(g.second) << " | "
             << setw(8) << dp.first << " | "
             << setw(20) << format_way(dp.second) << " | "
             << is_correct << "\n";
    }
    cout << string(80, '=') << "\n";

    return 0;
}