n,m=map(int,input().split())
x,y,dir=map(int,input().split())

visited=[[0]*m for _ in range(n)]
visited[x][y]=1

data=[]
for i in range(n):
    data.append(list(map(int, input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global dir
    dir-=1
    if dir==-1:
        dir=3

# 시뮬레이션 시작
cnt=1
turn_time=0


while True:
    turn_left()
    nx,ny=x+dx[dir],y+dy[dir]

    if visited[nx][ny]==0 and data[nx][ny]==0:
        visited[nx][ny]=1
        x,y=nx,ny
        cnt+=1
        turn_time=0
        continue

    turn_time+=1

    if turn_time==4:
        nx,ny=x-dx[dir],y-dy[dir]
        if data[nx][ny]==0:
            x,y=nx,ny
            turn_time=0
        else: break

print(cnt)