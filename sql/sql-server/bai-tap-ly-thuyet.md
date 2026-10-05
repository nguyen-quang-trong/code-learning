# Xác định khóa chính, khóa ngoại, ràng buộc tham chiếu

- **Bài tập 1**
    
    > BOPHAN (MABP, TENBP)
    >
    > CHUCVU (MACV, TENCV)
    >
    > NHANVIEN (MANV, HOTENNV, PHAI, NGAYSINH, LUONG, MACV, MABP)

    **Ràng buộc tham chiếu:**
    1. NHANVIEN (MACV) → CHUCVU (MACV)
    2. NHANVIEN (MABP) → BOPHAN (MABP)
    
- **Bài tập 2**
    
    > SV (MSSV, HOTEN, NGSINH, PHAI, NOISINH, MALOP)
    >
    > LOP (MALOP, TENLOP, LTRUONG, SISO, MAGVCN)
    >
    > KHOA (MAKHOA, TENKHOA, TRKHOA)
    >
    > MONHOC (MAMH, TENMH, TC)
    >
    > GV (MAGV, HOTEN, PHAI, NGSINH, NGLV, HSL, MAKHOA)
    >
    > GDAY (MALOP, MAMH, MAGV, HOCKY, NAMHOC)
    >
    > KETQUA (MSSV, MAMH, LANTHI, DIEM)
    
    **Ràng buộc tham chiếu:**
    1. LOP (LTRUONG) → SV (MSSV)
    2. KETQUA (MSSV) → SV (MSSV)
    3. SV (MALOP) → LOP (MALOP)
    4. GDAY (MALOP) → LOP (MALOP)
    5. GV (MAKHOA) → KHOA (MAKHOA)
    6. GDAY (MAMH) → MONHOC (MAMH)
    7. KETQUA (MAMH) → MONHOC (MAMH)
    8. LOP (MAGVCN) → GV (MAGV)
    9. KHOA (TRKHOA) → GV (MAGV)
    10. GDAY (MAGV) → GV (MAGV)
    
- **Bài tập 3**
    
    > KHACHHANG (MAKH, HOTEN, DCHI, SODT, NGSINH, DOANHSO, NGDK)
    >
    > NHANVIEN (MANV, HOTEN, NGVL, SODT)
    >
    > SANPHAM (MASP, TENSP, DVT, NUOCSX, GIA)
    >
    > HOADON (SOHD, NGHD, MAKH, MANV, TRIGIA)>
    >
    > CTHD (SOHD, MASP, SL)

    **Ràng buộc tham chiếu:**
    1. HOADON (MAKH) → KHACHHANG (MAKH)
    2. HOADON (MANV) → NHANVIEN (MANV)
    3. CTHD (MASP) → SANPHAM (MASP)
    4. CTHD (SOHD) → HOADON (SOHD)
    
- **Bài tập 4**
    
    > KHACHHANG (MAKH, TENKH, DIACHI, CMND).
    >
    > KYHAN (MAKYHAN, SOTHANG, LAISUAT).
    >
    > SOTIETKIEM (MASO, MAKH, MAKYHAN, SOTIENGUI).
    >
    > LOAIGD (MALOAIGD, TENLOAIGD).
    >
    > GIAODICH (MASO, LANGD, NGAYGD, SOTIENGD, MALOAIGD)

    **Ràng buộc tham chiếu:**
    1. SOTIETKIEM (MAKH) → KHACHHANG (MAKH)
    2. SOTIETKIEM (MAKYHAN) → KYHAN (MAKYHAN)
    3. GIAODICH (MASO) → SOTIETKIEM (MASO)
    4. GIAODICH (MALOAIGD) → LOAIGD (MALOAIGD)
    
- **Bài tập 5**
    
    > NXB (MANXB, TENNXB, DIACHI)
    >
    > SACH (MASACH, TENSACH, GIA, MANXB, NAMXB)
    >
    > TACGIA (MATG, TENTG, DIENTHOAI)
    >
    > SACH_TACGIA (MATG, MASACH)

    **Ràng buộc tham chiếu:**
    1. SACH (MNXB) → NXB (MANXB)
    2. SACH_TACGIA (MASACH) → SACH (MASACH)
    3. SACH_TACGIA (MATG) → TACGIA (MATG)
    
- **Bài tập 6**
    
    > NHAXUATBAN (MANXB, TENNXB)
    >
    > THELOAI (MATL, TENTL)
    >
    > SACH (MASACH, TUADE, MANXB, TACGIA, SOLUONG, NGAYNHAP, MATL)
    >
    > BANDOC (MATHE, TENBANDOC, DIACHI, SODT)
    >
    > MUONSACH (MASACH, MATHE, NGAYMUON, NGAYTRA)

    **Ràng buộc tham chiếu:**
    1. SACH (MANXB) → NHAXUATBAN (MANXB)
    2. SACH (MATL) → THELOAI (MATL)
    3. MUONSACH (MASACH) → SACH (MASACH)
    4. MUONSACH (MATHE) → BANDOC (MATHE)

# Bài tập đại số quan hệ

## Bài 1

![Cơ sở dữ liệu quản lý đề án](https://res.cloudinary.com/rsaokywc/image/upload/v1790920103/csdl-qlda.webp)

- **Câu 1**: Cho biết tên, ngày sinh thân nhân nữ của nhân viên có mã số 333445555.
    
    $$
    \pi_{TENTN,NGAYSINH}\big(\sigma_{PHAI='Nu'~\land~MA\_NVIEN='333445555'}(THANNHAN)\big)
    $$
    
- **Câu 2**: Cho biết mã nhân viên tham gia đề án 1.
    
    $$
    \pi_{MA\_NVIEN}\big(\sigma_{SODA='1'}(PHANCONG)\big)
    $$
    
- **Câu 3**:  Cho biết mã nhân viên không tham gia đề án 1.
    
    $$
    \begin{split}
    &R1\larr\sigma_{SODA='1'}(PHANCONG)\\
    &\pi_{MA\_NVIEN}(PHANCONG-R1)
    \end{split}
    $$
    
- **Câu 4**:Tìm họ tên của nhân viên phòng số 5 có tham gia vào đề án “Tin hoc hoa” với số giờ làm việc là 10 giờ.
    
    $$
    \begin{split}
    &R1\larr\pi_{MADA}\big(\sigma_{TENDA='Tin~hoc~hoa'}(DEAN)\big)\\ 
    &R2\larr\pi_{MA\_NVIEN}\big(\sigma_{THOIGIAN=10}(PHANCONG\bowtie_{SODA=MADA}R1)\big)\\
    &\pi_{HONV,TENLOT,TENV}\big(\sigma_{PHG=5}(NHANVIEN\bowtie_{MANV=MA\_NVIEN}R2)\big)
    \end{split}
    $$
    
- **Câu 5**: Lập danh sách các con của các nhân viên trong công ty. Hiển thị: họ tên đầy đủ của nhân viên, tên con, phái và ngày sinh của người con đó.
    
    $$
    \begin{split}
    &R1\larr\sigma_{QUANHE='con~trai'~\lor~QUANHE='con~gai'}(THANNHAN)\\
    &R2\larr NHANVIEN\bowtie_{MANV=MA\_NVIEN}R1\\
    &\pi_{HONV,TENLOT,TENNV,TENTN,R1.PHAI,NGAYSINH}(R2)
    \end{split}
    $$
    
- **Câu 6**: Cho biết thông tin cá nhân của trưởng phòng ‘Quan ly’.
    
    $$
    \begin{split}
    &R1\larr\pi_{TRPHG}\big(\sigma_{TENPHG='Quan~ly'}(PHONGBAN)\big)\\
    &R2\larr NHANVIEN\bowtie_{MANV=TRPHG}R1\\
    &\pi_{HONV,TENLOT,TENNV,MANV,NGSINH,DCHI,PHAI}(R2)
    \end{split}
    $$
    
- **Câu 7**: Cho biết tên phòng ban có địa điểm đồng thời ở ‘TPHCM’ và ‘Vung tau’.
    
    $$
    \begin{split}
    &R1\larr\pi_{MAPHG}\big(\sigma_{DIADIEM='TP~HCM'}(DIADIEM\_PHG)\big)\\
    &R2\larr \pi_{MAPHG}\big(\sigma_{DIADIEM='Vung~Tau'}(DIADIEM\_PHG)\big)\\
    &R3\larr R1~\cap~R2\\
    &\pi_{TENPHG}(PHONGBAN\bowtie_{PHONGBAN.MAPHG=R3.MAPHG}R3)
    \end{split}
    $$
    
- **Câu 8**: Cho biết mã nhân viên có tham gia vào các đề án ‘San pham Z’.
    
    $$
    \begin{split}
    &R1\larr\pi_{MADA}\big(\sigma_{TENDA='San~pham~Z'}(DEAN)\big)\\
    &\pi_{MA\_NVIEN}(PHANCONG\bowtie_{SODA=MADA}R1)
    \end{split}
    $$
    
- **Câu 9**: Cho biết trung bình lương của phòng ‘Nghien cuu’.
    
    $$
    \begin{split}
    &R1\larr\pi_{MAPHG}\big(\sigma_{TENPHG='Nghien~cuu'}(PHONGBAN)\big)\\
    &\Huge\Im \normalsize AVG(LUONG)~ \LARGE^{(NHANVIEN\bowtie_{PHG=MAPHG}R1)}
    \end{split}
    $$
    
- **Câu 10**: Cho biết trung bình lương của từng phòng ban. Thông tin hiển thị: tên phòng ban, lương trung bình.    
    $$
    \begin{split}
    &R1(PHG,LTB)\larr PHG\Huge\Im \normalsize AVG(LUONG)~ \LARGE^{(NHANVIEN)}\\
    &\pi_{MAPHG,LTB}(PHONGBAN\bowtie_{MAPHG=PHG}R1)
    \end{split}
    $$
    
- **Câu 11**: Hiển thị tên phòng ban có lương trung bình > 3500.
    
    $$
    \begin{split}
    &R1(PHG,LTB)\larr PHG\Huge\Im \normalsize AVG(LUONG)~ \LARGE^{(NHANVIEN)}\\
    &R2\larr\sigma_{LTB>3500}(R1) \\
    &\pi_{MAPHG,LTB}(PHONGBAN\bowtie_{MAPHG=PHG}R2)
    \end{split}
    $$
    
- **Câu 12**: Cho biết họ tên nhân viên tham gia nhiều đề án hơn ‘Dinh Ba Tien’.
    
    $$
    \begin{split}
    &R1\larr\pi_{MANV}\big(\sigma_{HONV='Dinh'~\land~TENLOT='Ba'~\land~TENNV='Tien'}(NHANVIEN)\big)\\
    &R2\larr PHANCONG\bowtie_{MA\_NVIEN=MANV}R1\\
    &R3(SldaDBT)\larr \Huge\Im \normalsize COUNT(SODA)~ \LARGE^{(R3)}\\
    &R4(MA\_NVIEN,Slda)\larr MA\_NVIEN\Huge\Im \normalsize COUNT(SODA)~ \LARGE^{(PHANCONG)}\\
    &R5(R4\bowtie_{Slda>SldaDBT}R3)\\
    &\pi_{HONV,TENLOT,TENNV}(NHANVIEN\bowtie_{MANV=MA\_NVIEN}R5)
    \end{split}
    $$
    

## Bài 2

![alt img](https://res.cloudinary.com/rsaokywc/image/upload/v1790924818/csdl-dsqh.webp)
> Ở câu g, chữ “C” được thay đổi thành chữ “R”

- **Câu a**
    
    $$
    \def\arraystretch{1.5}
    \begin{array}{c:c:c}
    P & Q & B \\ \hline
    10 & a & b \\ \hdashline
    10 & a & b \\ \hdashline
    25 & a & c
    \end{array}
    $$
    
- **Câu b**
    
    $$
    
    \begin{split}
    &\bullet\sigma_{A>=20~\lor~R=6}(T2)
    \\
    \def\arraystretch{1.5}
    &\begin{array}{c:c:c}
    A & B & R \\\hline
    25 & c & 5 \\\hdashline
    10 & b & 6
    \end{array}
    \\\\
    &\bullet T1\bowtie_{Q=B}\big(\sigma_{A>=20~\lor~R=6}(T2)\big)
    \\
    \def\arraystretch{1.5}
    &\begin{array}{c:c:c:c:c:c}
    P & Q & T1.R & A & B & T2.R \\ \hline
    15 & b & 8 & 10 & b & 6
    \end{array}
    \end{split}
    $$
    
- **Câu c**
    
    $$
    \def\arraystretch{1.5}
    \begin{array}{c:c:c:c:c:c}
    P & Q & T1.R & A & B &T2.R \\\hline
    10 & a & 5 & 25 & c & 5 \\\hdashline
    25 & a & 6 & 10 & b & 6 \\\hdashline
    null & null & null & 10 & b & 4
    \end{array}
    $$
    
- **Câu d**
    
    $$
    \def\arraystretch{1.5}
    \begin{array}{c:c:c:c:c:c}
    P & Q & T1.R & A & B &T2.R \\\hline
    10 & a & 5 & 10 & b & 6 \\\hdashline
    15 & b & 8 & null & null & null \\\hdashline
    25 & a & 6 & null & null & null \\\hdashline
    null & null & null & 10 & b & 4 \\\hdashline
    null & null & null & 25 & c & 5
    \end{array}
    $$
    
- **Câu e**
    
    $$
    \def\arraystretch{1.5}
    \begin{array}{c:c:c}
    P & Q & R \\\hline
    10 & a & 5 \\\hdashline
    15 & b & 8 \\\hdashline
    25 & a & 6 \\\hdashline
    10 & b & 4 \\\hdashline
    25 & c & 5 \\\hdashline
    10 & b & 6
    \end{array}
    $$
    
- **Câu f**
    
    $$
    \def\arraystretch{1.5}
    \begin{array}{c:c:c}
    P & Q & R \\ \hline
    10 & a & 5 \\ \hdashline
    15 & b & 8 \\ \hdashline
    25 & a & 6
    \end{array}
    $$
    
- **Câu g**
    
    $$
    
    \begin{split}
    &\bullet\sigma_{P>=15~\lor~Q='a'}(T1)
    \\
    \def\arraystretch{1.5}
    &\begin{array}{c:c:c}
    P & Q & R \\\hline
    25 & a & 6
    \end{array}
    \\\\
    &\bullet \pi_{B,R}(T2)
    \\
    \def\arraystretch{1.5}
    &\begin{array}{c:c}
    B & R \\ \hline
    b & 4 \\\hdashline
    c & 5 \\\hdashline
    b & 6
    \end{array}
    \\\\
    &\bullet \sigma_{P>=15~\lor~Q='a'}(T1)\bowtie_{T1.R=T2.R}\pi_{B,R}(T2)
    \\
    \def\arraystretch{1.5}
    &\begin{array}{c:c:c:c:c}
    P & Q & T1.R & B & T2.R \\ \hline
    25 & a & 6 & b & 6
    \end{array}
    \end{split}
    $$
    
- **Câu h**
    
    $$
    
    \begin{split}
    &\bullet T1^*T2
    \\
    \def\arraystretch{1.5}
    &\begin{array}{c:c:c:c:c}
    P & Q & T1.R & A & B \\\hline
    10 & a & 5 & 25 & c \\\hdashline
    25 & a & 6 & 10 & b
    \end{array}
    \\\\
    &\bullet \pi_{P,Q,B}(T1^*T2)
    \\
    \def\arraystretch{1.5}
    &\begin{array}{c:c:c}
    P & Q & B \\\hline
    10 & a & c \\\hdashline
    25 & a & b
    \end{array}
    \end{split}
    $$

# Bài tập SQL

## Bài tập loại 1

### Bài tập 1

- **Câu 1:** Tạo csdl QLSV trên đĩa Z:\ với kiểu dữ liệu và các ràng buộc đã cho.
    
    ```sql
    create database QLSV
    on(
    	name=QLSV_mdf,
    	filename='Z:\QLSV.mdf',
    	size=10,
    	maxsize=50,
    	filegrowth=5)
    log on(
    	name=QLSV_log,
    	filename='Z:\QLSV.ldf',
    	size=10,
    	maxsize=50,
    	filegrowth=5)
    ```
    
- **Câu 2:** Tạo tất cả các ràng buộc tham chiếu (khóa ngoại)
    
    | Thuộc tính | Kiểu dữ liệu | Diễn giải |
    | --- | --- | --- |
    | TEN | chuỗi (25) | Họ tên sinh viên |
    | MASV | chuỗi (4) | Mã sinh viên |
    | NAM | số nguyên | Năm thứ (SV năm thứ mấy) |
    | KHOA | chuỗi (10) | Khoa quản lý |
    | MAMH, MAMH_TRUOC | chuỗi (6) | Mã môn học, mã môn học trước |
    | TEN_MH | chuỗi (30) | Tên môn học |
    | SOTINCHI | số nguyên | Số tín chỉ |
    | DIEM | số thực (1 số lẻ) | Điểm thi |
    | MAHP | số nguyên | Mã học phần |
    | HOCKY | số nguyên | Học kỳ |
    | NAMHOC | chuỗi (10) | Năm học |
    | GV | chuỗi (25) | Tên giáo viên giảng dạy |
    
    **Ràng buộc:**
    
    - SINHVIEN:
        - ten, khoa: không được rỗng
        - masv: gồm 1 ký tự chữ, 3 ký tự số
        - khoa: mặc định là CNTT
    - KETQUA: diem: có 1 số lẻ, phải >= 0 và <= 10
    - MHOC:
        - Mamh: gồm 3 ký tự chữ, 3 ký tự số
        - Ten_mh: duy nhất và không được rỗng
        - Sotinchi: phải >= 1 và <= 10
    - HOCPHAN: Mahp>0

    **Tạo bảng:**
    
    - **Bảng `SVIEN`**
        
        ```sql
        create table SVIEN(
        	ten nvarchar(25) not null,
        	masv char(4) primary key check(masv LIKE '[a-z][0-9][0-9][0-9]'),
        	nam int,
        	khoa varchar(10) not null default('CNTT')
        )
        ```
        
    - **Bảng `MHOC`**
        
        ```sql
        create table MHOC(
        	ten_mh nvarchar(30),
        	mamh char(6) primary key check(mamh LIKE '[a-z][a-z][a-z][0-9][0-9][0-9]'),
        	sotinchi int check(sotinchi>=1 and sotinchi<=10),
        	khoa char(10)
        )
        ```
        
    - **Bảng `HOCPHAN`**
        
        ```sql
        create table HOCPHAN(
        	mahp int primary key check(mahp>0),
        	mamh char(6),
        	hocky int,
        	namhoc char(10),
        	gv nvarchar(25)
        )
        ```
        
    - **Bảng `DIEUKIEN`**
        
        ```sql
        create table DKIEN(
        	mamh char(6),
        	mamh_truoc char(6),
        	primary key(mamh,mamh_truoc)
        )
        ```
        
    - **Bảng `KETQUA`**
        
        ```sql
        create table KETQUA(
        	masv char(4),
        	mahp int,
        	diem decimal(3,1) check (diem>=0 and diem<10),
        	primary key(masv,mahp),
        	foreign key(masv)references SVIEN(masv),
        	foreign key(mahp)references HOCPHAN(mahp)
        )
        ```
        
- **Câu 3:** Nhập dữ liệu cho tất cả các bảng trên
    - **Bảng `SVIEN`**
        
        
        | TEN | MASV | NAM | KHOA |
        | --- | --- | --- | --- |
        | Nguyễn Hồng Sơn | A001 | 1 | SP |
        | Lê Châu Bảo | B010 | 2 | CNTT |
        
        ```sql
        insert into SVIEN values ('Nguyen Hong Son','A001',1,'SP')
        insert into SVIEN values ('Le Chau Bao','B010',2,'CNTT')
        ```
        
    - **Bảng `MHOC`**
        
        
        | TEN_MH | MAMH | SOTINCHI | KHOA |
        | --- | --- | --- | --- |
        | Tin học đại cương | COS301 | 3 | CNTT |
        | Cấu trúc dữ liệu | COS312 | 3 | CNTT |
        | Toán rời rạc | COS111 | 2 | CNTT |
        | Anh văn không chuyên 1 | ENG101 | 4 | SP |
        | Anh văn không chuyên 2 | ENG102 | 3 | SP |
        
        ```sql
        insert into MHOC values ('Tin hoc dai cuong','COS301',3,'CNTT')
        insert into MHOC values ('Cau truc du lieu','COS312',3,'CNTT')
        insert into MHOC values ('Toan roi rac','COS111',2,'CNTT')
        insert into MHOC values ('Anh van khong chuyen 1','ENG101',4,'SP')
        insert into MHOC values ('Anh van khong chuyen 2','ENG102',3,'SP')
        ```
        
    - **Bảng `HOCPHAN`**
        
        
        | MAHP | MAMH | HOCKY | NAMHOC | GV |
        | --- | --- | --- | --- | --- |
        | 1 | COS301 | 1 | 2010-2011 | Kim |
        | 2 | COS111 | 1 | 2010-2011 | Trang |
        | 3 | ENG101 | 1 | 2011-2012 | Nam |
        | 4 | COS111 | 2 | 2011-2012 | Duy |
        | 5 | ENG102 | 2 | 2011-2012 | Lộc |
        | 6 | COS301 | 2 | 2011-2012 | Thủy |
        
        ```sql
        insert into HOCPHAN values (1,'COS301',1,'2010-2011','Kim')
        insert into HOCPHAN values (2,'COS111',1,'2010-2011','Trang')
        insert into HOCPHAN values (3,'ENG101',1,'2011-2012','Nam')
        insert into HOCPHAN values (4,'COS111',2,'2011-2012','Duy')
        insert into HOCPHAN values (5,'ENG102',2,'2011-2012','Loc')
        insert into HOCPHAN values (6,'COS301',2,'2011-2012','Thuy')
        ```
        
    - **Bảng `DIEUKIEN`**
        
        
        | MAMH | MAMH_TRUOC |
        | --- | --- |
        | COS312 | COS301 |
        | COS312 | COS111 |
        | ENG102 | ENG101 |
        
        ```sql
        insert into DKIEN values ('COS312','COS301')
        insert into DKIEN values ('COS312','COS111')
        insert into DKIEN values ('ENG102','ENG101')
        ```
        
    - **Bảng `KETQUA`**
        
        
        | MASV | MAHP | DIEM |
        | --- | --- | --- |
        | A001 | 1 | 5.5 |
        | A001 | 3 | 8 |
        | B010 | 1 | 9 |
        | B010 | 2 | 7.5 |
        | B010 | 3 | 6 |
        | B010 | 5 | 8 |
        | B010 | 6 | 9 |
        | A001 | 5 | 9.5 |
        
        ```sql
        insert into KETQUA values ('A001',1,5.5)
        insert into KETQUA values ('A001',3,8)
        insert into KETQUA values ('B010',1,9)
        insert into KETQUA values ('B010',2,7.5)
        insert into KETQUA values ('B010',3,6)
        insert into KETQUA values ('B010',5,8)
        insert into KETQUA values ('B010',6,9)
        insert into KETQUA values ('A001',5,9.5)
        ```
        

### Bài tập 2

- **Câu 1:** Tạo csdl QLNV trên đĩa Z:\ với kiểu dữ liệu hợp lý và các ràng buộc đã cho.
    
    
    |  | Primary data (.mdf) | Log file (.log) |
    | --- | --- | --- |
    | Tên | QLNV_data | QLNV_log |
    | Đường dẫn | Z:\QLNV_data.mdf | Z:\QLNV_log.ldf |
    | Tự động tăng kích thước | Yes | Yes |
    | Kích thước ban đầu | 4MB | 2MB |
    | Kích thước mỗi lần tăng | 2MB | 1MB |
    | Kích thước tối đa | 20MB | 10MB |
    
    ```sql
    create database QLNV
    on(
    	name=QLNV_mdf,
    	filename='Z:\QLNV.mdf',
    	size=4,
    	maxsize=20,
    	filegrowth=2)
    log on(
    	name=QLNV_log,
    	filename='Z:\QLNV.ldf',
    	size=2,
    	maxsize=10,
    	filegrowth=1)
    ```
    
- **Câu 2:** Tạo tất cả các ràng buộc tham chiếu (khóa ngoại)
    
    
    - PHONG (Maphg  Char(2),  Tenphg  Varchar(20))
        - Maphg: 2 kí tự chữ
        - Tenphg: duy nhất, không được rỗng
    - CONGVIEC (Macv  Char(3),  Tencv  Varchar(20))
        - Macv: 3 kí tự chữ
        - Tencv: duy nhất, không được rỗng
    - NHANVIEN (Manv Char(5), Holot Varchar(15), Ten Varchar(10), Luong SmallInt, Phai Bit, Ngsinh Date,  Macv Char(3), Mapb Char(2))
        - Manv:  2 kí tự chữ và 3 kí tự số
        - Holot, Ten: không được rỗng
        - Luong: phải >0
        - Phai:  mặc định là ‘nam’
        
    
    - **Bảng `PHONG`**
        
        ```sql
        create table PHONG(
        	maphg char(2) primary key check(maphg like '[a-z][a-z]'),
        	tenphg varchar(20) unique not null
        )
        ```
        
    - **Bảng `CONGVIEC`**
        
        ```sql
        create table CONGVIEC(
        	macv char(3) primary key check(macv like '[a-z][a-z][a-z]'),
        	tencv varchar(20) unique not null
        )
        ```
        
    - **Bảng `NHANVIEN`**
        
        ```sql
        create table NHANVIEN(
        	manv char(5) primary key check(manv like '[a-z][a-z][0-9][0-9][0-9]'),
        	holot varchar(15) not null,
        	ten varchar(10) not null,
        	luong smallint check(luong>0),
        	phai bit default('True'),
        	ngsinh date,
        	macv char(3),
        	mapb char(2),
        	foreign key (macv)references CONGVIEC(macv),
        	foreign key (mapb)references PHONG(maphg)
        )
        ```
        
    
- **Câu 3:** Nhập dữ liệu cho tất cả các bảng trên
    - **Bảng `PHONG`**
        
        
        | Maphg | Tenphg |
        | --- | --- |
        | KT | Phong ke toan |
        | LT | Phong lap trinh |
        | GD | Ban giam doc |
        | QC | Phong quang cao |
        | TE | Phong kiem thu |
        
        ```sql
        insert into PHONG values ('KT','Phong ke toan')
        insert into PHONG values ('LT','Phong lap trinh')
        insert into PHONG values ('GD','Ban giam doc')
        insert into PHONG values ('QC','Phong quang cao')
        insert into PHONG values ('TE','Phong kiem thu')
        ```
        
    - **Bảng `CONGVIEC`**
        
        
        | Macv | Tencv |
        | --- | --- |
        | ANA | Phan tich |
        | ACC | Ke toan |
        | MGR | Giam doc |
        | PRO | Lap trinh vien |
        | TES | Kiem thu phan mem |
        
        ```sql
        insert into CONGVIEC values ('ANA','Phan tich')
        insert into CONGVIEC values ('ACC','Ke toan')
        insert into CONGVIEC values ('MGR','Giam doc')
        insert into CONGVIEC values ('PRO','Lap trinh vien')
        insert into CONGVIEC values ('TES','Kiem thu phan mem')
        ```
        
    - **Bảng `NHANVIEN`**
        
        
        | Manv | Holot | Ten | Luong | Phai | Nsinh | Macv | Mapb |
        | --- | --- | --- | --- | --- | --- | --- | --- |
        | KT001 | Nguyen Thanh | Tuyen | 1000 | True | 01/05/1980 | ACC | KT |
        | LT001 | Tran Huu | Huy | 1500 | False | 07/07/1979 | ANA | LT |
        | LT002 | Mai Van | Tung | 1200 | False | 11/08/1986 | PRO | LT |
        | LT003 | Ha My | Hang | 1200 | True | 12/09/1988 | PRO | LT |
        | TE001 | Trieu Minh | Minh | 900 | True | 05/10/1988 | TES | TE |
        | GD001 | Truong Vo | Ky | 2500 | False | 09/15/1979 | MGR | GD |
        
        ```sql
        insert into NHANVIEN values ('KT001','Nguyen Thanh','Tuyen',1000,'True','01/05/1980','ACC','KT')
        insert into NHANVIEN values ('LT001','Tran Huu','Huy',1500,'False','07/07/1979','ANA','LT')
        insert into NHANVIEN values ('LT002','Mai Van','Tung',1200,'False','11/08/1986','PRO','LT')
        insert into NHANVIEN values ('LT003','Ha My','Hang',1200,'True','12/09/1988','PRO','LT')
        insert into NHANVIEN values ('TE001','Trieu Minh','Minh',900,'True','05/10/1988','TES','TE')
        insert into NHANVIEN values ('GD001','Truong Vo','Ky',2500,'False','09/15/1979','MGR','GD')
        ```

## Bài tập loại 2

### Bài tập 1 (Dùng CSDL QLSV ở bài tập loại 1)

- **Câu 2:** Thêm vào bảng SVIEN cột Dthoai varchar(9) và Phai char(3) (chi chap nhan 1 trong 2 giá trị ‘nam’ hoặc ‘nu’)
    
    ```sql
    alter table svien add Dthoai varchar(9)
    alter table svien add Phai char(3) check(Phai='nam'or Phai='nu')
    ```
    
- **Câu 3:** Sửa cột Dthoai có kiểu dữ liệu mới là varchar(11) và không được trùng nhau.
    
    ```sql
    alter table svien alter column Dthoai varchar(11)
    alter table svien add unique(Dthoai)
    ```
    
- **Câu 4:** Cập nhật số điện thoại của A001 thành ‘01234111222’
    
    ```sql
    update svien 
    set dthoai='01234111222'
    where masv='A001'
    ```
    
- **Câu 5:** Xóa bỏ cột Dthoai đã thêm vào trên bảng SVIEN.
    
    ```sql
    alter table svien drop column dthoai
    ```
    
- **Câu 6:** Thêm 1 sinh viên: (‘Phan Quoc Tuan’, ‘B012’,1, nam)
    
    ```sql
    insert into svien values('Phan Quoc Tuan', 'B012',1,default,'Nam')
    ```
    
- **Câu 7:** Thêm 1 học phần (HOCPHAN) mới (7, ‘COS301’,1,2011-2012,Van)
    
    ```sql
    insert into hocphan values(7,'COS301',1,'2011-2012','Van')
    ```
    
- **Câu 8:** Thêm vào bảng KETQUA (‘B012’, 7, 9)
    
    ```sql
    insert into ketqua values('B012', 7, 9)
    ```
    
- **Câu 9:** Sửa tên của ‘Phan Quoc Tuan’ thành ‘Pham Quoc Tuan’ và năm thành 2
    
    ```sql
    update svien
    set ten='Pham Quoc Tuan', nam=2
    where ten='Phan Quoc Tuan'
    ```
    
- **Câu 10:** Sửa điểm thi học phần 7 của ‘Pham Quoc Tuan’ thành 9.5
    
    ```sql
    update ketqua
    set diem=9.5
    where mahp=7
    and masv in(select masv
    			from svien
    			where ten='Pham Quoc Tuan')
    ```
    
- **Câu 11:** Xóa sv có mã số B012, xóa kết quả của sv B012, xóa môn COS301 trong hk 1 năm 2011 - 2012
    - **Xóa kết quả của sv B012**
    
    ```sql
    delete from ketqua
    where masv='B012'
    ```
    
    - **Xóa môn COS301 trong hk 1 năm 2011-2012**
    
    ```sql
    delete from hocphan
    where mamh='COS301' and hocky=1 and namhoc='2011-2012'
    ```
    
    - **Xóa sv có mã số B012**
    
    ```sql
    delete from svien
    where masv='B012'
    ```
    
- **Câu 12:** Thực hiện các lệnh ở mục 2.5 trên bảng KETQUA, HOCPHAN
    
    ```sql
    
    sp_help ketqua
    sp_pkeys ketqua
    sp_fkeys ketqua
    
    sp_help hocphan
    sp_pkeys hocphan
    sp_fkeys hocphan
    ```
    

### Bài tập 2 (Dùng CSDL QLBS ở bài tập loại 1)

- **Câu 2:** Tạo bảng ChamCongNV có cấu trúc giống bảng Nhanvien
    
    ```sql
    create table ChamCongNV(
    	manv  char(4) primary key,
    	holot nvarchar(25),
    	tennv nvarchar(10),
    	phai nvarchar(3),
    	ngaysinh smalldatetime,
    	diachi nvarchar(40)
    )
    ```
    
- **Câu 3:** Chèn thêm cột NgayCong, DonGiaGiaCong (có kiểu số nguyên) vào bảng ChamCongNV
    
    ```sql
    alter table chamcongnv add ngaycong int
    alter table chamcongnv add dongiagiacong int
    ```
    
- **Câu 4:** Xóa các cột HoLot, Tennv, Phai, NgaySinh, DiaChi trong bảng ChamCongNV
    
    ```sql
    alter table chamcongnv drop column holot
    alter table chamcongnv drop column tennv
    alter table chamcongnv drop column phai
    alter table chamcongnv drop column ngaysinh
    alter table chamcongnv drop column diachi
    ```
    
- **Câu 5:** Thêm vào bảng Hoadon cột NGAYLAPHD (kiểu char(10))
    
    ```sql
    alter table hoadon add ngaylaphd char(10)
    ```
    
- **Câu 6:** Hiệu chỉnh kiểu dữ liệu cho cột vừa thêm thành kiểu datetime.
    
    ```sql
    alter table hoadon alter column ngaylaphd datetime
    ```
    
- **Câu 7:** Đổi tên cơ sở dữ liệu thành HOTENSV_SOMAY
    
    ```sql
    sp_renamedb 'QLBanSach','HOTENSV_SOMAY'
    ```
    
- **Câu 8:** Đổi tên bảng ChamCongNV thành Bangluong.
    
    ```sql
    sp_rename 'ChamCongNV','Bangluong'
    ```
    
- **Câu 9:** Xóa Bangluong khỏi cơ sở dữ liệu.
    
    ```sql
    drop table Bangluong
    ```
    
- **Câu 10:** Xóa bảng Hoadon khỏi CSDL, có thực hiện được không? Giải thích. Cách nào để xóa bảng HoaDon?
    
    ```sql
    drop table hoadon
    ```
    
- **Lệnh UPDATE:**
    - **Câu 11:** Cập nhật đơn giá 30000 cho mã sách S001
        
        ```sql
        update sach
        set dongia=30000
        where masach='S001'
        ```
        
    - **Câu 12:** Cập nhật số lượng tồn = 50% số lượng tồn hiện có cho những cuốn sách thuộc mã nhóm N002
        
        ```sql
        update sach
        set slton=slton*50/100
        where maloai='N002'
        ```
        
    - **Câu 13:** Cập nhật mã loại N001 trong bảng LOAISACH thành N100? Có cập nhật được hay không? Vì sao?
        
        ```sql
        update loaisach
        set maloai='N100'
        where maloai='N001'
        --Không thể cập nhật mã loại N001 trong bảng LOAISACH thành N100 bởi vì 'N001' đang được sử dụng trong một bảng khác và việc thay đổi này gây xung đột dữ liệu giữa các bảng
        ```
        
    - **Câu 14:** Tăng đơn giá các danh mục sách lên 3%
        
        ```sql
        update sach
        set dongia=dongia+dongia*3/100
        ```
        
    - **Câu 15:** Giảm 10% đơn giá cho loại sách Anh văn.
        
        ```sql
        update sach
        set dongia=dongia-dongia*10/100
        where maloai in (
        			select maloai
        			from loaisach
        			where tenloai='Anh van'
        		)
        ```
        
    - **Câu 16:** Thêm vào cột GIABAN trong bảng CTHD. Cập nhật giá bán bằng với đơn giá trong bảng SACH.
        
        ```sql
        alter table cthd add giaban int
        
        update cthd
        set giaban = (
        			select dongia
        			from sach
        			where cthd.masach=sach.masach
        		)
        ```
        
    - **Câu 17:**Thêm vào cột NGAYVAOLAM, kiểu date trong bảng Nhanvien. Cập nhật ngày vào làm cho nhân viên = Năm sinh +18.
        
        ```sql
        alter table nhanvien add ngayvaolam date
        
        update nhanvien
        set ngayvaolam=dateadd(year,18,ngaysinh)
        ```
        
    - **Câu 18:** Thêm vào cột PhuCap, kiểu int trong bảng Nhanvien. Cập nhật phụ cấp cho những nhân viên có thâm niên từ 10 năm trở lên (thâm niên được tính = năm hiện tại – năm vào làm). Phụ cấp = 100.000 * thâm niên.
        
        ```sql
        alter table nhanvien add phucap int
        update nhanvien
        set phucap=100000*(year(ngayvaolam)-year(ngaysinh))
        where (year(ngayvaolam)-year(ngaysinh))>=10
        ```
        
- **Lệnh INSERT:**
    - **Câu 19:** Thêm vào bảng LOAISACH (‘N007’, ‘Sức khỏe và đời sống’)
        
        ```sql
        insert into loaisach values('N007','Suc khoe va doi song')
        ```
        
    - **Câu 20:** Thêm vào bảng CTHD với số hóa đơn 6, mã sách S001 với số lượng 5 và S002 với số lượng
        
        ```sql
        insert into cthd values('6','S001',5,0)
        insert into cthd values('6','S002',20,0)
        ```
        
    - **Câu 21:** Thêm vào bảng SACH với mã sách S011, tên sách là ‘Cánh đồng bất tận’, tác giả ‘Nguyễn Ngọc Tư’, mã loại N006, đơn giá 45000, số lượng tồn 5.
        
        ```sql
        insert into sach values('S011','Canh dong bat tan','Nguyen Ngoc Tu','N006',45000,5)
        ```
        
    - **Câu 22:** Thêm vào bảng SACH với mã sách S011, tên sách là ‘Hỏi đáp sức khỏe’, tác giả ‘Đỗ Hồng Ngọc’, mã loại N008, đơn giá 25000, số lượng tồn 50. Hãy quan sát lỗi (nếu có) và giải thích?
        
        ```sql
        insert into sach values('S011','Hoi dap suc khoe','Do Hong Ngoc','N008',25000,50)
        --Không thể thực thi dòng lệnh trên vì 'S011' đã tồn tại
        ```
        
- **Lệnh DELETE:**
    - **Câu 23:** Xóa loại sách ‘N007’ trong bảng LOAISACH
        
        ```sql
        delete from loaisach
        where maloai='N007'
        ```
        
    - **Câu 24:** Xóa Hoadon số 6 trong bảng Hoadon. Hãy quan sát lỗi (nếu có) và giải thích?
        
        ```sql
        delete from hoadon
        where mahd='6'
        --Không thể thực thi dòng lệnh trên vì nếu xóa sẽ ảnh hưởng đến dữ liệu trong bảng khác.
        ```