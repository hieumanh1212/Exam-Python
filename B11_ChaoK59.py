import math
import queue
n=int(input())
a=[math.inf]
a+=list(map(int,input().split()))
S = queue.LifoQueue()
L=[]
R=[]
S.put(0)
for i in range(1,n+1):
    while S.empty()==False:
         t =S.get()
         if(a[t] > a[i]):
            S.put(t)
            L.append(t)
            S.put(i)
            break
S= queue.LifoQueue()
S.put(0)
for i in range(1,n+1):
    while S.empty()==False:
        t =S.get()
        if(a[t]>a[n+1-i]):
            S.put(t)
            R.append(t)
            S.put(n+1-i)
            break
R.reverse()
result=[]
for i in range(n):
    if(L[i]==R[i]==0):
        result.append(-1)
    elif L[i]==0: result.append(R[i]-1)
    elif R[i]==0: result.append(L[i]-1)
    elif(-L[i]+i+1 <= R[i]-i-1):
        result.append(L[i]-1)
    else: result.append(R[i]-1)
print(*result)
