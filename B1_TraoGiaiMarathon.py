'''
Y tuong:
- Su dung namedtuple de tao cau truc sinh vien gom 3 thuoc tinh:
ten, diem, khoa
- Tao 2 list A va B:
+ List A de luu tru thong tin cac sinh vien thuoc khoa dien - dien tu
+ List B de luu tru thong tin cac sinh vien thuoc khoa con lai
Sap xep theo diem
'''
from collections import namedtuple
Student = namedtuple('Student', 'ten diem khoa')
if __name__ == '__main__':
    n = int(input())
    A,B = [],[]
    for i in range(n):
        a,b,c = input().rsplit(None,2)
        if c == "DDT": A.append(Student(a,int(b),c))
        else: B.append(Student(a,int(b),c))
    A.sort(key = lambda x:x.diem, reverse = True)
    B.sort(key = lambda x:x.diem, reverse = True)
    print("Giai nhat: " + A[0].ten)
    print("Giai nhi: " + A[1].ten)
    print("Giai ba: " + A[2].ten)
    print("Giai giao luu: " + B[0].ten)