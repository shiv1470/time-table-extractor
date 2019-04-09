import xlrd
def findname(FacultCode):
    location=("/home/shivam/Documents/divyanshooter/Faculty Abbreviation Even 2019.xls")
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
    fcode=input()
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
def printtimetable(fcode):
    tt=[["Monday:"],["Tuesday"],["Wednesday"],["Thursday"],["Friday"],["Saturday"]]
    sem2loc=("/home/shivam/Documents/divyanshooter/B TECH II SEM.xls")
    sem2WB=xlrd.open_workbook(sem2loc)
    sem2sheet=sem2WB.sheet_by_index(0)
    for i in range(sem2sheet.nrows):
        for j in range(sem2sheet.ncols):
            val=sem2sheet.cell_value(i,j)
            if fcode in val:
                for idx in range(i,-1,-1):
                    v=findday(sem2sheet.cell_value(idx,0))
                    if(v>=0):
                        tt[v].append(val)
                        break
    sem4loc=("/home/shivam/Documents/divyanshooter/B TECH IV SEM.xls")
    sem4WB=xlrd.open_workbook(sem4loc)

    sem6loc=("/home/shivam/Documents/divyanshooter/B tech VI Sem.xls")
    sem6WB=xlrd.open_workbook(sem6loc)

    sem8loc=("/home/shivam/Documents/divyanshooter/B TECH VIII SEM.xls")
    sem8WB=xlrd.open_workbook(sem8loc)

    for i in tt:
        for j in i:
            print(j)
printtimetable(fcode)
