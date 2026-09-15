#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <iomanip>
#include <cassert>

using namespace std;

map<string, map<string, double>> LM = {
    {"em",  {{"hoc", 0.52}, {"di", 0.48}}},
    {"hoc", {{"bai", 0.40}, {"toan", 0.35}, {"ve", 0.25}}},
    {"di",  {{"cho", 0.58}, {"boi", 0.22}, {"ngu", 0.20}}}
};

pair<string, double> liet_ke_tot_nhat() {
    double max_p = -1.0;
    string best_s = "";
    for (auto const &[w2, p2] : LM["em"]) {
        for (auto const &[w3, p3] : LM[w2]) {
            double p = p2 * p3;
            if (p > max_p) {
                max_p = p;
                best_s = "em " + w2 + " " + w3;
            }
        }
    }
    return {best_s, max_p};
}

pair<string, double> giai_ma_tham_lam() {
    string cur = "em", cau = "em";
    double prob = 1.0;
    for (int step = 0; step < 2; step++) {
        string best_w = "";
        double max_p = -1.0;
        if (LM.find(cur) != LM.end()) {
            for (auto const &[nxt, p] : LM[cur]) {
                if (p > max_p) {
                    max_p = p;
                    best_w = nxt;
                }
            }
        }
        if (max_p > 0) {
            prob *= max_p;
            cau += " " + best_w;
            cur = best_w;
        }
    }
    return {cau, prob};
}

pair<string, double> giai_ma_chum(int k) {
    vector<pair<vector<string>, double>> chum = {{{"em"}, 1.0}};
    for (int step = 0; step < 2; step++) {
        vector<pair<vector<string>, double>> ung_vien;
        for (auto const &item : chum) {
            string cur = item.first.back();
            if (LM.find(cur) != LM.end()) {
                for (auto const &[nxt, p] : LM[cur]) {
                    vector<string> new_w = item.first;
                    new_w.push_back(nxt);
                    ung_vien.push_back({new_w, item.second * p});
                }
            }
        }
        if (ung_vien.empty()) break;
        sort(ung_vien.begin(), ung_vien.end(), [](const auto &a, const auto &b) {
            return a.second > b.second;
        });
        if ((int)ung_vien.size() > k) ung_vien.resize(k);
        chum = ung_vien;
    }
    string res = "";
    if (!chum.empty()) {
        for (int i = 0; i < (int)chum[0].first.size(); i++) {
            if (i > 0) res += " ";
            res += chum[0].first[i];
        }
        return {res, chum[0].second};
    }
    return {"", 0.0};
}

vector<string> words = {"em", "hoc", "bai", "toan"};
vector<string> tags = {"N", "V"};
map<string, double> pi_map = {{"N", 0.6}, {"V", 0.4}};
map<string, map<string, double>> A = {
    {"N", {{"N", 0.35}, {"V", 0.65}}},
    {"V", {{"N", 0.70}, {"V", 0.30}}}
};
map<string, map<string, double>> B = {
    {"N", {{"em", 0.35}, {"hoc", 0.10}, {"bai", 0.40}, {"toan", 0.30}}},
    {"V", {{"em", 0.05}, {"hoc", 0.45}, {"bai", 0.05}, {"toan", 0.02}}}
};

void chay_viterbi(vector<map<string, double>> &f, vector<map<string, string>> &tu, vector<string> &day_nhan, double &max_prob) {
    int T = words.size();
    f.assign(T, map<string, double>());
    tu.assign(T, map<string, string>());
    
    for (const string &t : tags) {
        f[0][t] = pi_map[t] * B[t][words[0]];
        tu[0][t] = "-";
    }
    
    for (int i = 1; i < T; i++) {
        for (const string &t : tags) {
            double best_val = -1.0;
            string best_prev = "";
            for (const string &s : tags) {
                double val = f[i - 1][s] * A[s][t];
                if (val > best_val) {
                    best_val = val;
                    best_prev = s;
                }
            }
            f[i][t] = best_val * B[t][words[i]];
            tu[i][t] = best_prev;
        }
    }
    
    string cuoi = (f[T - 1]["N"] >= f[T - 1]["V"]) ? "N" : "V";
    max_prob = f[T - 1][cuoi];
    day_nhan.assign(T, "");
    day_nhan[T - 1] = cuoi;
    for (int i = T - 1; i >= 1; i--) {
        day_nhan[i - 1] = tu[i][day_nhan[i]];
    }
}

pair<vector<string>, double> vet_can_viterbi() {
    vector<string> best_seq;
    double best_prob = -1.0;
    for (const string &t1 : tags) {
        for (const string &t2 : tags) {
            for (const string &t3 : tags) {
                for (const string &t4 : tags) {
                    double p = pi_map[t1] * B[t1][words[0]] *
                               A[t1][t2] * B[t2][words[1]] *
                               A[t2][t3] * B[t3][words[2]] *
                               A[t3][t4] * B[t4][words[3]];
                    if (p > best_prob) {
                        best_prob = p;
                        best_seq = {t1, t2, t3, t4};
                    }
                }
            }
        }
    }
    return {best_seq, best_prob};
}

int main() {
    auto [cau_tot, diem_tot] = liet_ke_tot_nhat();
    auto [cau_tham_lam, diem_tham_lam] = giai_ma_tham_lam();
    auto [cau_chum_1, diem_chum_1] = giai_ma_chum(1);
    auto [cau_chum_2, diem_chum_2] = giai_ma_chum(2);
    auto [cau_chum_3, diem_chum_3] = giai_ma_chum(3);
    
    vector<map<string, double>> f;
    vector<map<string, string>> tu;
    vector<string> day_nhan;
    double max_prob = 0;
    chay_viterbi(f, tu, day_nhan, max_prob);
    
    cout << "BANG 4.3. BA THUAT TOAN GIAI MA\n";
    cout << "Liet ke: " << cau_tot << " (" << fixed << setprecision(4) << diem_tot << ")\n";
    cout << "Tham lam: " << cau_tham_lam << " (" << diem_tham_lam << ")\n";
    cout << "Chum k=1: " << cau_chum_1 << " | k=2: " << cau_chum_2 << " | k=3: " << cau_chum_3 << "\n";
    cout << "Viterbi: ";
    for (int i = 0; i < (int)day_nhan.size(); i++) {
        if (i > 0) cout << " ";
        cout << day_nhan[i];
    }
    cout << " | Xac suat: " << fixed << setprecision(6) << max_prob << "\n";
    return 0;
}