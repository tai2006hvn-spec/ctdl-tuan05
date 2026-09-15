import random
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def chong_nhau(a, b):
    return not (a[1] <= b[0] or b[1] <= a[0])

def vet_can_hoat_dong(acts):
    """Vet can moi tap con 2^n bang bitmask"""
    n = len(acts)
    best_cnt = 0
    for mask in range(1 << n):
        subset = [acts[i] for i in range(n) if (mask >> i) & 1]
        valid = True
        for i in range(len(subset)):
            for j in range(i + 1, len(subset)):
                if chong_nhau(subset[i], subset[j]):
                    valid = False
                    break
            if not valid:
                break
        if valid and len(subset) > best_cnt:
            best_cnt = len(subset)
    return best_cnt

def qhd_hoat_dong(acts):
    """Quy hoach dong tren doan"""
    ds = sorted(acts, key=lambda x: x[1])
    n = len(ds)
    if n == 0:
        return 0
    f = [1] * n
    for i in range(n):
        for j in range(i):
            if ds[j][1] <= ds[i][0]:
                if f[j] + 1 > f[i]:
                    f[i] = f[j] + 1
    return max(f)

def tham_lam_ket_thuc_som(acts):
    """Tham lam ket thuc som nhat (luon toi uu)"""
    ds = sorted(acts, key=lambda x: (x[1], x[0]))
    cnt = 0
    het = -1
    for s, f in ds:
        if s >= het:
            cnt += 1
            het = f
    return cnt

def tham_lam_bat_dau_som(acts):
    """Tham lam bat dau som nhat (co the sai)"""
    ds = sorted(acts, key=lambda x: (x[0], x[1]))
    cnt = 0
    het = -1
    for s, f in ds:
        if s >= het:
            cnt += 1
            het = f
    return cnt

def tham_lam_ngan_nhat(acts):
    """Tham lam ngan nhat (co the sai)"""
    lai = list(acts)
    cnt = 0
    while lai:
        tot = min(lai, key=lambda x: (x[1] - x[0], x[1]))
        cnt += 1
        lai = [g for g in lai if not chong_nhau(tot, g)]
    return cnt

def run_tests():
    print("=" * 70)
    print("KIEM CHUNG DOC LAP BAI 4.2: CHON HOAT DONG (VET CAN vs QHD vs THAM LAM)")
    print("=" * 70)
    random.seed(42)
    total_tests = 30
    passed = 0
    bd_som_fails = 0
    ngan_nhat_fails = 0

    for test_id in range(1, total_tests + 1):
        n = random.randint(5, 12)
        acts = []
        for _ in range(n):
            s = random.randint(1, 25)
            f = s + random.randint(1, 12)
            acts.append((s, f))

        ans_bf = vet_can_hoat_dong(acts)
        ans_dp = qhd_hoat_dong(acts)
        ans_greedy_ef = tham_lam_ket_thuc_som(acts)

        assert ans_bf == ans_dp == ans_greedy_ef, f"Test {test_id} THAT BAI!"
        passed += 1

        if tham_lam_bat_dau_som(acts) != ans_bf:
            bd_som_fails += 1
        if tham_lam_ngan_nhat(acts) != ans_bf:
            ngan_nhat_fails += 1

    print(f"[OK] {passed}/{total_tests} test ngau nhien DAT 100% khop giua Vet can, QHD va Tham lam KT som.")
    print(f"[CANH BAO TIEU CHI SAI] Bat dau som that bai: {bd_som_fails}/{total_tests} test.")
    print(f"[CANH BAO TIEU CHI SAI] Ngan nhat that bai: {ngan_nhat_fails}/{total_tests} test.")
    print("   (chung minh cac tieu chi tham lam sai khac khong bao loi runtime nhung cho ket qua thieu hut).")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
