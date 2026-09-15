#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <string>

using namespace std;

void cai_tui(const vector<int> &w, const vector<int> &v, int W, const vector<string> &names) {
    int n = w.size();
    vector<vector<int>> f(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= W; j++) {
            f[i][j] = f[i - 1][j]; 
            if (w[i - 1] <= j) {   
                f[i][j] = max(f[i][j], f[i - 1][j - w[i - 1]] + v[i - 1]);
            }
        }
    }

    cout << "--- BANG QUY HOACH DONG f[i][j] ---\n";
    cout << left << setw(12) << "f[i][j]";
    for (int j = 0; j <= W; j++) cout << right << setw(4) << j;
    cout << "\n";

    cout << left << setw(12) << "i=0";
    for (int j = 0; j <= W; j++) cout << right << setw(4) << f[0][j];
    cout << "\n";

    for (int i = 1; i <= n; i++) {
        string label = "i=" + to_string(i) + " (" + names[i - 1] + ")";
        cout << left << setw(12) << label;
        for (int j = 0; j <= W; j++) cout << right << setw(4) << f[i][j];
        cout << "\n";
    }

    vector<int> chon;
    int j = W;
    for (int i = n; i >= 1; i--) {
        if (f[i][j] != f[i - 1][j]) {
            chon.push_back(i);
            j -= w[i - 1];
        }
    }
    reverse(chon.begin(), chon.end());

    int total_w = 0;
    cout << "\n--- KET QUA ---\n";
    cout << "Gia tri lon nhat f[" << n << "][" << W << "]: " << f[n][W] << "\n";
    cout << "Tap do vat duoc chon: ";
    for (size_t k = 0; k < chon.size(); k++) {
        cout << names[chon[k] - 1] << (k + 1 < chon.size() ? ", " : "");
        total_w += w[chon[k] - 1];
    }
    cout << " (chi so: ";
    for (size_t k = 0; k < chon.size(); k++) {
        cout << chon[k] << (k + 1 < chon.size() ? ", " : "");
    }
    cout << ")\n";
    cout << "Tong trong luong: " << total_w << " / " << W << "\n";
}

int main() {
    vector<int> w = {2, 3, 4, 5, 7};
    vector<int> v = {3, 7, 9, 12, 16};
    vector<string> names = {"A", "B", "C", "D", "E"};
    int W = 11;

    cai_tui(w, v, W, names);
    return 0;
}