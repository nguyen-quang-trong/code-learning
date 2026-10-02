# Viết một hàm đặt tên là NegativeNumberInStrings(str). Hàm này có đối số truyền vào là một chuỗi bất kỳ, Hãy viết lệnh để xuất ra các số nguyên âm trong chuỗi. 
# Ví dụ: Nếu nhập vào chuỗi “abc-5xyz-12k9l--p” thì hàm phải xuất ra được 2 số nguyên âm đó là -5 và -12.

def NegativeNumberInStrings(str):
    s=""
    for i in range(len(str)):
        if str[i]!="-":continue
        else:
            tmp=""
            while True:
                i+=1
                # print(str[i])
                if str[i] in "0,1,2,3,4,5,6,7,8,9":
                    tmp=tmp+str[i]
                else:
                    break
            if tmp!="":
                if s!="":s=s+";"
                s=s+"-"+tmp
    return s

str="abc-5xyz-12k9l--p"
print("So am trong chuoi la:",NegativeNumberInStrings(str))