'''
Y tuong:
- Su dung thuat toan BFS va CTDL Queue de giai quyet bai toan
- Nap diem xuat phat la goc vao Queue
- Tao mot Dictionary de luu cac diem da di qua
- Duyet Queue:
+ Voi moi lan duyet u = Q.get(), kiem tra xem co the tach u thanh
bieu thuc u = a*b hay khong, neu co thi kiem tra xem da di qua
diem v = (a-1)(b+1) hay chua. Neu chua thi them vao Queue va
Dictionary
+ Sau khi duyet, sap xep cac diem da di qua theo thu tu tu nho den lon
'''
import queue
import math
if __name__ == '__main__':
    n = int(input())
    Q = queue.Queue()
    Q.put(n)
    D={n:True}
    while Q.qsize():
        u = Q.get()
        for a in range(1,1+int(math.sqrt(u))):
            if u % a == 0:
                v = (a-1)*(u//a+1)
                if v not in D.keys():
                    D[v] = True
                    Q.put(v)
    res = [x for x in D.keys()]
    res.sort()
    print(*res,end = ' ')