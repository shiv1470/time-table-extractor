subject_file = open("subjects.txt","r")
n=int(subject_file.readline())
sub=[]
subcode={}
colors=[0]*n
for i in range(n):
    x=subject_file.readline().split(" -> ")
    sub.append(x)
    subcode[x[0]]=[i,x[1]]
graph=[None]*n
for i in range(n):
    graph[i]=[0]*n
student_file = open("students.txt" , "r")
n2=int(student_file.readline())
for i in range(n2):
    x=student_file.readline().split()
    x[1]=x[1].split(",")
    for j in x[1]:
        for k in x[1]:
            if(j==k):
                continue
            graph[subcode[j][0]][subcode[k][0]]=1
            graph[subcode[k][0]][subcode[j][0]]=1
colors[0]=1
colorsused=1
for i in range(1,n):
    c=[]
    for j in range(n):
        if graph[i][j]==1 and colors[j] not in c:
            c.append(colors[j])
    for col in range(1,colorsused+2):
        if col not in c:
            colors[i]=col
            colorsused=max(colorsused,col)
            break
print(colors)
