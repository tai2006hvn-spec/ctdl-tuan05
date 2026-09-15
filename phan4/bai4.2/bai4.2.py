def chong_nhau(h1, h2):
    return not (h1[2] <= h2[1] or h2[2] <= h1[1])

def chon_ket_thuc_som_nhat(acts):
    ds = sorted(acts, key=lambda x: (x[2], x[1]))
    chon = []
    het = -1
    for h in ds:
        if h[1] >= het:
            chon.append(h)
            het = h[2]
    return chon

def chon_bat_dau_som_nhat(acts):
    ds = sorted(acts, key=lambda x: (x[1], x[2]))
    chon = []
    het = -1
    for h in ds:
        if h[1] >= het:
            chon.append(h)
            het = h[2]
    return chon

def chon_ngan_nhat(acts):
    lai = list(acts)
    chon = []
    while lai:
        tot = lai[0]
        for q in lai[1:]:
            len_q = q[2] - q[1]
            len_tot = tot[2] - tot[1]
            if len_q < len_tot or (len_q == len_tot and q[2] < tot[2]):
                tot = q
        chon.append(tot)
        lai = [g for g in lai if not chong_nhau(tot, g)]
    chon.sort(key=lambda x: x[1])
    return chon

def chon_it_chong_lan_nhat(acts):
    lai = list(acts)
    chon = []
    while lai:
        tot = lai[0]
        for q in lai[1:]:
            bac_q = sum(1 for g in lai if g != q and chong_nhau(q, g))
            bac_tot = sum(1 for g in lai if g != tot and chong_nhau(tot, g))
            if bac_q < bac_tot or (bac_q == bac_tot and q[2] < tot[2]):
                tot = q
        chon.append(tot)
        lai = [g for g in lai if not chong_nhau(tot, g)]
    chon.sort(key=lambda x: x[1])
    return chon

def loi_giai_toi_uu(acts):
    ds = sorted(acts, key=lambda x: x[2])
    n = len(ds)
    f = [1] * n
    trace = [-1] * n
    for i in range(n):
        for j in range(i):
            if ds[j][2] <= ds[i][1]:
                if f[j] + 1 > f[i]:
                    f[i] = f[j] + 1
                    trace[i] = j
    max_idx = max(range(n), key=lambda i: f[i])
    best = []
    cur = max_idx
    while cur != -1:
        best.append(ds[cur])
        cur = trace[cur]
    best.reverse()
    return best

def main():
    activities = [
        ("H1", 1, 5),
        ("H2", 2, 5),
        ("H3", 2, 6),
        ("H4", 3, 4),
        ("H5", 4, 8),
        ("H6", 6, 9),
        ("H7", 8, 11),
        ("H8", 9, 14),
        ("H9", 11, 13),
        ("H10", 12, 15),
    ]

    res_kt = chon_ket_thuc_som_nhat(activities)
    res_bd = chon_bat_dau_som_nhat(activities)
    res_nn = chon_ngan_nhat(activities)
    res_cl = chon_it_chong_lan_nhat(activities)
    res_opt = loi_giai_toi_uu(activities)

    table = [
        ("Ket thuc som nhat", res_kt),
        ("Bat dau som nhat", res_bd),
        ("Ngan nhat", res_nn),
        ("It chong lan nhat", res_cl),
        ("So nhieu nhat that su", res_opt),
    ]

    print("=" * 80)
    print("BANG 4.2. BON TIEU CHI THAM LAM VA LOI GIAI TOI UU TREN BO MUOI HOAT DONG")
    print("=" * 80)
    header = f"{'Tieu chi':<24} | {'Cac hoat dong duoc chon':<28} | {'So HD':<6} | {'Dat toi uu'}"
    print(header)
    print("-" * 80)

    for name, res in table:
        act_names = "{" + ", ".join(x[0] for x in res) + "}"
        cnt = len(res)
        is_opt = "Co" if cnt == len(res_opt) else "Khong"
        if name == "So nhieu nhat that su":
            is_opt = "Toi uu"
        print(f"{name:<24} | {act_names:<28} | {cnt:<6} | {is_opt}")
    print("=" * 80)

if __name__ == "__main__":
    main()