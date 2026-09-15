using Printf

LM = Dict(
"em"  => Dict("hoc" => 0.52, "di" => 0.48),
"hoc" => Dict("bai" => 0.40, "toan" => 0.35, "ve" => 0.25),
"di"  => Dict("cho" => 0.58, "boi" => 0.22, "ngu" => 0.20)
)

function liet_ke_tat_ca_cau()
cauthap = Tuple{String, Float64}[]
for (w2, p2) in LM["em"]
for (w3, p3) in LM[w2]
push!(cauthap, ("em $w2 $w3", p2 * p3))
end
end
sort!(cauthap, by = x -> x[2], rev = true)
return cauthap
end

function giai_ma_tham_lam()
cau = ["em"]; cur = "em"; prob = 1.0
for step in 1:2
nxt_dict = LM[cur]; best_w = ""; max_p = -1.0
for (w, p) in nxt_dict
if p > max_p; max_p = p; best_w = w; end
end
prob *= max_p; push!(cau, best_w); cur = best_w
end
return join(cau, " "), prob
end

function giai_ma_chum(k)
chum = [([ "em" ], 1.0)]
for step in 1:2
ung_vien = Tuple{Vector{String}, Float64}[]
for (w_list, p_val) in chum
cur = w_list[end]
if haskey(LM, cur)
for (nxt, p) in LM[cur]
push!(ung_vien, (vcat(w_list, [nxt]), p_val * p))
end
end
end
sort!(ung_vien, by = x -> x[2], rev = true)
chum = ung_vien[1:min(k, length(ung_vien))]
end
return join(chum[1][1], " "), chum[1][2]
end

words = ["em", "hoc", "bai", "toan"]
tags = ["N", "V"]
pi_dict = Dict("N" => 0.6, "V" => 0.4)
A = Dict("N" => Dict("N" => 0.35, "V" => 0.65), "V" => Dict("N" => 0.70, "V" => 0.30))
B = Dict("N" => Dict("em" => 0.35, "hoc" => 0.10, "bai" => 0.40, "toan" => 0.30),
"V" => Dict("em" => 0.05, "hoc" => 0.45, "bai" => 0.05, "toan" => 0.02))

function viterbi(words, tags, pi_dict, A, B)
T = length(words)
f = [Dict{String, Float64}() for _ in 1:T]
tu = [Dict{String, String}() for _ in 1:T]
for t in tags
f[1][t] = pi_dict[t] * B[t][words[1]]
tu[1][t] = "-"
end
for i in 2:T
for t in tags
best_val = -1.0; best_prev = ""
for s in tags
val = f[i - 1][s] * A[s][t]
if val > best_val; best_val = val; best_prev = s; end
end
f[i][t] = best_val * B[t][words[i]]
tu[i][t] = best_prev
end
end
cuoi = (f[T]["N"] >= f[T]["V"]) ? "N" : "V"
day_nhan = Vector{String}(undef, T)
day_nhan[T] = cuoi
for i in T:-1:2; day_nhan[i - 1] = tu[i][day_nhan[i]]; end
return f, tu, day_nhan, f[T][cuoi]
end

function vet_can_viterbi(words, tags, pi_dict, A, B)
best_seq = String[]
best_prob = -1.0
for t1 in tags
for t2 in tags
for t3 in tags
for t4 in tags
p = pi_dict[t1] * B[t1][words[1]] *
A[t1][t2] * B[t2][words[2]] *
A[t2][t3] * B[t3][words[3]] *
A[t3][t4] * B[t4][words[4]]
if p > best_prob
best_prob = p
best_seq = [t1, t2, t3, t4]
end
end
end
end
end
return best_seq, best_prob
end

ds_cau = liet_ke_tat_ca_cau()
cau_tot_nhat, diem_tot_nhat = ds_cau[1]
cau_tham_lam, diem_tham_lam = giai_ma_tham_lam()
cau_chum_1, diem_chum_1 = giai_ma_chum(1)
cau_chum_2, diem_chum_2 = giai_ma_chum(2)
cau_chum_3, diem_chum_3 = giai_ma_chum(3)

f, tu, day_nhan, prob_viterbi = viterbi(words, tags, pi_dict, A, B)
viterbi_seq = join(day_nhan, " ")
seq_vc, prob_vc = vet_can_viterbi(words, tags, pi_dict, A, B)
vc_seq = join(seq_vc, " ")

println("="^80)
println("BANG 4.3. BA THUAT TOAN GIAI MA TREN CUNG MOT MO HINH")
println("="^80)
@printf("%-26s | %-18s | %-15s | %s\n", "Thuat toan", "Ket qua tra ve", "Diem / xac suat", "Co toi uu?")
println("-"^80)
@printf("%-26s | %-18s | %-15.4f | Tot nhat\n", "Liet ke: cau tot nhat", cau_tot_nhat, diem_tot_nhat)
@printf("%-26s | %-18s | %-15.4f | Khong\n", "Giai ma tham lam", cau_tham_lam, diem_tham_lam)
@printf("%-26s | %-18s | %-15.4f | Khong\n", "Giai ma theo chum, k = 1", cau_chum_1, diem_chum_1)
@printf("%-26s | %-18s | %-15.4f | Co\n", "Giai ma theo chum, k = 2", cau_chum_2, diem_chum_2)
@printf("%-26s | %-18s | %-15.4f | Co\n", "Giai ma theo chum, k = 3", cau_chum_3, diem_chum_3)
@printf("%-26s | %-18s | %-15.6f | Co\n", "Viterbi (gan nhan)", viterbi_seq, prob_viterbi)
println("="^80)

println("\n" * "="^80)
println("BANG 4.4. LUOI VITERBI CUA CAU 'em hoc bai toan' (6 CHU SO THAP PHAN)")
println("="^80)
@printf("%-3s | %-8s | %-12s | %-12s | %-14s | %s\n", "i", "Tu w_i", "f[i][N]", "f[i][V]", "Nhan truoc N", "Nhan truoc V")
println("-"^80)
for i in 1:length(words)
@printf("%-3d | %-8s | %-12.6f | %-12.6f | %-14s | %s\n", i, words[i], f[i]["N"], f[i]["V"], tu[i]["N"], tu[i]["V"])
end
println("="^80)

println("\n--- KIEM CHUNG DOC LAP VOI VET CAN (2^4 = 16 DAY NHAN) ---")
@printf("Viterbi: %s voi xac suat %.8f\n", viterbi_seq, prob_viterbi)
@printf("Vet can: %s voi xac suat %.8f\n", vc_seq, prob_vc)
@assert day_nhan == seq_vc "Ket qua khong khop!"
println("=> KET QUA VITERBI KHOP VOI VET CAN 100%!")
