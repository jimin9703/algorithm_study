from collections import deque
 
d = deque()
n = int(input())
max = deque()
li = []
 
for i in range(n):
    b = list(map(int,input().split()))
    if b[0] == 1:
        d.append(b[1])
        if len(max) < len(d):
            if len(max) == 0:
                for j in range(len(d)):
                    max.append(d[j])
            else:
                max.clear()
                for l in range(len(d)):
                    max.append(d[l])
        elif len(max) == len(d):
            if max[-1] > d[-1]:
                max.clear()
                for k in range(d):
                    max.append(d[k])
    else:
        d.popleft()
 
print(len(max), end=" ")
print(max[-1])