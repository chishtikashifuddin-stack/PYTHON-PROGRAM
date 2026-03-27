a = str(0)
b = 2
for c in a*99 :
    a = int(a)
    if a<=99:
        a+=1
        c = a//b
        if c%2!=0:
            d=1
            print(c)
            for a1 in str(d)*10:
                if d<=9:
                    d+=1
                    print(str(c)+"*"+str(d)+"="+str(d*c)

a = 0
for a in range(0,100):
    if a ==20:
       continue
    else :
        print(a)