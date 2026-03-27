a = "kashif chisti" #global variable
b = 2
def fun():
    global a #it becomes a global variable
    print("my name is "+a)
    
fun()
print(a)
#print(e)
def fun1():
    global a
    
    a = "ansh"
    print("my name is "+a)

fun1()