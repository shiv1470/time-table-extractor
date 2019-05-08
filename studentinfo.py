def main():
    student_file = open("students.txt" , "r")
    subject_file = open("subjects.txt","r")
    print("Enter Enrollment of student")
    en=input()
    subj=None
    for i in range(int(student_file.readline())):
        x=student_file.readline().split()
        if(x[0]==en):
            subj=x[1].split(',')
            break
    if(subj==None):
        print("Oops! Student details not found!!")
        return
    subcode={}
    print("")
    for i in range(int(subject_file.readline())):
        x=subject_file.readline().split(' -> ')
        subcode[x[0]]=x[1]
    for i in subj:
        print(i,subcode[i],end="")
