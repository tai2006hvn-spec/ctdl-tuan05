def cai_tui(w, v, W, names=None):
    n = len(w)
    if names is None:
        names = [f"DV{i+1}" for i in range(n)]
        
    f = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(W + 1):
            f[i][j] = f[i - 1][j]  
            if w[i - 1] <= j:      
                f[i][j] = max(f[i][j], f[i - 1][j - w[i - 1]] + v[i - 1])
                
    print("--- BANG QUY HOACH DONG f[i][j] ---")
    header = "f[i][j]\t" + "\t".join(f"{j}" for j in range(W + 1))
    print(header)
    row_labels = ["i=0"] + [f"i={i+1} ({names[i]})" for i in range(n)]
    for i in range(n + 1):
        print(f"{row_labels[i]:<10}\t" + "\t".join(str(f[i][j]) for j in range(W + 1)))
        
    chon = []
    j = W
    for i in range(n, 0, -1):
        if f[i][j] != f[i - 1][j]:
            chon.append(i)
            j -= w[i - 1]
    chon.reverse()
    
    chosen_names = [names[i - 1] for i in chon]
    total_w = sum(w[i - 1] for i in chon)
    max_v = f[n][W]
    
    print("\n--- KET QUA ---")
    print(f"Gia tri lon nhat f[{n}][{W}]: {max_v}")
    print(f"Tap do vat duoc chon: {', '.join(chosen_names)} (chi so: {chon})")
    print(f"Tong trong luong: {total_w} / {W}")
    return max_v, chon

if __name__ == "__main__":
    w = [2, 3, 4, 5, 7]
    v = [3, 7, 9, 12, 16]
    names = ['A', 'B', 'C', 'D', 'E']
    W = 11
    cai_tui(w, v, W, names)