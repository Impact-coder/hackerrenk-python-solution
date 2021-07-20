n = int(input())
m = set(map(int, input().split()))

N = int(input())
L=list(m)
for j in range(N):
    s = input().split()
    command = s[0]
        
    if command=="pop":
        if(len(m)!=0):
            m.pop()
    elif command=="remove":
        e=int(s[1])
        if(e in m):
            m.remove(e)
    elif command=="discard":
        e=int(s[1])
        if(e in m):
            m.discard(e)
            
print(sum(m))
    
