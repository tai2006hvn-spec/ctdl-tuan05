# BÁO CÁO BÀI TẬP VỀ NHÀ CHƯƠNG 04: CÁC MÔ HÌNH THUẬT TOÁN
### Học phần: Cấu trúc Dữ liệu và Giải thuật (INT1306)
**Học viện Công nghệ Bưu chính Viễn thông (PTIT)**  
**Khoa Công nghệ Thông tin**

---

## 👨‍🎓 Thông tin sinh viên
- **Họ và tên:** Phạm Anh Tài
- **Mã số sinh viên (MSSV):** N24DCDT081
- **Lớp / Nhóm học phần:** D24CQDT01-N — Nhóm 3
- **Kho lưu trữ GitHub:** [https://github.com/tai2006hvn-spec/ctdl-tuan05](https://github.com/tai2006hvn-spec/ctdl-tuan05)

---

## 📌 Giới thiệu tổng quan
Dự án bao gồm mã nguồn cài đặt và kiểm thử cho các bài toán thuộc **Chương 04: Các mô hình thuật toán** (Quy hoạch động, Tham lam, Chia để trị). Toàn bộ các bài lập trình đều được triển khai đồng thời trên **3 ngôn ngữ: Python, C++ và Julia**, đảm bảo tính chuẩn xác, đồng nhất về kết quả và tuân thủ tuyệt đối quy định của bộ dữ liệu chuẩn.

Bên cạnh mã nguồn chính, mỗi bài toán đều tích hợp **chương trình kiểm chứng độc lập** (sử dụng thuật toán Vét cạn hoặc Quy hoạch động đối chiếu) chạy trên dữ liệu ngẫu nhiên để phát hiện các bẫy thuật toán nguy hiểm (tham lam không tối ưu, duyệt mảng quy hoạch động sai chiều).

---

## 📂 Cấu trúc thư mục mã nguồn

```text
ctdl-tuan05/
├── README.md                          # Hướng dẫn chi tiết cách chạy từng ngôn ngữ & báo cáo
├── phan2/                             # Phần 2: Bài toán Cái túi 0/1 (Knapsack 0/1)
│   ├── cai_tui.py                     # Cài đặt Quy hoạch động trên Python
│   ├── cai_tui.cpp                    # Cài đặt Quy hoạch động trên C++
│   ├── cai_tui.jl                     # Cài đặt Quy hoạch động trên Julia
│   ├── cai_tui.exe                    # File thực thi C++ biên dịch sẵn
│   └── kiem_chung_cai_tui.py          # Kiểm chứng độc lập (Vét cạn vs QHD & Bẫy duyệt sai chiều)
└── phan4/                             # Phần 4: Ba bài toán ứng dụng
    ├── bai4.1/                        # Bài 4.1: Đổi tiền (Tham lam vs Quy hoạch động)
    │   ├── bai4.1.py                  # Cài đặt trên Python
    │   ├── bai4.1.cpp                 # Cài đặt trên C++
    │   ├── bai4.1.jl                  # Cài đặt trên Julia
    │   ├── bai4.1.exe                 # File thực thi C++ biên dịch sẵn
    │   └── kiem_chung_4.1.py          # Kiểm chứng độc lập ngẫu nhiên (Vét cạn vs QHD vs Tham lam)
    ├── bai4.2/                        # Bài 4.2: Chọn hoạt động (4 tiêu chí Tham lam vs Tối ưu)
    │   ├── bai4.2.py                  # Cài đặt trên Python
    │   ├── bai4.2.cpp                 # Cài đặt trên C++
    │   ├── bai4.2.jl                  # Cài đặt trên Julia
    │   ├── bai4.2.exe                 # File thực thi C++ biên dịch sẵn
    │   └── kiem_chung_4.2.py          # Kiểm chứng độc lập ngẫu nhiên (Vét cạn vs QHD vs Tham lam)
    └── bai4.3/                        # Bài 4.3: Giải mã mô hình ngôn ngữ & Thuật toán Viterbi
        ├── bai4.3.py                  # Cài đặt trên Python
        ├── bai4.3.cpp                 # Cài đặt trên C++
        ├── bai4.3.jl                  # Cài đặt trên Julia
        ├── bai4.3.exe                 # File thực thi C++ biên dịch sẵn
        └── kiem_chung_4.3.py          # Kiểm chứng độc lập Viterbi vs Vét cạn (16 dãy nhãn & HMM ngẫu nhiên)
```

---

## 🛠️ Yêu cầu môi trường & Cài đặt

1. **Python:** Phiên bản `>= 3.8` (đã kiểm thử thành công trên Python 3.14.7). Không yêu cầu thư viện bên ngoài (dùng chuẩn thư viện tích hợp `sys`, `random`, `itertools`).
2. **C++ Compiler:** Trình biên dịch hỗ trợ chuẩn `C++17` trở lên (g++ / MinGW / Clang / MSVC - đã kiểm thử trên GCC 16.1.0).
3. **Julia:** Phiên bản `>= 1.6` (đã kiểm thử thành công trên Julia 1.12.6). Dùng module chuẩn `Printf`.

---

## 🚀 Hướng dẫn chi tiết cách chạy từng bài trên từng ngôn ngữ

> **Lưu ý:** Mọi lệnh bên dưới được thực hiện từ thư mục gốc của dự án (`ctdl-tuan05`).

---

### 1. Phần 2 — Bài toán Cái túi 0/1 (Knapsack 0/1)
Bộ đồ vật chuẩn mục A: $n = 5$, $w = [2, 3, 4, 5, 7]$, $v = [3, 7, 9, 12, 16]$, sức chứa $W = 11$.

- **Chạy bản Python:**
  ```bash
  python phan2/cai_tui.py
  ```
- **Biên dịch & chạy bản C++:**
  ```bash
  g++ -O2 -std=c++17 phan2/cai_tui.cpp -o phan2/cai_tui
  # Trên Windows:
  .\phan2\cai_tui.exe
  # Trên Linux/macOS:
  ./phan2/cai_tui
  ```
- **Chạy bản Julia:**
  ```bash
  julia phan2/cai_tui.jl
  ```
- **Chương trình kiểm chứng độc lập (Vét cạn $2^n$ vs QHD & cảnh báo duyệt sai chiều):**
  ```bash
  python phan2/kiem_chung_cai_tui.py
  ```

---

### 2. Bài 4.1 — Đổi tiền: Tham lam so với Quy hoạch động
Kiểm thử trên cả 6 bộ mệnh giá chuẩn ở mục B để phát hiện các bộ mệnh giá mà tham lam thất bại.

- **Chạy bản Python:**
  ```bash
  python phan4/bai4.1/bai4.1.py
  ```
- **Biên dịch & chạy bản C++:**
  ```bash
  g++ -O2 -std=c++17 phan4/bai4.1/bai4.1.cpp -o phan4/bai4.1/bai4.1
  # Trên Windows:
  .\phan4\bai4.1\bai4.1.exe
  # Trên Linux/macOS:
  ./phan4/bai4.1/bai4.1
  ```
- **Chạy bản Julia:**
  ```bash
  julia phan4/bai4.1/bai4.1.jl
  ```
- **Chương trình kiểm chứng độc lập (Vét cạn đệ quy vs QHD vs Tham lam trên 30 bộ dữ liệu ngẫu nhiên):**
  ```bash
  python phan4/bai4.1/kiem_chung_4.1.py
  ```

---

### 3. Bài 4.2 — Chọn hoạt động: Bốn tiêu chí trên cùng một bộ dữ liệu
So sánh 4 tiêu chí tham lam (*Kết thúc sớm nhất*, *Bắt đầu sớm nhất*, *Ngắn nhất*, *Ít chồng lấn nhất*) với nghiệm tối ưu toàn cục (QHD) trên 10 hoạt động chuẩn ở mục C.

- **Chạy bản Python:**
  ```bash
  python phan4/bai4.2/bai4.2.py
  ```
- **Biên dịch & chạy bản C++:**
  ```bash
  g++ -O2 -std=c++17 phan4/bai4.2/bai4.2.cpp -o phan4/bai4.2/bai4.2
  # Trên Windows:
  .\phan4\bai4.2\bai4.2.exe
  # Trên Linux/macOS:
  ./phan4/bai4.2/bai4.2
  ```
- **Chạy bản Julia:**
  ```bash
  julia phan4/bai4.2/bai4.2.jl
  ```
- **Chương trình kiểm chứng độc lập (Vét cạn $2^n$ bitmask vs QHD vs Tham lam trên 30 tập hoạt động ngẫu nhiên):**
  ```bash
  python phan4/bai4.2/kiem_chung_4.2.py
  ```

---

### 4. Bài 4.3 — Ba thuật toán giải mã của mô hình ngôn ngữ & Viterbi
So sánh *Liệt kê*, *Giải mã tham lam*, *Giải mã theo chùm* ($k = 1, 2, 3$) và thuật toán *Viterbi* gán nhãn từ loại cho câu *"em học bài toán"*, đối chiếu vét cạn $2^4 = 16$ dãy nhãn.

- **Chạy bản Python:**
  ```bash
  python phan4/bai4.3/bai4.3.py
  ```
- **Biên dịch & chạy bản C++:**
  ```bash
  g++ -O2 -std=c++17 phan4/bai4.3/bai4.3.cpp -o phan4/bai4.3/bai4.3
  # Trên Windows:
  .\phan4\bai4.3\bai4.3.exe
  # Trên Linux/macOS:
  ./phan4/bai4.3/bai4.3
  ```
- **Chạy bản Julia:**
  ```bash
  julia phan4/bai4.3/bai4.3.jl
  ```
- **Chương trình kiểm chứng độc lập (Viterbi vs Vét cạn toàn bộ dãy nhãn trên dữ liệu chuẩn & 30 mô hình HMM ngẫu nhiên):**
  ```bash
  python phan4/bai4.3/kiem_chung_4.3.py
  ```

---

## ⚡ Lệnh chạy kiểm thử nhanh toàn bộ (All-in-One Command)

### Trên Windows PowerShell:
```powershell
Write-Host "=== 1. PHAN 2: CAI TUI ===" -ForegroundColor Cyan
python phan2/cai_tui.py
julia phan2/cai_tui.jl
.\phan2\cai_tui.exe
python phan2/kiem_chung_cai_tui.py

Write-Host "=== 2. PHAN 4: BAI 4.1 ===" -ForegroundColor Cyan
python phan4/bai4.1/bai4.1.py
julia phan4/bai4.1/bai4.1.jl
.\phan4\bai4.1\bai4.1.exe
python phan4/bai4.1/kiem_chung_4.1.py

Write-Host "=== 3. PHAN 4: BAI 4.2 ===" -ForegroundColor Cyan
python phan4/bai4.2/bai4.2.py
julia phan4/bai4.2/bai4.2.jl
.\phan4\bai4.2\bai4.2.exe
python phan4/bai4.2/kiem_chung_4.2.py

Write-Host "=== 4. PHAN 4: BAI 4.3 ===" -ForegroundColor Cyan
python phan4/bai4.3/bai4.3.py
julia phan4/bai4.3/bai4.3.jl
.\phan4\bai4.3\bai4.3.exe
python phan4/bai4.3/kiem_chung_4.3.py
```

---

## 📊 Bảng tổng hợp kết quả thực nghiệm

### 1. Bảng 2.1 — Kết quả bài toán Cái túi 0/1 ($W = 11$)
| Đại lượng | Giá trị tìm được |
| :--- | :--- |
| **Giá trị lớn nhất $f[5][11]$** | **25** |
| **Tập đồ vật được chọn** | **$\{C, E\}$** (đồ vật thứ 3 và thứ 5) |
| **Tổng trọng lượng** | $4 + 7 = \mathbf{11} \le 11$ |
| **Số ô của bảng $f$** | $(5 + 1) \times (11 + 1) = \mathbf{72}$ ô |
| **Ô đầu tiên trên đường truy vết có $f[i][j] \ne f[i-1][j]$** | $f[5][11]$ (do $f[5][11] = 25 \ne f[4][11] = 24$) |

---

### 2. Bảng 4.1 — Đổi tiền: Tham lam so với Quy hoạch động
| Bộ | Mệnh giá | Số tiền $S$ | Tham lam (số tờ) | Cách trả tham lam | QHD (số tờ) | Cách trả tối ưu | Tham lam đúng? |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- | :---: |
| **1** | $\{1, 4, 6, 9\}$ | 12 | 4 | $9 + 1 + 1 + 1$ | **2** | $6 + 6$ | ❌ **Sai** |
| **2** | $\{1, 5, 10, 20, 50\}$ | 85 | 4 | $50 + 20 + 10 + 5$ | **4** | $50 + 20 + 10 + 5$ | ✔️ **Đúng** |
| **3** | $\{1, 3, 7, 12\}$ | 20 | 3 | $12 + 7 + 1$ | **3** | $12 + 7 + 1$ | ✔️ **Đúng** |
| **4** | $\{1, 2, 5, 10\}$ | 38 | 6 | $10 + 10 + 10 + 5 + 2 + 1$ | **6** | $10 + 10 + 10 + 5 + 2 + 1$ | ✔️ **Đúng** |
| **5** | $\{1, 6, 10\}$ | 12 | 3 | $10 + 1 + 1$ | **2** | $6 + 6$ | ❌ **Sai** |
| **6** | $\{1, 4, 5, 15, 20\}$ | 23 | 4 | $20 + 1 + 1 + 1$ | **3** | $15 + 4 + 4$ | ❌ **Sai** |

---

### 3. Bảng 4.2 — Chọn hoạt động: 4 tiêu chí tham lam trên 10 hoạt động
| Tiêu chí | Các hoạt động được chọn | Số HĐ | Đạt tối ưu? |
| :--- | :--- | :---: | :---: |
| **Kết thúc sớm nhất** | **$\{H4, H5, H7, H9\}$** | **4** | ✔️ **Có (Tối ưu)** |
| **Bắt đầu sớm nhất** | $\{H1, H6, H8\}$ | 3 | ❌ Không |
| **Ngắn nhất** | $\{H4, H6, H9\}$ | 3 | ❌ Không |
| **Ít chồng lấn nhất** | $\{H4, H6, H9\}$ | 3 | ❌ Không |
| **Số nhiều nhất thật sự (QHD)** | **$\{H4, H5, H7, H9\}$** | **4** | 🌟 **Tối ưu toàn cục** |

---

### 4. Bảng 4.3 — Ba thuật toán giải mã của mô hình ngôn ngữ
| Thuật toán | Kết quả trả về | Điểm / Xác suất | Có tối ưu? |
| :--- | :--- | :---: | :---: |
| **Liệt kê câu tốt nhất** | `em đi chợ` | **0,2784** | 🌟 Tốt nhất |
| **Giải mã tham lam** | `em học bài` | 0,2080 | ❌ Không |
| **Giải mã theo chùm ($k = 1$)** | `em học bài` | 0,2080 | ❌ Không |
| **Giải mã theo chùm ($k = 2$)** | `em đi chợ` | **0,2784** | ✔️ Có |
| **Giải mã theo chùm ($k = 3$)** | `em đi chợ` | **0,2784** | ✔️ Có |
| **Viterbi (gán nhãn câu "em học bài toán")** | **`N V N N`** | **0,001806** | ✔️ **Có (100% khớp Vét cạn)** |

---

## 🔍 Cơ chế kiểm chứng độc lập & Cảnh báo bẫy thuật toán (Yêu cầu bắt buộc)

Theo quy định bắt buộc của Chương 04, các thuật toán Tham lam và Quy hoạch động thường mắc phải những lỗi logic rất tinh vi: **chương trình chạy bình thường, hoàn toàn không báo lỗi runtime nhưng âm thầm trả về kết quả sai**. 

Dự án đã tích hợp các chương trình kiểm chứng độc lập để phát hiện và làm sáng tỏ các bẫy này:

1. **Bẫy duyệt sai chiều trong Cái túi 1 chiều (`kiem_chung_cai_tui.py`):**
   - Khi tối ưu không gian mảng 1 chiều $f[j]$, bắt buộc phải duyệt $j$ **giảm dần** từ $W$ về $w_i$ để đảm bảo mỗi đồ vật chỉ được chọn tối đa 1 lần.
   - Nếu duyệt $j$ **tăng dần**, ô $f[j - w_i]$ đã bị ghi đè bởi chính đồ vật $i$ trước đó, khiến đồ vật $i$ bị lấy nhiều lần. Thuật toán âm thầm chuyển sang giải bài toán *Cái túi không giới hạn* (Unbounded Knapsack) mà không hề có cảnh báo lỗi.
   - Kết quả kiểm chứng ngẫu nhiên cho thấy 100% trường hợp duyệt tăng dần đều bị sai lệch giá trị so với nghiệm 0/1 của Vét cạn.

2. **Bẫy tham lam đổi tiền (`kiem_chung_4.1.py`):**
   - Thuật toán tham lam luôn chọn tờ tiền lớn nhất chỉ đúng trên hệ mệnh giá chuẩn (*Canonical Coin System*).
   - Trên các bộ mệnh giá tùy ý, tham lam dễ dàng bị "mắc kẹt" tại cực trị địa phương (ví dụ ở Bộ 1: chọn tờ 9 dẫn đến phải trả thêm ba tờ 1 = 4 tờ, trong khi $6 + 6 = 2$ tờ).
   - Kiểm chứng trên 30 bộ dữ liệu ngẫu nhiên cho thấy tỷ lệ tham lam trả về kết quả kém tối ưu xuất hiện thường xuyên dù chương trình kết thúc êm thấm.

3. **Bẫy chọn hoạt động sai tiêu chí (`kiem_chung_4.2.py`):**
   - Tiêu chí "Bắt đầu sớm nhất" bị bẫy bởi các hoạt động kéo dài chiếm dụng phòng học, chặn mất nhiều hoạt động ngắn hơn diễn ra liên tiếp.
   - Tiêu chí "Ngắn nhất" bị bẫy bởi hoạt động nằm lơ lửng ở giữa khoảng thời gian trống, chặn mất 2 hoạt động ở hai đầu.
   - Chỉ duy nhất tiêu chí "Kết thúc sớm nhất" được chứng minh bằng kỹ thuật đổi chỗ (*Exchange Argument*) là luôn bảo đảm tối ưu toàn cục.

4. **Bẫy tràn dưới (*underflow*) trong thuật toán Viterbi chuỗi dài (`kiem_chung_4.3.py`):**
   - Nhân liên tiếp hàng trăm xác suất nhỏ hơn 1 sẽ khiến giá trị tích lũy vượt quá ngưỡng biểu diễn dương nhỏ nhất của số thực dấu phẩy động `double` ($\approx 10^{-308}$), kéo toàn bộ bảng về `0.0`.
   - Thuật toán mất khả năng truy vết và gán nhãn sai. Giải pháp chuẩn mực là chuyển toàn bộ sang không gian logarit (**Log-space Viterbi**).

---
*Báo cáo và mã nguồn được xây dựng chuẩn mực phục vụ học phần Cấu trúc Dữ liệu và Giải thuật — PTIT.*
