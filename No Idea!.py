# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
array = input().split()
like = set(input().split())
dislike = set(input().split())

happiness=0

for i in array:
    if(i in like):
        happiness+=1
    elif(i in dislike):
        happiness-=1
print(happiness)