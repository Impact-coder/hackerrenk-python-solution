if __name__ == '__main__':
    greads=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        greads.append([name,score])
    
    scores=list(set(scores))   
    scores.sort()
    ans=[]
    for i in range(0,len(greads)):
        if greads[i][1] == scores[1]:
            ans.append(greads[i][0])
        
    ans.sort()
    for i in ans:
        print(i)
