## Những giá trị nào có thể xuất hiện trong randrange(0, 100)? 4.5; 34; -1; 100; 0; 99
34; 0; 99

## Kiểm tra kết quả thực hiện từng trường hợp trong đoạn code dưới đây:
```python
def sum1(n): 
    s = 0 
    while n > 0: 
        s += 1 
        n -= 1 
    return s 
def sum2(): 
    global val 
    s = 0 
    while val > 0: 
        s += 1 
        val -= 1 
    return s 
 
def sum3(): 
    s = 0 
    for i in range(val, 0, -1): 
     s += 1 
    return s 
```
**Trường hợp 1:**

```python
def main(): 
    global val 
    val = 5 
    print(sum1(5)) 
    print(sum2()) 
    print(sum3()) 
main() 
```

Kết quả:

5

5

0

**Trường hợp 2:**

```python
def main(): 
    global val 
    val = 5 
    print(sum1(5)) 
    print(sum3()) 
    print(sum2()) 
main() 
```

Kết quả:

5

5

0

**Trường hợp 3:**

```python
def main(): 
    global val 
    val = 5 
    print(sum2()) 
    print(sum1(5)) 
    print(sum3()) 
main() 
```

Kết quả: 

5

5

0