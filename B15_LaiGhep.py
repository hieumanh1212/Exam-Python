'''
- Su dung phuong phap quay lui de giai quyet bai toan
- So sanh ki tu tai vi tri i cua 2 xau goc. Neu giong nhau thi ki
tu tai vi tri i cua xau con phai la ki tu nay. Neu khac thi thu
tung ki tu cho den khi xau con so ky tu thi ghi nhan 1 truong hop
'''
R = []
def Try(i,n,s1,s2,s3):
    if i == n:
        R.append(s3)
    else:
        if s1[i] == s2[i]:
            Try(i+1,n,s1,s2,s3+s1[i])
        else:
            Try(i+1,n,s1,s2,s3+s1[i])
            Try(i+1,n,s1,s2,s3+s2[i])
if __name__ == '__main__':
    s1 = input()
    s2 = input()
    Try(0,len(s1),s1,s2,"")
    R.sort()
    print(*R, sep = '')