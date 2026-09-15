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
    vet = [-1] * (S + 1)
    f[0] = 0
    
    for c in sorted(coins):
        for j in range(c, S + 1):
            if f[j - c] + 1 < f[j]:
                f[j] = f[j - c] + 1
                vet[j] = c
                
    if f[S] >= INF:
        return None, []
        
    res = []
    cur = S
    while cur > 0:
        c = vet[cur]
        res.append(c)
        cur -= c
    return f[S], sorted(res, reverse=True)

def main():
    datasets = [
        (1, [1, 4, 6, 9], 12),
        (2, [1, 5, 10, 20, 50], 85),
        (3, [1, 3, 7, 12], 20),
        (4, [1, 2, 5, 10], 38),
        (5, [1, 6, 10], 12),
        (6, [1, 4, 5, 15, 20], 23),
    ]

    print("=" * 80)
    print("BANG 4.1. THAM LAM SO VOI QUY HOACH DONG TREN SAU BO MENH GIA")
    print("=" * 80)
    header = f"{'Bo':<4} | {'TL (to)':<8} | {'Cach tra tham lam':<22} | {'QHD (to)':<8} | {'Cach tra toi uu':<20} | {'Tham lam dung?'}"
    print(header)
    print("-" * 80)

    for bo_id, coins, S in datasets:
        cnt_g, way_g = doi_tien_tham_lam(coins, S)
        cnt_dp, way_dp = doi_tien_qhd(coins, S)
        is_correct = "Dung" if cnt_g == cnt_dp else "Sai"
        
        str_g = " + ".join(map(str, way_g))
        str_dp = " + ".join(map(str, way_dp))
        print(f"{bo_id:<4} | {cnt_g:<8} | {str_g:<22} | {cnt_dp:<8} | {str_dp:<20} | {is_correct}")
    print("=" * 80)

if __name__ == "__main__":
    main()