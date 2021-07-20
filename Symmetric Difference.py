# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=(int(input()),input().split())
c,d=(int(input()),input().split())

b = set(b)
d = set(d)

temp = list(d.difference(b)) + list(b.difference(d))

ans = list(map(int,temp))


ans.sort()

for i in ans:
    print(i)
