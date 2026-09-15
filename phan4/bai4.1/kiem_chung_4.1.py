import random
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def doi_tien_tham_lam(coins, S):
    coins = sorted(coins, reverse=True)
    res = []
    rem = S
    for c in coins:
        while rem >= c:
            res.append(c)
            rem -= c
    if rem != 0:
        return None, []
    return len(res), res

def doi_tien_qhd(coins, S):
    INF = 10**9
    f = [INF] * (S + 1)
    f[0] = 0
    for c in sorted(coins):
        for j in range(c, S + 1):
            if f[j - c] + 1 < f[j]:
                f[j] = f[j - c] + 1
    if f[S] >= INF:
        return None
    return f[S]

def doi_tien_vet_can(coins, S):
    """Vet can bang de quy co memoization tim so to it nhat"""
    memo = {}
    INF = 10**9
    def solve(rem):
        if rem == 0:
            return 0
        if rem < 0:
            return INF
        if rem in memo:
            return memo[rem]
        res = INF
        for c in coins:
            res = min(res, 1 + solve(rem - c))
        memo[rem] = res
        return res
    ans = solve(S)
    return ans if ans < INF else None

def run_tests():
    print("=" * 70)
    print("KIEM CHUNG DOC LAP BAI 4.1: DOI TIEN (VET CAN vs QUY HOACH DONG vs THAM LAM)")
    print("=" * 70)
    random.seed(42)
    total_tests = 30
    passed = 0
    greedy_fails = 0

    for test_id in range(1, total_tests + 1):
        # Sinh bo menh gia co chua so 1 de luon doi duoc tien
        k = random.randint(3, 5)
        coins = sorted(list({1} | {random.randint(2, 20) for _ in range(k)}))
        S = random.randint(10, 40)

        ans_dp = doi_tien_qhd(coins, S)
        ans_bf = doi_tien_vet_can(coins, S)

        assert ans_dp == ans_bf, f"Test {test_id} THAT BAI: QHD={ans_dp}, Vet can={ans_bf}"
        passed += 1

        ans_greedy, _ = doi_tien_tham_lam(coins, S)
        if ans_greedy != ans_dp:
            greedy_fails += 1

    print(f"[OK] {passed}/{total_tests} test ngau nhien DAT 100% khop giua Vet can va QHD.")
    print(f"[CANH BAO THAM LAM] Co {greedy_fails}/{total_tests} test Tham lam cho ket qua KHONG toi uu")
    print("   (chung minh tham lam doi tien sai ma hoan toan khong bao loi runtime).")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
