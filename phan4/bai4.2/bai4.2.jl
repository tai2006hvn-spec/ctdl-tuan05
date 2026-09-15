using Printf

struct Act
    name::String
    s::Int
    f::Int
end

function chong_nhau(a::Act, b::Act)
    return !(a.f <= b.s || b.f <= a.s)
end

function chon_ket_thuc_som_nhat(acts)
    ds = sort(acts, by = x -> (x.f, x.s))
    chon = Act[]
    het = -1
    for h in ds
        if h.s >= het
            push!(chon, h)
            het = h.f
        end
    end
    return chon
end

function chon_bat_dau_som_nhat(acts)
    ds = sort(acts, by = x -> (x.s, x.f))
    chon = Act[]
    het = -1
    for h in ds
        if h.s >= het
            push!(chon, h)
            het = h.f
        end
    end
    return chon
end

function chon_ngan_nhat(acts)
    lai = copy(acts)
    chon = Act[]
    while !isempty(lai)
        tot = lai[1]
        for i in 2:length(lai)
            q = lai[i]
            len_q = q.f - q.s
            len_tot = tot.f - tot.s
            if len_q < len_tot || (len_q == len_tot && q.f < tot.f)
                tot = q
            end
        end
        push!(chon, tot)
        lai = filter(g -> !chong_nhau(tot, g), lai)
    end
    sort!(chon, by = x -> x.s)
    return chon
end

function chon_it_chong_lan_nhat(acts)
    lai = copy(acts)
    chon = Act[]
    while !isempty(lai)
        tot = lai[1]
        dem_chong = h -> count(g -> g.name != h.name && chong_nhau(h, g), lai)
        for i in 2:length(lai)
            q = lai[i]
            bac_q = dem_chong(q)
            bac_tot = dem_chong(tot)
            if bac_q < bac_tot || (bac_q == bac_tot && q.f < tot.f)
                tot = q
            end
        end
        push!(chon, tot)
        lai = filter(g -> !chong_nhau(tot, g), lai)
    end
    sort!(chon, by = x -> x.s)
    return chon
end

function loi_giai_toi_uu(acts)
    ds = sort(acts, by = x -> x.f)
    n = length(ds)
    f = ones(Int, n)
    trace = fill(-1, n)
    for i in 1:n
        for j in 1:(i - 1)
            if ds[j].f <= ds[i].s
                if f[j] + 1 > f[i]
                    f[i] = f[j] + 1
                    trace[i] = j
                end
            end
        end
    end
    max_idx = argmax(f)
    best = Act[]
    cur = max_idx
    while cur != -1
        push!(best, ds[cur])
        cur = trace[cur]
    end
    reverse!(best)
    return best
end

function format_acts(acts)
    return "{" * join([h.name for h in acts], ", ") * "}"
end

function main()
    activities = [
        Act("H1", 1, 5),
        Act("H2", 2, 5),
        Act("H3", 2, 6),
        Act("H4", 3, 4),
        Act("H5", 4, 8),
        Act("H6", 6, 9),
        Act("H7", 8, 11),
        Act("H8", 9, 14),
        Act("H9", 11, 13),
        Act("H10", 12, 15)
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
        ("So nhieu nhat that su", res_opt)
    ]

    println("="^80)
    println("BANG 4.2. BON TIEU CHI THAM LAM VA LOI GIAI TOI UU TREN BO MUOI HOAT DONG")
    println("="^80)
    @printf("%-24s | %-28s | %-6s | %s\n", 
            "Tieu chi", "Cac hoat dong duoc chon", "So HD", "Dat toi uu")
    println("-"^80)

    for (name, res) in table
        cnt = length(res)
        is_opt = (cnt == length(res_opt)) ? "Co" : "Khong"
        if name == "So nhieu nhat that su"
            is_opt = "Toi uu"
        end
        @printf("%-24s | %-28s | %-6d | %s\n",
                name, format_acts(res), cnt, is_opt)
    end
    println("="^80)
end

main()