'''
Y tuong:
- Su dung thuat toan va tham lam va CTDL PriorityQueue
- Tao mot mang A 2 chieu de luu thong tin thoi gian t va gia tri v cua
mot mon hang
- Duyet A tu cuoi len theo thoi gian tu lon den nho, cac gia tri se duoc
them vao Queue
- Tai moi thoi diem i thi giao mon hang co gia tri lon nhat nhan duoc
trong Queue, tuc la phan tu dau tien nam trong Queue vi la hang doi uu
tien.
=> Tham lam theo gia tri lon nhat con thuc hien duoc
- Tuy nhien khi them gia tri vao Queue phai them gia tri am cua no vi
la hang doi uu tien nen se lay ra gia tri nho nhat truoc
'''
import queue
if __name__ == '__main__':
    n = int(input())
    A = [[] for x in range(100006)]
    for i in range(n):
        t,v = map(int,input().split())
        A[t].append(v)
    Q = queue.PriorityQueue()
    res = 0
    for i in range(100001,0,-1):
        for x in A[i]: Q.put(-x)
        if Q.qsize(): res += Q.get()
    print(-res)