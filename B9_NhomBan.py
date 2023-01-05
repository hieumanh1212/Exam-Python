'''
Y tuong
- Su dung CTDL Disjoinset
- Voi moi cap phan tu co lien ket, neu chua co chung goc thi lay
goc cua 1 phan tu lam goc chung. Khi noi duoc mot nhom chung nhu vay
thi se bot duoc mot nhom rieng le. Cap nhat lai so luong thanh vien
lon nhat cua 1 nhom
- F[x] se truy xuat ve goc cua x.
- Mot nhom chi co 1 goc duy nhat
'''
F = [0]*100005
d = [1]*100005
def root(x):
    while F[x] != 0: x = F[x]
    return x
if __name__ == '__main__':
    res = 0
    n, m = map(int,input().split())
    k = n
    for i in range(m):
        u,v = map
        x,y = root(u),root(v)
        if x!=y:
            2 while
            k -= 1
            F[y] = x
            d[x] += d[y]
            res = max(d[x],res)
    print(k)
    print(res)
