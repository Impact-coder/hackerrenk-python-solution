# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *
N,M = map(int,input().split())

for i in range(0,floor(N/2)):
    st=(i*2+1)*(".|.")
    print(st.center(M,"-"))
    
print("WELCOME".center(M,"-"))

for i in range(floor(N/2)-1,-1,-1):
    st=(i*2+1)*(".|.")
    print(st.center(M,"-"))