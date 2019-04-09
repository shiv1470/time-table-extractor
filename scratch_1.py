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
def printtimetable(fcode):
    location=("/home/shivam/Documents/divyanshooter/Faculty Abbreviation Even 2019.xls")
