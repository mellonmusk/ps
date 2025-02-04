# 기간을 기준으로 sort하는 것보다 3/1-11/30 사이에서 시작일과 종료일을 조정해가는 방식이 적합함.
n=int(input())
result=0
flowers=[]
for i in range(n):
    a1,a2,a3,a4=map(int,input().split())
    flowers.append([a1*100+a2, a3*100+a4])
cur=301
while True:
    next=cur
    for start,end in flowers:
        if start<=cur and end>next:
            next=end
    if cur==next:
        result=0
        break
    result+=1
    if next>=1201: break
    cur=next

print(result)
