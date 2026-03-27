a = 0
b = 2
for c in str(a)*99:
    if a<=99:
        a+=1
        c = a//b
        if c%2!=0:
            d=1
            print(c)
            for a1 in str(d)*10:
                if d<=9:
                    d+=1
                    print(str(c)+"*"+str(d)+"="+str(d*c))