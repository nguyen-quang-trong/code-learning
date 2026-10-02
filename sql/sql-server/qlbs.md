### Cơ sở dữ liệu quản lý bán sách có sẵn phục vụ việc học: [QLBS.zip](https://drive.google.com/file/d/1dKblSUakiw1pmGXcsFmWPaeYhiKAEM2z/view?usp=sharing)

- **Câu 1:** Liệt kê danh mục sách theo thứ tự mã sách.
    
    ```sql
    select *
    from sach
    order by masach
    ```
    
- **Câu 2:** Liệt kê nhân viên theo thứ tự tên.
    
    ```sql
    select *
    from nhanvien
    order by tennv
    ```
    
- **Câu 3:** Liệt kê những nhân viên nam theo thứ tự tên.
    
    ```sql
    select *
    from nhanvien
    where phai='Nam'
    order by tennv
    ```
    
- **Câu 4:** Liệt kê những nhân viên có tên là Đào.
    
    ```sql
    select *
    from nhanvien
    where tennv='Dao'
    ```
    
- **Câu 5:** Liệt kê những nhân viên có tên bắt đầu bằng ký tự ‘t’
    
    ```sql
    select *
    from nhanvien
    where tennv like 'T%'
    ```
    
- **Câu 6:** Liệt kê những nhân viên có họ lót là Thảo hay Văn
    
    ```sql
    select *
    from nhanvien
    where holot like '%Thao%'
    		or holot like '%Van%'
    ```
    
- **Câu 7:** Liệt kê những nhân viên sinh năm 1975
    
    ```sql
    select *
    from nhanvien
    where year(ngaysinh)=1975
    ```
    
- **Câu 8:** Liệt kê những nhân viên sinh vào tháng 5
    
    ```sql
    select *
    from nhanvien
    where month(ngaysinh)=5
    ```
    
- **Câu 9:** Liệt kê những cuốn sách có tên tác giả bắt đầu là Nguyễn
    
    ```sql
    select *
    from sach
    where tacgia like 'Nguyen%'
    ```
    
- **Câu 10:** Liệt kê những sách có số lượng tồn < 80
    
    ```sql
    select *
    from sach
    where slton<80
    ```
    
- **Câu 11:** Liệt kê những quyển sách có đơn giá từ 14000 đến 40000
    
    ```sql
    select *
    from sach
    where dongia>=14000 
    		and dongia<=40000
    ```
    
- **Câu 12:** Liệt kê những cuốn sách thuộc loại N001 và N002
    
    ```sql
    select *
    from sach
    where maloai='N001' 
    		or maloai='N002'
    ```
    
- **Câu 13:** Liệt kê những sách có đơn giá>=30.000 và số lượng tồn <50
    
    ```sql
    select *
    from sach
    where dongia>=30000 
    		and slton<50
    ```
    
- **Câu 14:** Liệt kê những cuốn sách thuộc loại N001 và số lượng tồn từ 10 đến 40
    
    ```sql
    select *
    from sach
    where maloai='N001' 
    		and slton>=10 
    		and slton<=40
    ```
    
- **Câu 15:** Liệt kê hóa đơn theo thứ tự tăng dần của MaNV, nếu trùng MaNV thì xếp theo ngày bán.
    
    ```sql
    select *
    from hoadon
    order by manv,ngayban
    ```
    
- **Câu 16:** Hiển thị danh sách những sách thuộc ngành tin học gồm: mã sách, tên sách, mã nhóm.
    
    ```sql
    select masach,tensach,ls.maloai
    from sach s,loaisach ls
    where s.maloai=ls.maloai 
    		and tenloai='Tin hoc'
    ```
    
- **Câu 17:** Liệt kê sách thuộc loại tin học có số lượng tồn >10
    
    ```sql
    select *
    from sach s, loaisach ls
    where s.maloai=ls.maloai
    		and tenloai='Tin hoc'
    		and slton>10
    ```
    
- **Câu 18:** Liệt kê các danh mục sách và tiền tồn vốn, xếp theo thứ tự giảm dần của tiền tồn. Bảng kết quả gồm mã sách, tên sách, loại sách, tác giả, đơn giá, số lượng, tiền vốn = đơn giá x số lượng tồn
    
    ```sql
    select masach,tensach,s.maloai,tacgia,dongia,slton,(dongia*slton) as 'TienVon'
    from sach s, loaisach ls
    where s.maloai=ls.maloai
    order by tienvon desc
    ```

- **Câu 19:** Danh sách các hóa đơn ứng với tổng tiền của từng hóa đơn.
    
    ```sql
    select hd.mahd,hd.MaNV,hd.NgayBan, sum(soluong*dongia) as 'TongTien'
    from sach s, cthd, hoadon hd
    where s.masach=cthd.masach 
    		and cthd.mahd=hd.mahd
    group by hd.mahd,hd.MaNV,hd.NgayBan
    ```
    
- **Câu 20:** Danh sách các hóa đơn có ngày bán là ngày 15/7/2015.
    
    ```sql
    select *
    from hoadon
    where day(ngayban)=15 
    		and month(ngayban)=7 
    		and year(ngayban)=2015
    ```
    
- **Câu 21:** Danh sách các sách đã được bán, ứng với tổng số lượng, thành tiền.
    
    ```sql
    select s.masach,s.tensach,s.tacgia,s.maloai, sum(soluong) as 'TongSL', sum(dongia*soluong) as 'ThanhTien'
    from cthd, sach s, hoadon hd
    where s.masach=cthd.masach 
    		and cthd.mahd=hd.mahd
    group by s.masach,s.tensach,s.tacgia,s.maloai
    ```
    
- **Câu 22:** Danh sách các hóa đơn bán trong 20/7/2015, ứng với tổng số lượng, thành tiền.
    
    ```sql
    select hd.mahd, sum(soluong) as 'TongSL', sum(dongia*soluong) as 'ThanhTien'
    from sach s, cthd, hoadon hd
    where s.masach=cthd.masach 
    		and cthd.mahd=hd.mahd 
    		and ngayban='2015/7/20'
    group by hd.mahd
    ```
    
- **Câu 23:** Danh sách các sách không bán được.
    
    ```sql
    select *
    from sach
    where masach not in (
    			select masach
    			from cthd
    		)
    ```
    
- **Câu 24:** Danh sách các nhân viên chưa lập hóa đơn nào.
    
    ```sql
    select *
    from nhanvien
    where manv not in (
    			select manv
    			from hoadon
    		)
    ```
    
- **Câu 25:** Danh sách các sách có số lượng bán nhiều nhất.
    
    ```sql
    select s.masach,s.tensach,s.tacgia,s.maloai, sum(soluong)
    from sach s,cthd c
    where s.masach=c.masach
    group by s.masach,s.tensach,s.tacgia,s.maloai
    having sum(soluong)=(
    			select top 1 sum(soluong) 
    			from cthd
    			group by masach
    			order by sum(soluong) desc
    		)
    ```
    
- **Câu 26:** Danh sách các nhân viên ứng với tổng số tiền hóa đơn mà nhân viên ấy lập.
    
    ```sql
    select nv.manv, sum(s.dongia*c.soluong)
    from nhanvien nv, hoadon hd, cthd c, sach s
    where s.masach=c.masach 
    		and c.mahd=hd.mahd 
    		and hd.manv=nv.manv
    group by nv.manv
    ```
    
- **Câu 27:** Thống kê thành tiền ứng với mỗi nhóm sách và mỗi ngày.
    
    ```sql
    select s.maloai, h.ngayban, sum(s.dongia*c.soluong)
    from sach s, cthd c, hoadon h
    where s.masach=c.masach 
    		and c.mahd = h.mahd
    group by s.maloai, h.ngayban
    ```
    
- **Câu 28:** Cho biết nhân viên nào bán được nhiều sách nhất và số lượng là bao nhiêu.
    
    ```sql
    select nv.manv, sum(c.soluong)
    from nhanvien nv, hoadon h, cthd c
    where nv.manv=h.manv 
    		and h.mahd=c.mahd
    group by nv.manv
    having sum(c.soluong)=(
    			select top 1 sum(soluong)
    			from hoadon h, cthd c
    			where h.mahd=c.mahd
    			group by manv
    			order by sum(soluong) desc
    		)
    ```
    
- **Câu 29:** Cho biết những nhân viên nào có cùng ngày sinh.
    
    ```sql
    select nv1.manv
    from nhanvien nv1, nhanvien nv2
    where nv1.manv!=nv2.manv 
    		and nv1.ngaysinh=nv2.ngaysinh
    ```
    
- **Câu 30:** Cho biết nhân viên nào có tuổi lớn nhất.
    
    ```sql
    select *
    from nhanvien
    where year(getdate())-year(ngaysinh)=(
    			select top 1 year(getdate())-year(ngaysinh)
    			from nhanvien
    			order by year(getdate())-year(ngaysinh) desc
    		)
    ```