LM = {
    "em":  {"hoc": 0.52, "di": 0.48},
    "hoc": {"bai": 0.40, "toan": 0.35, "ve": 0.25},
    "di":  {"cho": 0.58, "boi": 0.22, "ngu": 0.20}
}

def liet_ke_tat_ca_cau():
    tat_ca = []
    for w2, p2 in LM["em"].items():
        for w3, p3 in LM[w2].items():
            cau = f"em {w2} {w3}"
            diem = p2 * p3
            tat_ca.append((cau, diem))
    tat_ca.sort(key=lambda x: x[1], reverse=True)
    return tat_ca

def giai_ma_tham_lam():
    cau = ["em"]
    cur = "em"
    prob = 1.0
    for _ in range(2):
        next_words = LM[cur]
        best_w = max(next_words, key=lambda w: next_words[w])
        prob *= next_words[best_w]
        cau.append(best_w)
        cur = best_w
    return " ".join(cau), prob

def giai_ma_chum(k):
    chum = [(["em"], 1.0)]
    for _ in range(2):
        ung_vien = []
        for words, prob in chum:
            cur = words[-1]
            for next_w, p in LM[cur].items():
                ung_vien.append((words + [next_w], prob * p))
        ung_vien.sort(key=lambda x: x[1], reverse=True)
        chum = ung_vien[:k]
    best_words, best_prob = chum[0]
    return " ".join(best_words), best_prob

words = ["em", "hoc", "bai", "toan"]
tags = ["N", "V"]
pi = {"N": 0.6, "V": 0.4}
A = {
    "N": {"N": 0.35, "V": 0.65},
    "V": {"N": 0.70, "V": 0.30}
}
B = {
    "N": {"em": 0.35, "hoc": 0.10, "bai": 0.40, "toan": 0.30},
    "V": {"em": 0.05, "hoc": 0.45, "bai": 0.05, "toan": 0.02}
}

def viterbi(words, tags, pi, A, B):
    T = len(words)
    f = [{} for _ in range(T)]
    tu = [{} for _ in range(T)]
    
    for t in tags:
        f[0][t] = pi[t] * B[t][words[0]]
        tu[0][t] = "-"
        
    for i in range(1, T):
        for t in tags:
            best_val = -1.0
            best_prev = None
            for s in tags:
                val = f[i - 1][s] * A[s][t]
                if val > best_val:
                    best_val = val
                    best_prev = s
            f[i][t] = best_val * B[t][words[i]]
            tu[i][t] = best_prev
            
    cuoi = max(tags, key=lambda t: f[T - 1][t])
    max_prob = f[T - 1][cuoi]
    day_nhan = [cuoi]
    for i in range(T - 1, 0, -1):
        day_nhan.append(tu[i][day_nhan[-1]])
    day_nhan.reverse()
    return f, tu, day_nhan, max_prob

def vet_can_viterbi(words, tags, pi, A, B):
    best_seq, best_prob = None, -1.0
    for t1 in tags:
        for t2 in tags:
            for t3 in tags:
                for t4 in tags:
                    prob = (pi[t1] * B[t1][words[0]] *
                            A[t1][t2] * B[t2][words[1]] *
                            A[t2][t3] * B[t3][words[2]] *
                            A[t3][t4] * B[t4][words[3]])
                    if prob > best_prob:
                        best_prob, best_seq = prob, [t1, t2, t3, t4]
    return best_seq, best_prob

if __name__ == "__main__":
    ds_cau = liet_ke_tat_ca_cau()
    cau_tot, diem_tot = ds_cau[0]
    cau_tham_lam, diem_tham_lam = giai_ma_tham_lam()
    cau_chum_1, diem_chum_1 = giai_ma_chum(1)
    cau_chum_2, diem_chum_2 = giai_ma_chum(2)
    cau_chum_3, diem_chum_3 = giai_ma_chum(3)
    f, tu, day_nhan, prob_viterbi = viterbi(words, tags, pi, A, B)
    seq_vc, prob_vc = vet_can_viterbi(words, tags, pi, A, B)
    seq_str = " ".join(day_nhan)
    seq_vc_str = " ".join(seq_vc)
    
    print("=" * 80)
    print("BANG 4.3. BA THUAT TOAN GIAI MA TREN CUNG MOT MO HINH")
    print("=" * 80)
    print(f"{'Thuat toan':<26} | {'Ket qua tra ve':<18} | {'Diem / xac suat':<15} | Co toi uu?")
    print("-" * 80)
    print(f"{'Liet ke: cau tot nhat':<26} | {cau_tot:<18} | {diem_tot:<15.4f} | Tot nhat")
    print(f"{'Giai ma tham lam':<26} | {cau_tham_lam:<18} | {diem_tham_lam:<15.4f} | Khong")
    print(f"{'Giai ma theo chum, k = 1':<26} | {cau_chum_1:<18} | {diem_chum_1:<15.4f} | Khong")
    print(f"{'Giai ma theo chum, k = 2':<26} | {cau_chum_2:<18} | {diem_chum_2:<15.4f} | Co")
    print(f"{'Giai ma theo chum, k = 3':<26} | {cau_chum_3:<18} | {diem_chum_3:<15.4f} | Co")
    print(f"{'Viterbi (gan nhan)':<26} | {seq_str:<18} | {prob_viterbi:<15.6f} | Co")
    print("=" * 80)
    
    print("\n" + "=" * 80)
    print("BANG 4.4. LUOI VITERBI CUA CAU 'em hoc bai toan' (6 CHU SO THAP PHAN)")
    print("=" * 80)
    print(f"{'i':<3} | {'Tu w_i':<8} | {'f[i][N]':<12} | {'f[i][V]':<12} | {'Nhan truoc N':<14} | {'Nhan truoc V'}")
    print("-" * 80)
    for i in range(len(words)):
        p_n = tu[i]["N"] if tu[i]["N"] else "-"
        p_v = tu[i]["V"] if tu[i]["V"] else "-"
        print(f"{i+1:<3} | {words[i]:<8} | {f[i]['N']:<12.6f} | {f[i]['V']:<12.6f} | {p_n:<14} | {p_v}")
    print("=" * 80)
    
    print("\n--- KIEM CHUNG DOC LAP VOI VET CAN (2^4 = 16 DAY NHAN) ---")
    print(f"Viterbi: {seq_str} voi xac suat {prob_viterbi:.8f}")
    print(f"Vet can: {seq_vc_str} voi xac suat {prob_vc:.8f}")
    assert day_nhan == seq_vc
    print("=> KET QUA VITERBI KHOP VOI VET CAN 100%!")