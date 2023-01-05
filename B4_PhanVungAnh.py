'''
Y tuong:
- Su dung thuat toan DFS va CTDL LIFOQUEUE
- Khi nhap ma tran, ta them mot buc tuong xung quanh no de tranh
loi khi truy cap vao index khong ton tai
- Duyet lan luot tung phan tu trong ma tran, neu = 0 thi gan = -1
roi duyet lang gieng 8, neu = 0 thi gan = -1, dem += 1. Put vao Q
- Sau khi duyet luu vao List
'''
import queue
class Anh:
    def nhap(self):
        self.n,self.m = map(int,input().split())
        self.A = [[1]*(self.m+2)]
        for i in range(self.n):
            ip = list(map(int,input().split()))
            self.A.append(([1]+ip+[1]))
        self.A.append([1]*(self.m+2))
    def sol(self):
        res = []
        Q = queue.LifoQueue()
        for i in range(1,self.n+1):
            for j in range(1,self.m+1):
                if self.A[i][j] == 0: res.append(self.Search(i,j,Q))
        res.sort()
        print(len(res))
        print(*res,end = ' ')
    def Search(self,u,v,Q):
        dem = 1
        Q.put((u,v))
        self.A[u][v] = -1
        while Q.qsize():
            z,t = Q.get()
            for i in {-1,0,1}:
                for j in {-1,0,1}:
                    if self.A[z+i][t+j] == 0:
                        Q.put((z+i,t+j))
                        dem += 1
                        self.A[z+i][t+j] = -1
        return dem
if __name__ == '__main__':
    A = Anh()
    A.nhap()
    A.sol()
