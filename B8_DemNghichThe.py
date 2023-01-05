'''
Y tuong:
- Su dung cau truc cay IT de giai quyet bai toan
- Xet phan tu nao thi cong them so phan tu dung truoc no ma lon ho no
(Tuc la cac phan tu lon hon no ma da duoc duyet va luu trong cay IT)
- A[k] la so phan tu nam trong [L,R)
- Moi khi them phan tu thi phai cap nhat A[k]
- Neu doan dang xet con nhieu hon 1 phan tu (L+1<R):
+ Neu x thuoc khoang trai, cong them so phan tu khoang phai vao bien ket
qua roi de quy ben trai
+ Neu x khong thuoc khoang trai, de quy khoang phai
'''
A = [0]*400005
res = 0
def update(k,L,R,x):
    global A,res
    A[k] += 1
    if L+1 == R: return
    if L+1<R:
        if x < (L+R)//2:
            res += A[2*k+2]
            update(2*k+1,L,(L+R)//2,x)
        else:
            update(2*k+2, (L+R)//2, R, x)