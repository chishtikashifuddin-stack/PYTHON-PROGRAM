'''
a = 1
def fun():
    global a
    a = "kashif"
    print(a)
fun()    
print(a)    
print(a)
'''
a = 2
c = 1,2,3,4,5,6,7,8,9,10
def fun():
    global c 
    for c in c:
            print (str(a)+"*" + str(c) +"="  +str (a*c))
fun()