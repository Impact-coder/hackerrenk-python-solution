if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans=[]
    for i in range (0,x+1):
        temp=[i,]
        for j in range (0,y+1):
            temp=[i,j]
            for k in range (0,z+1):
                temp=[i,j,k]
                if(sum(temp) != n):
                    ans.append(temp)
    
    print(ans)
