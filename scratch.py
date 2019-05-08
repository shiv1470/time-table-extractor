def main():
    import xlrd
    import string_matchRK as rk
    def findTypeOfClass(code):
        if code=='P':
            return "Lab"
        elif code=='L':
            return "Lecture"
        else :
            return "Tutorial"
    def findname(FacultCode):
        location=("Faculty Abbreviation Even 2019.xls")
        abbWB = xlrd.open_workbook(location)
        mainsheet=abbWB.sheet_by_index(0)
        for i in range(mainsheet.nrows):
            try:
                s0=mainsheet.cell_value(i,0)
                if(FacultCode==s0):
                    return mainsheet.cell_value(i,1)
                s2=mainsheet.cell_value(i,2)
                if(FacultCode==s2):
                    return mainsheet.cell_value(i,3)
                s4=mainsheet.cell_value(i,4)
                if(FacultCode==s4):
                    return mainsheet.cell_value(i,5)
            except:
                print("Error reading value at row no.",i)
                return -1
        return None
    fcode="MKT"
    fname=None
    while(True):
        print("Please Enter the code for faculty")
        fcode=input().upper()
        fname=findname(fcode)
        if fname==None:
            print("Oops Invalid faculty Code! Try again.")
        else:
            print("Welcome!",fname)
            break
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
            if '/'+fcode in val or ' '+fcode in val or ','+fcode in val :
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
    sem4loc=("B TECH IV SEM.xls")
    sem4WB=xlrd.open_workbook(sem4loc)
    sem4sheet=sem4WB.sheet_by_index(0)
    sem="   SEM4   "
    for i in range(sem4sheet.nrows):
        for j in range(sem4sheet.ncols):
            val=sem4sheet.cell_value(i,j)
            if '/'+fcode in val or ' '+fcode in val or ','+fcode in val :
                time=sem4sheet.cell_value(1,j)
                if(val[0]=='P'):
                    x=time.split("-")
                    y=sem4sheet.cell_value(1,j+1)
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
                    v=findday(sem4sheet.cell_value(idx,0))
                    if(v>=0):
                        tt[v].append(time+": "+sem+classType+" "+val)
                        break
    sem6loc=("B tech VI Sem.xls")
    sem6WB=xlrd.open_workbook(sem6loc)
    sem6sheet=sem6WB.sheet_by_index(0)
    sem="   SEM6  "
    for i in range(sem6sheet.nrows):
        for j in range(sem6sheet.ncols):
            val=sem6sheet.cell_value(i,j)
            if '/'+fcode in val or ' '+fcode in val or ','+fcode in val :
                time=sem6sheet.cell_value(1,j)
                if(val[0]=='P'):
                    x=time.split("-")
                    y=sem6sheet.cell_value(1,j+1)
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
                    v=findday(sem6sheet.cell_value(idx,0))
                    if(v>=0):
                        tt[v].append(time+": "+sem+classType+" "+val)
                        break
    sem8loc=("B TECH VIII SEM.xls")
    sem8WB=xlrd.open_workbook(sem8loc)
    sem8sheet=sem8WB.sheet_by_index(0)
    sem="   SEM8  "
    rk.match("0","0")
    for i in range(sem8sheet.nrows):
        for j in range(sem8sheet.ncols):
            val=sem8sheet.cell_value(i,j)
            if '/'+fcode in val or ' '+fcode in val or ','+fcode in val :
                time=sem8sheet.cell_value(1,j)
                if(val[0]=='P'):
                    x=time.split("-")
                    y=sem8sheet.cell_value(1,j+1)
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
                    v=findday(sem8sheet.cell_value(idx,0))
                    if(v>=0):
                        tt[v].append(time+": "+sem+classType+" "+val)
                        break
    print("\n")
    print("Time Table for ",fname,":")
    for i in tt:
        if(len(i)<2):
            continue
        for j in i:
            print(j)
        print("---------------------------------------------------------------------")
