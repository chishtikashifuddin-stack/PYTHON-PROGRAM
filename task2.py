a = input("EVERYTHING:")
c=""
for b in a:
    if b.lower() in a:
        c=c+b.upper()
    else :
        c=c+b.lower()
print(c)        