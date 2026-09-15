import random
import itertools
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def viterbi(words, tags, pi, A, B):
    T = len(words)
    f = [{} for _ in range(T)]
    tu = [{} for _ in range(T)]
    for t in tags:
        f[0][t] = pi[t] * B[t].get(words[0], 0.0)
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
            f[i][t] = best_val * B[t].get(words[i], 0.0)
            tu[i][t] = best_prev
    cuoi = max(tags, key=lambda t: f[T - 1][t])
    max_prob = f[T - 1][cuoi]
    day_nhan = [cuoi]
    for i in range(T - 1, 0, -1):
        day_nhan.append(tu[i][day_nhan[-1]])
    day_nhan.reverse()
    return day_nhan, max_prob

def vet_can_viterbi(words, tags, pi, A, B):
    T = len(words)
    best_seq = None
    best_prob = -1.0
    for seq in itertools.product(tags, repeat=T):
        prob = pi[seq[0]] * B[seq[0]].get(words[0], 0.0)
        for i in range(1, T):
            prob *= A[seq[i - 1]][seq[i]] * B[seq[i]].get(words[i], 0.0)
        if prob > best_prob:
            best_prob = prob
            best_seq = list(seq)
    return best_seq, best_prob

def run_tests():
    print("=" * 70)
    print("KIEM CHUNG DOC LAP BAI 4.3: VITERBI vs VET CAN (16 DAY NHAN & NGAU NHIEN)")
    print("=" * 70)

    # 1. Kiem chung tren du lieu chuan muc D
    words = ["em", "hoc", "bai", "toan"]
    tags = ["N", "V"]
    pi = {"N": 0.6, "V": 0.4}
    A = {"N": {"N": 0.35, "V": 0.65}, "V": {"N": 0.70, "V": 0.30}}
    B = {
        "N": {"em": 0.35, "hoc": 0.10, "bai": 0.40, "toan": 0.30},
        "V": {"em": 0.05, "hoc": 0.45, "bai": 0.05, "toan": 0.02}
    }

    seq_vit, p_vit = viterbi(words, tags, pi, A, B)
    seq_vc, p_vc = vet_can_viterbi(words, tags, pi, A, B)
    assert seq_vit == seq_vc, "Du lieu chuan muc D THAT BAI!"
    print(f"[TEST MUC D] Viterbi = {' '.join(seq_vit)} ({p_vit:.6f}) khop 100% voi Vet can.")

    # 2. Kiem chung tren 30 mo hinh HMM sinh ngau nhien
    random.seed(42)
    total_tests = 30
    passed = 0
    vocab = ["w1", "w2", "w3", "w4", "w5"]

    for test_id in range(1, total_tests + 1):
        T = random.randint(3, 5)
        sent = [random.choice(vocab) for _ in range(T)]
        p_N = random.uniform(0.1, 0.9)
        pi_rand = {"N": p_N, "V": 1.0 - p_N}

        p_NN = random.uniform(0.1, 0.9)
        p_VN = random.uniform(0.1, 0.9)
        A_rand = {
            "N": {"N": p_NN, "V": 1.0 - p_NN},
            "V": {"N": p_VN, "V": 1.0 - p_VN}
        }

        def gen_B():
            weights = [random.uniform(0.1, 1.0) for _ in vocab]
            total = sum(weights)
            return {w: weights[i] / total for i, w in enumerate(vocab)}

        B_rand = {"N": gen_B(), "V": gen_B()}

        res_vit, p_vit_r = viterbi(sent, tags, pi_rand, A_rand, B_rand)
        res_vc, p_vc_r = vet_can_viterbi(sent, tags, pi_rand, A_rand, B_rand)

        assert abs(p_vit_r - p_vc_r) < 1e-9 and res_vit == res_vc, f"Test ngau nhien {test_id} THAT BAI!"
        passed += 1

    print(f"[OK] {passed}/{total_tests} test HMM ngau nhien DAT 100% khop tuyet doi.")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
