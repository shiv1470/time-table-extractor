subject_file = open("subjects.txt","r")
n=int(subject_file.readline())
sub=[]
subcode={}
for i in range(n):
    x=subject_file.readline().split(" -> ")
    sub.append(x)
    subcode[x[0]]=[i,x[1]]
graph=[None]*n
for i in range(n):
    graph[i]=[0]*n
student_file = open("students.txt" , "r")
n=int(student_file.readline())
for i in range(n):
    x=student_file.readline().split()
    x[1]=x[1].split(",")
    for j in x[1]:
        for k in x[1]:
            if(j==k):
                continue
            graph[subcode[j][0]][subcode[k][0]]=1
            graph[subcode[k][0]][subcode[j][0]]=1
