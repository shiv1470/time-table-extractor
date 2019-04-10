mod=1000000007
def match(text,pattern):
    global mod
    l2=len(pattern)
    A=65
    hashval=0
    for i in pattern:
        hashval=(hashval*26+(ord(i)-A+1))%mod
    currhash=0
    l1=len(text)
    for i in range(l1):
        currhash=(currhash*26 + (ord(text[i])-A+1))%mod
        if(i>=l2):
            currhash=(currhash-(ord(text[i-l2])-A+1)*pow(26,l2))%mod
        if(currhash==hashval):
            return True
    return False
