### Python hỗ trợ những kiểu dữ liệu cơ bản nào?
số nguyên (int), số thực (float), kiểu logic (boolean), chuỗi ký tự (string)

### Trình bày các loại ghi chú trong Python.
Ghi chú dòng: #

Ghi chú nhiều dòng: “”” … “””, dùng khi:
- Ghi chú dài, nhiều dòng ngay trong code mà vẫn giữ nguyên định dạng.
- Viết docstring cho hàm, lớp, module để IDE, help(), Sphinx đọc được.
- Tạo chuỗi văn bản dài có xuống dòng thật, ví dụ SQL, HTML, JSON mẫu, hoặc thông báo nhiều dòng.

### Trình bày ý nghĩa toán tử /, //, % , **, and, or, is.
/: chia thường

//: chia lấy phần nguyên

%: chia lấy dư

**: lũy thừa

And: đúng khi tất cả điều kiện đều đúng

Or: đúng khi ít nhất một điều kiện đúng

Is: kiểm tra hai biến có cùng trỏ đến một đối tượng hay không

### Trình bày một số cách nhập dữ liệu từ bàn phím .
Dùng hàm input() để nhập dữ liệu từ bàn phím.

### Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
Các loại lỗi:
  + Lỗi cú pháp: được thông bởi trình dịch
  + Lỗi ngữ nghĩa: cần sử dụng kinh nghiệm của lập trình viên để gỡ lỗi
  + Lỗi thực thi: khi lỗi xảy ra, chương trình sẽ tạo ra một đối tượng ngoại lệ gọi là exception.

Cách bắt lỗi: Xử lý ngoại lệ bằng lệnh try để bao một khối mã lệnh

### Giải thích kết quả tính toán của các biểu thức
Cho các biến với giá trị: i1 = 2, i2 = 5, i3 = -3, d1 = 2.0, d2 = 5.0, d3 = -0.5

Cho biết kết quả và giải thích cách thực hiện của các lệnh sau:

(a) i1 + (i2 * i3) = -13

Tính i2 nhân i3; lấy i1 cộng với kết quả vừa tính

(b) i1 * (i2 + i3) = 4

Tính i2 cộng i3; lấy i1 nhân với kết quả vừa tính

(c) i1 / (i2 + i3) = 1

Tính i2 cộng i3; lấy i1 chia với kết quả vừa tính

(d) i1 // (i2 + i3) = 1

Tính i2 cộng i3; lấy i1 chia với kết quả vừa tính

(e) i1 / i2 + i3 = -2,6

Tính i1 chia i2; lấy kết quả vừa tính cộng với i3

(f) i1 // i2 + i3 = -3

Tính i1 chia i2 lấy phần nguyên; lấy phần nguyên đó cộng với i3

(g) 3 + 4 + 5 / 3 = 8,6667

Tính 5 chia 3; tính 3 cộng 4, rồi cộng cho kết quả của phép chia

(h) 3 + 4 + 5 // 3 = 8

Tính 5 chia 3 lấy phần nguyên, tính 3 cộng 4, rồi cộng cho kết quả phần nguyên của phép chia

(i) (3 + 4 + 5) / 3 = 4

Tính 3 cộng 4 cộng 5, rồi lấy kết quả đó chia 3

(j) (3 + 4 + 5) // 3 = 4

Tính 3 cộng 4 cộng 5, rồi lấy kết quả đó chia 3 lấy nguyên

(k) d1 + (d2 * d3) = -0.5

Tính d2 nhân d3, lấy d1 cộng với kết quả vừa tính

(l) d1 + d2 * d3 = -0,5

Tính d2 nhân d3, lấy d1 cộng với kết quả vừa tính

(m) d1 / d2 - d3 = 0,9

Tính d1 chia d2, lấy kết quả trừ d3

(n) d1 / (d2 - d3) = 0,3636

Tính d2 trừ d3, lấy d1 chia kết quả vừa tính

(o) d1 + d2 + d3 / 3 = 6,8333

Tính d3 chia 3, tính d1 cộng d2, lấy kết quả vừa tính cộng kết quả của phép chia

(p) (d1 + d2 + d3) / 3 = 2,1667

Tính d1 cộng d2 cộng d3, lấy kết quả vừa tính chia 3

(q) d1 + d2 + (d3 / 3) = 6,8333

Tính d3 chia 3, tính d1 cộng d2, lấy kết quả vừa tính cộng kết quả của phép chia

(r) 3 * (d1 + d2) * (d1 - d3) = 52,5

Tính d1 + d2, tính d1 - d3, tính 3 nhân với tổng rồi nhân với hiệu

### Hãy viết ngắn gọn lại các lệnh dưới đây:
(a) x = x + 1=> x += 1

(b) x = x / 2=> x /= 2

(c) x = x - 1=> x -= 1

(d) x = x + y=> x += y

(e) x = x - (y + 7)=> x -= (y + 7)

(f) x = 2 * x=> x *= 2

(g) number_of_closed_cases = number_of_closed_cases + 2*ncc=> number_of_closed_cases += 2*ncc
