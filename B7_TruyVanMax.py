'''
- Su dung cau truc cay IT de giai quyet bai toan
- Ham update de cap nhat cay IT moi khi them phan tu
+ A[k] la phan tu lon nhat nam trong [L,R]
+ Neu phan tu moi co gia tri lon hon A[k] thi A[k] bang gia tri moi
+ Goi de quy cap nhat lai cac gia tri con cua A[k], neu vi tri
cua phan tu moi nam ben trai thi thuc hien cap nhat khoang ben trai
doan dang xet, neu nam o ben phai thi cap nhat ben phai. De quy se
thuc hien cho den khi doan L-R khong con phu hop
- Ham get de dua ra gia tri Ak tuong ung voi u-v truyen vao
+ Neu u-v truyen vao dung khoang L-K thi tra ve Ak
+ Neu u-v truyen vao khoang ben trai thi xet khoang ben trai
+ Neu u-v truyen vao khoang ben phai thi xet khoang ben phai
+ Neu u-v truyen vao khong trai hay phai thi chia thanh 2 de xu
ly roi lay gia tri lon hon
'''
class findMax:
    def update(self,k,L,R,i,x):
        if A[k] < x:
            A[k] = x
        if L<R:
            if i < (L+R)//2:
                self.update(2*k+1,L,(L+R)//2,i,x)
            else:
                self.update(2*k+2,(L+R)//2+1,R,i,x)
    def get(self,k,L,R,u,v):
        if u == L and v == R:
            return A[k]
        if v <= (L+R)//2:
            return self.get(2*k+1,L,(L+R)//2,u,v)
        if u > (L+R)//2:
            return self.get(2*k+2,(L+R)//2+1,(L+R)//2,u,v)
        return max(self.get(2*k+1,L,(L+R)//2, u, (L+R)//2),
                   self.get(2*k+2,(L+R)//2+1,R,(L+R)//2+1,v))