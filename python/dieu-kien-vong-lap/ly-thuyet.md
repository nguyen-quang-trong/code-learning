## Hãy cho biết kết quả của Boolean Expression
Cho x, y, z = 3, 5, 7. Hãy cho biết kết quả của Boolean Expression:

(a) x == 3 true

(b) x < y true

(c) x >= y false

(d) x <= y true

(e) x != y - 2 false

(f) x < 10 true

(g) x >= 0 and x < 10 true

(h) x < 0 and x < 10 false

(i) x >= 0 and x < 2 fasle

(j) x < 0 or x < 10 true

(k) x > 0 or x < 10 true

(l) x < 0 or x > 10 false

## Hãy cho biết kết quả xuất ra màn hình
Cho i, j, k là các con số và lệnh dưới đây:
```Python
if i < j:
  if j < k:
    i=j
  else:
    j = k
else:
  if j > k:
    j = i
  else:
    i = k
print("i =", i, " j =", j, " k =", k)
```
Hãy cho biết kết quả xuất ra màn hình nếu tuần tự 3 biến trên có các giá trị sau: 

(a) i = 3, j = 5, and k = 7 

i = 3 j = 5 k = 7

(b) i = 3, j = 7, and k = 5 

i = 3 j = 5 k = 5

(c) i = 5, j = 3, and k = 7 

i = 7 j = 3 k = 7

(d) i = 5, j = 7, and k =3 

i = 5 j = 3 k = 3

(e) i = 7, j = 3, and k = 5 

i = 5 j = 3 k = 5

(f) i =7, j = 5, and k = 3 

i = 7 j = 7 k = 3

## Cho biết bao nhiêu dấu * được in ra trên màn hình
```Python
a = 0
while a < 100:
  print('*', end='')
print()
```
Vô hạn dấu * được in ra màn hình

## Cho biết bao nhiêu dấu * được in ra trên màn hình
```Python
a = 0
while a < 100:
  b = 0
  while b < 40:
    if (a + b) % 2 == 0:
      print('*', end='')
    b += 1
  print()
  a += 1
```
2000

## Giải thích cách chạy của dòng lệnh range
(a) range(5) tạo dãy từ 0 đến 4

(b) range(5, 10) tạo dãy từ 5 đến 9

(c) range(5, 20, 3) tạo dãy từ 5, cộng thêm 3, và kết thúc trước số 20 

(d) range(20, 5, -1) tạo dãy từ 20, giảm 1, và kết thúc trước số 5

(e) range(20, 5, -3) tạo dãy từ 20, giảm 3, và kết thúc trước số 5

(f) range(10, 5) không có giá trị

(g) range(0) không có giá trị

(h) range(10, 101, 10) tạo dãy từ 10, cộng thêm 10, và kết thúc trước số 101

(i) range(10, -1, -1) tạo dãy từ 10, giảm 1, và kết thúc trước số -1

(j) range(-3, 4) tạo dãy từ -3 đến 3

(k) range(0, 10, 1) tạo dãy từ 0,cộng thêm 1, và kết thúc trước số 10

## Cho biết bao nhiêu dấu * được in ra trên màn hình
```Python
for a in range(20, 100, 5):
  print('*', end='')
print()
```
16
