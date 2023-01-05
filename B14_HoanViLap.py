'''
- Su dung thuat toan quay lui de giai quyet bai toan
- Tao mot Dictionary de luu so luong cac ki tu co trong xau
- Dua ra cac ki tu chua duoc cho vao trong xau hoan vi cho den khi
du n ki tu thi ghi nhan 1 truong hop
'''
def Try(B,n,i,val):
    if i == n: print(val)
    else:
        for x in B:
            if B[x[0]] > 0:
                B[x[0]] -= 1
                Try(B,n,i+1,val+x[0])
                B[x[0]] += 1
if __name__ == '__main__':
    n = input()
    A = list(n)
    A.sort()
    B = {}
    for x in A:
        if x not in B:
            B[x] = 0
        B[x] += 1
    Try(B,len(n), 0, "")