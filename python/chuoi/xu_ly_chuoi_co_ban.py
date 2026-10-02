# Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
# - Bao nhiêu chữ IN HOA.
# - Bao nhiêu chữ in thường.
# - Bao nhiêu chữ là chữ số.
# - Bao nhiêu chữ là ký tự đặc biệt.
# - Bao nhiêu chữ là khoảng trắng.
# - Bao nhiêu chữ là Nguyên Âm.
# - Bao nhiêu chữ là Phụ âm.

s=input("Nhập chuỗi: ")

hoa = 0
thuong = 0
so = 0
dacbiet = 0
khoangtrang = 0
nguyenam = 0
phuam = 0

for c in s:
    if c.isupper():
        hoa += 1

    elif c.islower():
        thuong += 1

    elif c.isdigit():
        so += 1

    elif c.isspace():
        khoangtrang += 1

    else:
        dacbiet += 1

    # Đếm nguyên âm và phụ âm
    if c.isalpha():
        if c.lower() in "aeiou":
            nguyenam += 1
        else:
            phuam += 1

print("Số chữ IN HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ là chữ số:", so)
print("Số ký tự đặc biệt:", dacbiet)
print("Số khoảng trắng:", khoangtrang)
print("Số chữ là Nguyên Âm:", nguyenam)
print("Số chữ là Phụ âm:", phuam)