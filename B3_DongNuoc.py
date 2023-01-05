'''
Y tuong
- Su dung thuat toan BFS va CTDL Queue de giai quyet bai toan
- Trang thai ban dau la 2 binh rong (0,0) voi so buoc la den trang thai nay la 0
- Tao mot Dictionary de luu trang thai cua 2 binh va so buoc de den trang thai do
- Duyet queue:
+ Voi moi trang thai, co 6 cach thuc hien buoc tiep theo:
1. Do het nuoc tu binh 1 di
2. Do het nuoc tu binh 2 di
3. Do day nuoc vao binh 1
4. Do day nuoc vao binh 2
5. Do nuoc tu binh 1 sang binh 2
6. Do nuoc tu binh 2 sang binh 1
+ Voi moi trang thai, kiem tra xem trang thai nay da duoc luu chua,
neu chua thi luu trang thai cung voi so buoc den trang thai do biet
so buoc = so buoc den trang thai truoc + 1. Sau do kiem tra xem
trang thai nay co phai ket qua khong
+ Sau khi duyet Queue xong ma chua dua ra ket qua thi "Khong dong duoc nuoc"
'''
import queue
def Search(n,m,k,Q):
    Q.put((0,0))
    D={(0,0):0}
    while Q.qsize():
        x,y = Q.get()
        z=x+y
        Next = [(0,y),(x,0),(n,y),(x,m),(max(0,z-m),min(z,m)),(min(z,n),max(0,z-n))]
        for v in Next:
            if v not in D.keys():
                D[v] = D[(x,y)] + 1
                Q.put(v)
                if v[0] == k or v[1] == k: return D[v]
    return "Khong dong duoc nuoc"
if __name__ == '__main__':
    n,m,k = map(int,input().split())
    Q = queue.Queue()
    print(Search(n,m,k,Q))
