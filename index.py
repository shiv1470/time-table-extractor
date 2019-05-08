while(True):
    print("\n\n\n                                            ***** Time Table Extractor *****")
    print("Enter 1 for Faculty Time Table")
    print("Enter 2 for Batch Time Table")
    print("Enter 3 for Exam Time Table")
    print("Enter 4 for Student Registered Subjects")
    print("Enter 5 for Exit")
    x=int(input())
    if(x>4 or x<0):
        if(x!=5):
            print("invalid choice!!!\n\n")
        else:
            print("\n\nThank You")
        break
    if(x==1):
        import scratch
        scratch.main()
    if(x==2):
        import batch
        batch.main()
    if(x==3):
        import scratch2
        scratch2.main()
    if(x==4):
        import studentinfo
        studentinfo.main()
