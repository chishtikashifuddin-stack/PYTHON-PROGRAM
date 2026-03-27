a = ""
d = "" 
def fun():
    global a 
    global d 
    a = input()
    cal()
def cal():
    global a 
    global d 
    if "" == d:
        if "+" in a:
            b,c=a.split("+")
            a = str(int(b)+int(c))
            d = a 
        
        if "-" in a:
            b,c=a.split("-")
            a = str(int(b)-int(c))
            d = a 
        
        if "*" in a:
            b,c=a.split("*")
            a = str(int(b)*int(c))
            d = a 
        
        if "/" in a:
            b,c=a.split("/")
            a = str(int(b)/int(c))
            d = a 
    else:
        if "+" in a:
            b,c=a.split("+")
            a = str((int(d)+int(c)))
            d = a 
        
        if "-" in a:
            b,c=a.split("-")
            a = str((int(d)-int(c)))
            d = a 
        
        if "*" in a:
            b,c=a.split("*")
            a = str((int(d)*int(c)))
            d = a 
        
        if "/" in a:
            b,c=a.split("/")
            a =(int(d)/int(c))
            d = a 
            
    print("TOTAL:"+str(a))  
    if "cls" == a:
        print("START NEW")
        d = ""
    fun()
        
        
fun()