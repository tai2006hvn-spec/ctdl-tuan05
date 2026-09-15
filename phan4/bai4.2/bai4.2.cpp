#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Act {
    string name;
    int s;
    int f;
};

bool chong_nhau(const Act &a, const Act &b) {
    return !(a.f <= b.s || b.f <= a.s);
}

vector<Act> chon_ket_thuc_som_nhat(vector<Act> acts) {
    sort(acts.begin(), acts.end(), [](const Act &a, const Act &b) {
        if (a.f != b.f) return a.f < b.f;
        return a.s < b.s;
    });
    vector<Act> chon;
    int het = -1;
    for (const auto &h : acts) {
        if (h.s >= het) {
            chon.push_back(h);
            het = h.f;
        }
    }
    return chon;
}

vector<Act> chon_bat_dau_som_nhat(vector<Act> acts) {
    sort(acts.begin(), acts.end(), [](const Act &a, const Act &b) {
        if (a.s != b.s) return a.s < b.s;
        return a.f < b.f;
    });
    vector<Act> chon;
    int het = -1;
    for (const auto &h : acts) {
        if (h.s >= het) {
            chon.push_back(h);
            het = h.f;
        }
    }
    return chon;
}

vector<Act> chon_ngan_nhat(vector<Act> acts) {
    vector<Act> lai = acts;
    vector<Act> chon;
    while (!lai.empty()) {
        Act tot = lai[0];
        for (size_t i = 1; i < lai.size(); i++) {
            int len_q = lai[i].f - lai[i].s;
            int len_tot = tot.f - tot.s;
            if (len_q < len_tot || (len_q == len_tot && lai[i].f < tot.f)) {
                tot = lai[i];
            }
        }
        chon.push_back(tot);
        vector<Act> moi;
        for (const auto &g : lai) {
            if (!chong_nhau(tot, g)) moi.push_back(g);
        }
        lai = moi;
    }
    sort(chon.begin(), chon.end(), [](const Act &a, const Act &b) { return a.s < b.s; });
    return chon;
}

vector<Act> chon_it_chong_lan_nhat(vector<Act> acts) {
    vector<Act> lai = acts;
    vector<Act> chon;
    while (!lai.empty()) {
        auto dem_chong = [&](const Act &h) {
            int c = 0;
            for (const auto &g : lai) {
                if (g.name != h.name && chong_nhau(h, g)) c++;
            }
            return c;
        };

        Act tot = lai[0];
        for (size_t i = 1; i < lai.size(); i++) {
            int bac_q = dem_chong(lai[i]);
            int bac_tot = dem_chong(tot);
            if (bac_q < bac_tot || (bac_q == bac_tot && lai[i].f < tot.f)) {
                tot = lai[i];
            }
        }
        chon.push_back(tot);
        vector<Act> moi;
        for (const auto &g : lai) {
            if (!chong_nhau(tot, g)) moi.push_back(g);
        }
        lai = moi;
    }
    sort(chon.begin(), chon.end(), [](const Act &a, const Act &b) { return a.s < b.s; });
    return chon;
}

vector<Act> loi_giai_toi_uu(vector<Act> acts) {
    sort(acts.begin(), acts.end(), [](const Act &a, const Act &b) { return a.f < b.f; });
    int n = acts.size();
    vector<int> f(n, 1);
    vector<int> trace(n, -1);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (acts[j].f <= acts[i].s) {
                if (f[j] + 1 > f[i]) {
                    f[i] = f[j] + 1;
                    trace[i] = j;
                }
            }
        }
    }
    int max_idx = 0;
    for (int i = 1; i < n; i++) {
        if (f[i] > f[max_idx]) max_idx = i;
    }
    vector<Act> best;
    int cur = max_idx;
    while (cur != -1) {
        best.push_back(acts[cur]);
        cur = trace[cur];
    }
    reverse(best.begin(), best.end());
    return best;
}

string format_acts(const vector<Act> &acts) {
    string s = "{";
    for (size_t i = 0; i < acts.size(); i++) {
        s += acts[i].name;
        if (i + 1 < acts.size()) s += ", ";
    }
    s += "}";
    return s;
}

int main() {
    vector<Act> activities = {
        {"H1", 1, 5},
        {"H2", 2, 5},
        {"H3", 2, 6},
        {"H4", 3, 4},
        {"H5", 4, 8},
        {"H6", 6, 9},
        {"H7", 8, 11},
        {"H8", 9, 14},
        {"H9", 11, 13},
        {"H10", 12, 15}
    };

    auto res_kt = chon_ket_thuc_som_nhat(activities);
    auto res_bd = chon_bat_dau_som_nhat(activities);
    auto res_nn = chon_ngan_nhat(activities);
    auto res_cl = chon_it_chong_lan_nhat(activities);
    auto res_opt = loi_giai_toi_uu(activities);

    int opt_cnt = res_opt.size();

    vector<pair<string, vector<Act>>> table = {
        {"Ket thuc som nhat", res_kt},
        {"Bat dau som nhat", res_bd},
        {"Ngan nhat", res_nn},
        {"It chong lan nhat", res_cl},
        {"So nhieu nhat that su", res_opt}
    };

    cout << string(80, '=') << "\n";
    cout << "BANG 4.2. BON TIEU CHI THAM LAM VA LOI GIAI TOI UU TREN BO MUOI HOAT DONG\n";
    cout << string(80, '=') << "\n";
    cout << left << setw(24) << "Tieu chi" << " | "
         << setw(28) << "Cac hoat dong duoc chon" << " | "
         << setw(6) << "So HD" << " | "
         << "Dat toi uu\n";
    cout << string(80, '-') << "\n";

    for (const auto &item : table) {
        int cnt = item.second.size();
        string is_opt = (cnt == opt_cnt) ? "Co" : "Khong";
        if (item.first == "So nhieu nhat that su") is_opt = "Toi uu";

        cout << left << setw(24) << item.first << " | "
             << setw(28) << format_acts(item.second) << " | "
             << setw(6) << cnt << " | "
             << is_opt << "\n";
    }
    cout << string(80, '=') << "\n";

    return 0;
}