import queue
def Balan(ip):
    S=queue.LifoQueue()
    out=""
    UT={'(':0,'+':1,'-':1,'*':2,'/':2}
    for c in ip:
        if '0'<=c<='9': out+=c
        elif c=='(':S.put(c)
        elif c==')':
            while S.queue[-1]!='(': out+=S.get()
            S.get()  #lay dau ( ra khoi stack
        else:  #cac phep toan
            while S.qsize() and UT[S.queue[-1]]>=UT[c]: out+=S.get()
            S.put(c)
    while S.qsize():out+=S.get()
    print(out)
    return out
def tinh(out):
    S=queue.LifoQueue()
    for c in out:
        if '0'<=c<='9': S.put(int(c))
        elif c=='+': S.put(S.get()+S.get())
        elif c=='*': S.put(S.get()*S.get())
        elif c=='-': S.put(-(S.get()-S.get()))
        else:
            a,b=S.get(),S.get()
            S.put(b//a)
    return S.get()
if __name__ == '__main__':
    out=Balan(input())
    print(tinh(out))