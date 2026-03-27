a =int(input())
c = 1,2,3,4,5,6,7,8,9,10,11,12
def fun():
    for a in c:
        for b in c:
            print (str(a)+"*" + str(b) +"="  +str(a*b))
fun()