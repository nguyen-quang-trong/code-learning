### Cơ sở dữ liệu quản lý dự án có sẵn phục vụ việc học: [QLDA.zip](https://drive.google.com/file/d/1oWgGa-41np3MNjKWXB4QYvmBOegvD1FU/view?usp=sharing)

- **Câu 1:** Tìm các nhân viên làm việc ở phòng số 4
    
    ```sql
    select *
    from NHANVIEN
    where phg=4
    ```
    
- **Câu 2:** Tìm các nhân viên có mức lương trên 3000
    
    ```sql
    select *
    from NHANVIEN
    where luong>3000
    ```
    
- **Câu 3:** Tìm các nhân viên có mức lương trên 2500 ở phòng 4 hoặc các nhân viên có mức lương trên 3000 ở phòng 5
    
    ```sql
    select *
    from NHANVIEN
    where  (luong>2500 and phg=4) 
    		or (luong>3000 and phg=5)
    ```
    
- **Câu 4:** Cho biết họ tên đầy đủ của các nhân viên ở TP HCM
    
    ```sql
    select honv,tenlot,tennv
    from NHANVIEN
    where dchi like '%TP HCM%'
    ```
    
- **Câu 5:** Cho biết họ tên đầy đủ của các nhân viên có họ bắt đầu bằng ký tự ‘N’
    
    ```sql
    select honv,tenlot,tennv
    from NHANVIEN
    where honv like 'N%'
    ```
    
- **Câu 6:** Cho biết ngày sinh và địa chỉ của nhân viên Dinh Ba Tien.
    
    ```sql
    select ngsinh,dchi
    from NHANVIEN
    where honv='Dinh' 
    		and tenlot='Ba' 
    		and tennv='Tien'
    ```
    
- **Câu 7:** Cho biết các nhân viên có năm sinh trong khoảng 1960 đến 1965
    
    ```sql
    select *
    from NHANVIEN
    where year(ngsinh) between 1960 and 1965
    ```
    
- **Câu 8:** Cho biết các nhân viên và năm sinh của nhân viên
    
    ```sql
    select *, year(ngsinh) as 'Nam sinh'
    from NHANVIEN
    ```
    
- **Câu 9:** Cho biết các nhân viên và tuổi của nhân viên
    
    ```sql
    select *, year(getdate())-year(ngsinh) as 'Tuoi'
    from NHANVIEN
    ```
    
- **Câu 10:** Với mỗi phòng ban, cho biết tên phòng ban và địa điểm phòng
    
    ```sql
    select tenphg,diadiem
    from PHONGBAN pb, DIADIEM_PHG ddp
    where pb.maphg=ddp.maphg
    ```
    
- **Câu 11:** Tìm tên những người trưởng phòng của từng phòng ban
    
    ```sql
    select honv,tenlot,tennv
    from NHANVIEN nv, PHONGBAN pb
    where nv.manv=pb.trphg
    ```
    
- **Câu 12:** Tìm tên và địa chỉ của tất cả các nhân viên của phòng "Nghiên cứu".
    
    ```sql
    select honv,tenlot,tennv,dchi
    from NHANVIEN nv, PHONGBAN pb
    where nv.phg=pb.maphg 
    		and pb.tenphg='Nghien cuu'
    ```
    
- **Câu 13:** Với mỗi đề án ở Hà Nội, cho biết tên đề án, tên phòng ban, họ tên và ngày nhận chức của trưởng phòng của phòng ban chủ trì đề án đó.
    
    ```sql
    select tenda,tenphg,honv,tenlot,tennv,ng_nhanchuc
    from NHANVIEN nv, PHONGBAN pb, DEAN da
    where da.ddiem_da='Ha Noi' 
    		and da.phong=pb.maphg 
    		and nv.manv=pb.trphg
    ```
    
- **Câu 14:** Tìm tên những nữ nhân viên và tên người thân của họ
    
    ```sql
    select honv,tenlot,tennv,tentn
    from NHANVIEN nv, THANNHAN tn
    where nv.phai='Nu' 
    		and nv.manv=tn.ma_nvien
    ```
    
- **Câu 15:** Với mỗi nhân viên, cho biết họ tên nv và họ tên người quản lý trực tiếp của nhân viên đó
    
    ```sql
    select nv.honv,nv.tenlot,nv.tennv,nql.honv,nql.tenlot,nql.tennv
    from NHANVIEN nv, NHANVIEN nql
    where nv.ma_nql=nql.manv
    ```
    
- **Câu 16:** Với mỗi nhân viên, cho biết họ tên của nhân viên đó, họ tên người trưởng phòng và họ tên người quản lý trực tiếp của nhân viên đó.
    
    ```sql
    select nv.honv,nv.tenlot,nv.tennv,trp.honv,trp.tenlot,trp.tennv,nql.honv,nql.tenlot,nql.tennv
    from NHANVIEN nv, NHANVIEN nql, NHANVIEN trp, PHONGBAN pb
    where nv.ma_nql=nql.manv 
    		and trp.manv=pb.trphg 
    		and nv.phg=pb.maphg
    ```
    
- **Câu 17:** Tên những nhân viên phòng số 5 có tham gia vào đề án "San pham X" và nhân viên này do "Nguyen Thanh Tung" quản lý trực tiếp.
    
    ```sql
    select nv.tennv
    from NHANVIEN nv, NHANVIEN nql, DEAN da, PHANCONG pc
    where nv.ma_nql=nql.manv and nql.honv='Nguyen' and nql.tenlot='Thanh' and nql.tennv='Tung'
    	and nv.phg=5
    	and tenda='San pham x'
    	and soda=mada
    	and ma_nvien=nv.manv
    ```
    
- **Câu 18:** Cho biết tên các đề án mà nhân viên Đinh Bá Tiến đã tham gia.
    
    ```sql
    select tenda
    from nhanvien, dean, phancong
    where honv='Dinh' 
    	and tenlot='Ba' 
    	and tennv='Tien'
    	and manv=ma_nvien
    	and soda=mada
    ```

- **Câu 19:** Cho biết số lượng đề án của công ty.
    
    ```sql
    select count(mada)
    from dean
    ```
    
- **Câu 20:** Cho biết số lượng đề án do phòng ‘Nghiên Cứu’ chủ trì.
    
    ```sql
    select count(mada)
    from dean, phongban
    where phong=maphg 
    	and tenphg='Nghien cuu'
    ```
    
- **Câu 21:** Cho biết lương trung bình của các nữ nhân viên.
    
    ```sql
    select avg(luong)
    from nhanvien
    where phai='Nu'
    ```
    
- **Câu 22:** Cho biết số thân nhân của nhân viên ‘Đinh Bá Tiến’.
    
    ```sql
    select count(tentn)
    from thannhan, nhanvien
    where manv=ma_nvien
    	and honv='Dinh' 
    	and tenlot='Ba'
    	and tennv='Tien'
    ```
    
- **Câu 23:** Với mỗi đề án, liệt kê tên đề án và tổng số giờ làm việc một tuần của tất cả các nhân viên tham dự đề án đó.
    
    ```sql
    select tenda, sum(thoigian)
    from phancong, dean
    where soda=mada
    group by tenda
    ```
    
- **Câu 24:** Với mỗi đề án, cho biết có bao nhiêu nhân viên tham gia đề án đó.
    
    ```sql
    select soda, count(ma_nvien)
    from phancong
    group by soda
    ```
    
- **Câu 25:** Với mỗi nhân viên, cho biết họ, tên nhân viên và số lượng thân nhân của nhân viên đó.
    
    ```sql
    select honv, tenlot, tennv, count(tentn)
    from nhanvien, thannhan
    where manv=ma_nvien
    group by honv, tenlot, tennv
    ```
    
- **Câu 26:** Với mỗi nhân viên, cho biết họ tên và số lượng đề án mà nhân viên đó đã tham gia.
    
    ```sql
    select honv,tenlot,tennv,count(soda)
    from nhanvien,phancong
    where manv=ma_nvien
    group by honv,tenlot,tennv
    ```
    
- **Câu 27:** Với mỗi nhân viên, cho biết số lượng nhân viên mà nhân viên đó quản lý trực tiếp.
    
    ```sql
    select nql.honv,nql.tenlot,nql.tennv,count(nv.manv)
    from nhanvien nv,nhanvien nql
    where nv.ma_nql=nql.manv
    group by nql.honv,nql.tenlot,nql.tennv
    ```
    
- **Câu 28:** Với mỗi phòng ban, liệt kê tên phòng ban và lương trung bình của những nhân viên làm việc cho phòng ban đó.
    
    ```sql
    select tenphg, avg(luong)
    from nhanvien,phongban
    where phg=maphg
    group by tenphg
    ```
    
- **Câu 29:** Với các phòng ban có mức lương trung bình trên 4000, liệt kê tên phòng ban và số lượng nhân viên của phòng ban đó.
    
    ```sql
    select tenphg, count(manv)
    from nhanvien,phongban
    where phg=maphg
    group by tenphg
    having avg(luong)>4000
    ```
    
- **Câu 30:** Với mỗi phòng ban, cho biết tên phòng ban và số lượng đề án mà phòng ban đó chủ trì.
    
    ```sql
    select tenphg, count(mada)
    from dean, phongban
    where phong=maphg
    group by tenphg
    ```
    
- **Câu 31:** Với mỗi phòng ban, cho biết tên phòng ban, họ tên người trưởng phòng và số lượng đề án mà phòng ban đó chủ trì
    
    ```sql
    select tenphg, honv, tenlot, tennv, count(mada)
    from nhanvien, phongban, dean
    where manv=trphg and maphg=phong
    group by tenphg, honv, tenlot, tennv
    ```
    
- **Câu 32:** Với mỗi phòng ban có mức lương trung bình lớn hơn 4000, cho biết tên phòng ban và số lượng đề án mà phòng ban đó chủ trì.
    
    ```sql
    select tenphg, count(mada) as 'Sl de an'
    from nhanvien,phongban,dean
    where maphg=phg and maphg=phong
    group by tenphg
    having avg(luong)>4000
    ```
    
- **Câu 33:** Cho biết số lượng đề án diễn ra tại từng địa điểm.
    
    ```sql
    select ddiem_da,count(mada)
    from dean
    group by ddiem_da
    ```
    

- **Câu 34:** Cho biết danh sách các đề án (MADA) có: nhân viên với họ (HONV) là ‘Dinh’ hoặc có người trưởng phòng chủ trì đề án với họ (HONV) là ‘Dinh’.
    
    ```sql
    select soda
    from nhanvien,phancong
    where ma_nvien=manv and honv='Dinh'
    union
    select soda
    from phancong,phongban,nhanvien
    where trphg=ma_nvien
    	and trphg=manv
    	and honv='Dinh'
    ```
    
- **Câu 35:** Danh sách những nhân viên (HONV, TENLOT, TENNV) có trên 2 thân nhân.
    
    ```sql
    select honv,tenlot,tennv
    from nhanvien,thannhan
    where manv=ma_nvien
    group by honv,tenlot,tennv
    having count(tentn)>2
    ```
    
- **Câu 36:** Danh sách những nhân viên (HONV, TENLOT, TENNV) không có thân nhân nào.
    
    ```sql
    select honv,tenlot,tennv
    from nhanvien
    where manv not in (
    			select ma_nvien
    			from thannhan
    		)
    ```
    
- **Câu 37:** Danh sách những trưởng phòng (HONV, TENLOT, TENNV) có tối thiểu 1 thân nhân.
    
    ```sql
    select honv,tenlot,tennv
    from nhanvien,phongban
    where manv=trphg
    	and trphg in (
    				select ma_nvien
    				from thannhan
    			)
    ```
    
- **Câu 38:** Tìm họ (HONV) của những trưởng phòng chưa có gia đình.
    
    ```sql
    select honv
    from nhanvien,phongban
    where manv=trphg
    	and trphg not in (
    					select ma_nvien
    					from thannhan
    				)
    ```
    
- **Câu 39:** Cho biết họ tên nhân viên (HONV, TENLOT, TENNV) có mức lương trên mức lương trung bình của phòng "Nghiên cứu"
    
    ```sql
    select honv,tenlot,tennv
    from nhanvien
    where luong > (
    			select avg(luong)
    			from nhanvien,phongban
    			where maphg=phg
    		)
    ```
    
- **Câu 40:** Cho biết tên phòng ban và họ tên trưởng phòng của phòng ban có đông nhân viên nhất.
    
    ```sql
    select tenphg,honv,tenlot,tennv
    from nhanvien,phongban
    where manv=trphg
    	and phg in (
    				select phg from nhanvien
    				group by phg
    				having count(*) = (
    							select top 1 count(*)
    							from nhanvien
    							group by phg
    							order by count(*) desc
    						)
    			)
    ```
    
- **Câu 41:** Cho biết danh sách các mã đề án mà nhân viên có mã là ‘123456789’ chưa làm.
    
    ```sql
    select mada
    from dean
    where mada not in (
    			select soda
    			from phancong,nhanvien
    			where manv=ma_nvien
    					and manv='123456789'
    		)
    ```
    
- **Câu 42:** Tìm họ tên (HONV, TENLOT, TENNV) và địa chỉ (DCHI) của những nhân viên làm việc cho một đề án ở ‘TP HCM’ nhưng phòng ban mà họ trực thuộc lại không tọa lạc ở thành phố ‘TP HCM’.
    
    ```sql
    select honv,tenlot,tennv,dchi
    from nhanvien,phancong,dean
    where manv=ma_nvien
    		and soda=mada
    		and ddiem_da='TP HCM'
    		and phg not in (
    					select maphg
    					from diadiem_phg
    					where diadiem='TP HCM'
    				)
    ```
    
- **Câu 43:** Tổng quát câu 42, tìm họ tên và địa chỉ của các nhân viên làm việc cho một đề án ở một thành phố nhưng phòng ban mà họ trực thuộc lại không toạ lạc ở thành phố đó.
- **Câu 44:** Danh sách những nhân viên (HONV, TENLOT, TENNV) làm việc trong mọi đề án của công ty.
    
    ```sql
    select honv, tenlot, tennv
    from nhanvien
    where not exists (
    			select *
    			from dean
    			where not exists (
    						select *
    						from phancong
    						where manv=ma_nvien 
    								and soda=mada
    					)
    		)
    ```
    
- **Câu 45:** Danh sách những nhân viên (HONV, TENLOT, TENNV) được phân công tất cả đề án do phòng số 4 chủ trì.
    
    ```sql
    select honv,tenlot,tennv
    from nhanvien
    where not exists (
    			select *
    			from dean
    			where phong=4 
    					and not exists (
    								select *
    								from phancong
    								where manv=ma_nvien 
    										and soda=mada
    							)
    		)
    ```
    
- **Câu 46:** Cho biết danh sách nhân viên tham gia vào tất cả các đề án ở TP HCM.
    
    ```sql
    select honv,tenlot,tennv
    from nhanvien
    where not exists (
    			select *
    			from dean
    			where ddiem_da='TP HCM'
    					and not exists (
    								select *
    								from phancong
    								where manv=ma_nvien
    										and soda=mada
    							)
    		)
    ```
    
- **Câu 47:** Cho biết phòng ban chủ trì tất cả các đề án ở TP HCM.
    
    ```sql
    select tenphg
    from phongban pb1
    where not exists (
    			select *
    			from dean
    			where ddiem_da='TP HCM'
    					and not exists (
    								select *
    								from phongban pb2
    								where pb1.maphg=pb2.mapgh
    										and pb2.maphg=phong
    							)
    		)
    ```