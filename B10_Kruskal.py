'''
Y tuong:
- Su dung thuat toan tham lam va CTDL Disjoinset
- Bat dau tu canh co trong so nho nhat, tiep tuc them cac canh
den khi dat duc muc tieu
=> Tham lam theo trong so cua canh
- Cac buoc thuc hien nhu sau:
+ Sap xep cac canh theo trong so tu nho den lon
+ Lay ra canh co trong so nho nhat va them vao cay
+ Neu them canh nao ma tao thanh 1 chu trinh thi bo qua canh do
+ Tiep tuc them canh den khi nao di qua tat ca cac dinh thi dung
'''
F = [0]*10002
def root(x):
    return x if F[x] == 0 else root(F[x])
if __name__ == '__main__':
    n, m = map(int,input().split())
    A = []
    for i in range(m):
        u,v,w = map(int,input().split())
        A.append((u,v,w,))
    A.sort(key = lambda x:x[2])
    res = 0
    for u,v,w in A:
        x = root(u)
        y = root(v)
        if x!=y:
            res += w
            while u != x:
                z = F[u]
                F[u] = x
                u = z
            while v != y:
                z = F[v]
                F[v] = x
                v = z
            F[y] = x
    print(res)
