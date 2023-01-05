'''
Y tuong
- Su dung hang doi uu tien PriorityQueue
- Nap k-1 phan tu dau tien (gia tri, vi tri) vao queue, uu tien theo
gia tri cua phan tu
- Tu phan tu thu k bat dau trinh tham: Tim phan tu lon nhat trong k phan
tu lien tiep, do la phan tu dau tien nam trong Queue
- Tuy nhien truoc khi thuc hien trinh tham ta can loai bo nhung phan tu
nam trong khoang dang duoc xet
'''
import queue
if __name__ == '__main__':
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    Q = queue.PriorityQueue()
    for i in range(k-1):
        Q.put((-A[i],i))
    for i in range(k-1,n):
        Q.put((-A[i],i))
        while Q.queue[0][1] <= i-k: Q.get()
        print(-Q.queue[0][0],end = ' ')
