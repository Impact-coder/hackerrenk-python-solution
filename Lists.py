
if __name__ == '__main__':
    N = int(input())
    L=[]
    for j in range(N):
        s = input().split()
        command = s[0]
        
        if command=="insert":
            i=int(s[1])
            e=int(s[2])
            L.insert(i,e)
        elif command=="remove":
            e=int(s[1])
            L.remove(e)
        elif command=="append":
            e=int(s[1])
            L.append(e)
        elif command=="sort":
            L.sort()
        elif command=="pop":
            L.pop()
        elif command=="reverse":
            L.reverse()
        elif command=="print":
            print(L)
        
