# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

x=int(input())
y=int(input())

for i in divmod(x,y):
    print(i)

print(divmod(x,y))