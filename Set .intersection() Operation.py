# Enter your code here. Read input from STDIN. Print output to STDOUT

a,b=(int(input()),input().split())
c,d=(int(input()),input().split())

b = set(b)
d = set(d)

print(len(b.intersection(d)))