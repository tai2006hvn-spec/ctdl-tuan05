import random
import sys

# Đảm bảo in tiếng Việt chuẩn trên mọi console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def cai_tui_vet_can(w, v, W):
    """Vet can moi tap con 2^n do vat"""
    n = len(w)
    best_val = 0
    best_comb = []
    for mask in range(1 << n):
        cur_w = sum(w[i] for i in range(n) if (mask >> i) & 1)
        cur_v = sum(v[i] for i in range(n) if (mask >> i) & 1)
        if cur_w <= W and cur_v > best_val:
            best_val = cur_v
            best_comb = [i for i in range(n) if (mask >> i) & 1]
    return best_val, best_comb

def cai_tui_qhd_2d(w, v, W):
    """Quy hoach dong bang 2 chieu f[i][j]"""
    n = len(w)
    f = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(W + 1):
            f[i][j] = f[i - 1][j]
            if w[i - 1] <= j:
                f[i][j] = max(f[i][j], f[i - 1][j - w[i - 1]] + v[i - 1])
    return f[n][W]

def cai_tui_qhd_1d_dung(w, v, W):
    """QHD 1 chieu duyet j GIAM DAN (chuan cho Cai tui 0/1)"""
    f = [0] * (W + 1)
    for i in range(len(w)):
        for j in range(W, w[i] - 1, -1):
            f[j] = max(f[j], f[j - w[i]] + v[i])
    return f[W]

def cai_tui_qhd_1d_sai_chieu(w, v, W):
    """QHD 1 chieu duyet j TANG DAN (sai chieu -> thanh Cai tui khong gioi han)"""
    f = [0] * (W + 1)
    for i in range(len(w)):
        for j in range(w[i], W + 1):
            f[j] = max(f[j], f[j - w[i]] + v[i])
    return f[W]

def run_tests():
    print("=" * 70)
    print("KIEM CHUNG DOC LAP BAI TOAN CAI TUI 0/1 (VET CAN vs QUY HOACH DONG)")
    print("=" * 70)
    random.seed(42)
    total_tests = 30
    passed = 0
    sai_chieu_detected = 0

    for test_id in range(1, total_tests + 1):
        n = random.randint(5, 12)
        W = random.randint(15, 35)
        w = [random.randint(1, 10) for _ in range(n)]
        v = [random.randint(1, 20) for _ in range(n)]

        val_bf, _ = cai_tui_vet_can(w, v, W)
        val_dp2d = cai_tui_qhd_2d(w, v, W)
        val_dp1d_dung = cai_tui_qhd_1d_dung(w, v, W)
        val_dp1d_sai = cai_tui_qhd_1d_sai_chieu(w, v, W)

        assert val_bf == val_dp2d == val_dp1d_dung, f"Test {test_id} THAT BAI!"
        passed += 1

        if val_dp1d_sai != val_bf:
            sai_chieu_detected += 1

    print(f"[OK] {passed}/{total_tests} test ngau nhien DAT 100% khop tuyet doi giua Vet can va QHD.")
    print(f"[CANH BAO DUYET SAI CHIEU] Co {sai_chieu_detected}/{total_tests} truong hop duyet j tang dan cho ket qua sai")
    print("   (nghiem bi lay lap lai do vat nhung chuong trinh hoan toan khong bao loi runtime).")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
