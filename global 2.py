a = (input())
c = 1,2,3,4,5,6,7,8,9,10                                                    
def fun():
    global a 
    global c
    for a in a:
        a = int(a)
        for b in c:
            print (str(a)+"*" + str(b) +"="  +str(a*b))
fun()