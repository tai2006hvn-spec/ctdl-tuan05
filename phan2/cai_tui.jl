using Printf

function cai_tui(w, v, W, names)
    n = length(w)
    f = zeros(Int, n + 1, W + 1)
    
    for i in 1:n
        for j in 0:W
            f[i + 1, j + 1] = f[i, j + 1] 
            if w[i] <= j
                f[i + 1, j + 1] = max(f[i + 1, j + 1], f[i, j - w[i] + 1] + v[i]) 
            end
        end
    end
    
    println("--- BANG QUY HOACH DONG f[i][j] ---")
    @printf("%-12s", "f[i][j]")
    for j in 0:W
        @printf("%4d", j)
    end
    println()
    
    @printf("%-12s", "i=0")
    for j in 0:W
        @printf("%4d", f[1, j + 1])
    end
    println()
    
    for i in 1:n
        label = @sprintf("i=%d (%s)", i, names[i])
        @printf("%-12s", label)
        for j in 0:W
            @printf("%4d", f[i + 1, j + 1])
        end
        println()
    end
    
    chon = Int[]
    j = W
    for i in n:-1:1
        if f[i + 1, j + 1] != f[i, j + 1]
            push!(chon, i)
            j -= w[i]
        end
    end
    reverse!(chon)
    
    chosen_names = [names[i] for i in chon]
    total_w = sum(w[i] for i in chon)
    max_v = f[n + 1, W + 1]
    
    println("\n--- KET QUA ---")
    println("Gia tri lon nhat f[$n][$W]: $max_v")
    print("Tap do vat duoc chon: ", join(chosen_names, ", "))
    println(" (chi so: ", join(chon, ", "), ")")
    println("Tong trong luong: $total_w / $W")
    
    return max_v, chon
end

w = [2, 3, 4, 5, 7]
v = [3, 7, 9, 12, 16]
names = ["A", "B", "C", "D", "E"]
W = 11

cai_tui(w, v, W, names)