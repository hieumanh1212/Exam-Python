'''
Y tuong:
- Su dung Stack (LIFOQUEUE)
- Xet moi phan tu cua day. Dua 2 phan tu lien tiep a[i] va a[i+1] vao stack
+ Neu a[i] < a[i+1] thi res = 1  (chi co 2 nguoi nhin thay nhau)
+ Neu a[i] >= a[i+1] thi them cac phan tu ke tiep a[i+1] vao stack, phan
tu sau phai co dieu kien <= a[i+1], ket thuc bang viec kiem tra het day
hoac khong thoa man dieu kien truoc do
=> Luc nay so cap nguoi nhin thay nhau = so phan tu stack - 1
res += so cap nguoi nhin thay nhau

'''

import queue
if __name__ == '__main__':
    Q = queue.LifoQueue()
    n = int(input())
    res = 0
    for x in map()
        while Q.qsize() and Q.queue[-1][0] < x:
            res += Q.queue[-1][1]
            Q.get()
        if Q.qsize() and Q.queue[-1][0] == x:
            res += Q.queue[-1][1] + (Q.qsize()>1)
            Q.queue[-1][1] +=1
        else:
            res += Q.qsize() > 0
            Q.put([x,1])
    print(res)
