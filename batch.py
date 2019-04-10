import xlrd
def findTypeOfClass(code):
    if code=='P':
        return "Lab"
    elif code=='L':
        return "Lecture"
    else :
        return "Tutorial"
def batchFinder(batch,val):
    if len(val)<5:
        return False
    else:
       if(len(batch)==2):
         if ((batch[0]==val[1] and batch[1]==val[2] and val[3] not in "0123456789") or(batch[0]==val[1] and batch[1]==val[4] and val[5] not in "0123456789")):
            return  True
       elif(len(batch)==3):
          if ((batch[0]==val[1] and batch[1]==val[2] and batch[2]==val[3] and val[4] not in "0123456789") or(batch[0]==val[1] and batch[1]==val[5] and batch[2]==val[6] and val[7] not in "0123456789")):
            return True

    return False
print('Enter Batch:')
bcode=input()
def findday(s):
    if "MON" in s:
        return 0
    if "TUE" in s:
        return 1
    if "WED" in s:
        return 2
    if "THU" in s:
        return 3
    if "FRI" in s:
        return 4
    if "SAT" in s:
        return 5
    return -1
tt=[["Monday:"],["Tuesday:"],["Wednesday:"],["Thursday:"],["Friday:"],["Saturday:"]]
sem2loc=("B TECH II SEM.xls")
sem2WB=xlrd.open_workbook(sem2loc)
sem2sheet=sem2WB.sheet_by_index(0)
sem="   SEM2   "
for i in range(sem2sheet.nrows):
    for j in range(sem2sheet.ncols):
        val=sem2sheet.cell_value(i,j)
        if batchFinder(bcode,val):
            time=sem2sheet.cell_value(1,j)
            if(val[0]=='P'):
                x=time.split("-")
                y=sem2sheet.cell_value(1,j+1)
                y=y.split("-")
                time=x[0]+"-"+y[1]
            space=""
            for k in range(len(time),10):
                space+=" "
            time=time+space
            classType=findTypeOfClass(val[0])
            space=""
            for k in range(len(classType),12):
                space+=" "
            classType+=space
            for idx in range(i,-1,-1):
                v=findday(sem2sheet.cell_value(idx,0))
                if(v>=0):
                    tt[v].append(time+": "+sem+classType+" "+val)
                    break

print("\n")
print("Time Table for ",bcode,":")
for i in tt:
    if(len(i)<2):
        continue
    for j in i:
        print(j)
    print("---------------------------------------------------------------------")
