using Printf

function doi_tien_tham_lam(coins, S)
    c_sorted = sort(coins, rev = true)
    res = Int[]
    rem = S
    for c in c_sorted
        while rem >= c
            push!(res, c)
            rem -= c
        end
    end
    if rem != 0
        return -1, Int[]
    end
    return length(res), res
end

function doi_tien_qhd(coins, S)
    INF = 1_000_000_000
    f = fill(INF, S + 1)
    vet = fill(-1, S + 1)
    f[0 + 1] = 0
    
    for c in sort(coins)
        for j in c:S
            if f[j - c + 1] + 1 < f[j + 1]
                f[j + 1] = f[j - c + 1] + 1
                vet[j + 1] = c
            end
        end
    end
    
    if f[S + 1] >= INF
        return -1, Int[]
    end
    
    res = Int[]
    cur = S
    while cur > 0
        c = vet[cur + 1]
        push!(res, c)
        cur -= c
    end
    return f[S + 1], sort(res, rev = true)
end

function main()
    datasets = [
        (1, [1, 4, 6, 9], 12),
        (2, [1, 5, 10, 20, 50], 85),
        (3, [1, 3, 7, 12], 20),
        (4, [1, 2, 5, 10], 38),
        (5, [1, 6, 10], 12),
        (6, [1, 4, 5, 15, 20], 23)
    ]

    println("="^80)
    println("BANG 4.1. THAM LAM SO VOI QUY HOACH DONG TREN SAU BO MENH GIA")
    println("="^80)
    @printf("%-4s | %-8s | %-22s | %-8s | %-20s | %s\n", 
            "Bo", "TL (to)", "Cach tra tham lam", "QHD (to)", "Cach tra toi uu", "Tham lam dung?")
    println("-"^80)

    for (bo_id, coins, S) in datasets
        cnt_g, way_g = doi_tien_tham_lam(coins, S)
        cnt_dp, way_dp = doi_tien_qhd(coins, S)
        is_correct = (cnt_g == cnt_dp) ? "Dung" : "Sai"
        
        str_g = join(string.(way_g), " + ")
        str_dp = join(string.(way_dp), " + ")
        
        @printf("%-4d | %-8d | %-22s | %-8d | %-20s | %s\n",
                bo_id, cnt_g, str_g, cnt_dp, str_dp, is_correct)
    end
    println("="^80)
end

main()