# import os
# import pywhatkit
# d = []
# a = input("ENTRE NUMBER:-")
# lines = a.split(",")
# for lines in d:
    # if lines in a:
        # b = os.popen(f"echo {a}>data.txt").read()   
        # for a in b:
            # if b in a:
                # pywhatkit.sendwhatmsg_instantly(b,"hii")


                
# import pywhatkit
# import os
# a = input("numbers : ")
# b = os.popen(f"echo {a}>>data.txt").read()
# a = a.split(",")
# c = []
# for numbers in a:
    # for line in numbers:
        # num = line.split("/n")
        # if num:
            # c.append(a)        
# for number in numbers:
    # if len(number) == 12 and number.isdigit():
            # print(f"Sending to {c}")   
            # pywhatkit.sendwhatmsg_instantly(f"+{b}","hii")          
    # else:
        # print(f"Invalid number: {b}")
        
        
        
# import pywhatkit
# import os
# a = input("Enter numbers : ")
# message = "hii"

# numbers = a.split(",")

# for number in numbers:
    # number = number.split()

    # if len(number) == 13:
        # print(f"Sending to {number}")
        # pywhatkit.sendwhatmsg_instantly(f"{number}", message)
    # else:
        # print(f"Invalid number: {number}")
             
       
       
# import pywhatkit
# import os

# a = input("Enter numbers: ")
# message = input("Enter Message: ")
# a = a.replace(" ", "")
# c = a.split(",")
# b = os.popen("type data.txt").read()
# d = []
# for number in c:
    # os.popen(f"echo {number} >> data.txt")   
    # d.append(number)    
    
    # if len(number) == 10 and number.isdigit():
        # if number in b:
            # print(f"Already sent {number}")
           
        # else:
            # print(f"Sending msg to {number}")
            # pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)
            
     
    # else:
        # print(f"Invalid number: {number}")
        
        
        


import pywhatkit
import os

a = input("Enter numbers: ")
message = input("Enter Message: ")
a = a.replace(" ", "")
c = a.split(",")
b = os.popen("type data.txt").read()

for number in c:

    if len(number) == 10 and number.isdigit():
        x =(f"{number},{message}")
        if x in b:
            print(f"Already sent same message to {number}")

        else:
            print(f"Sending msg to {number}")
            pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)

            os.popen(f"echo {x} >> data.txt")

    else:
        print(f"Invalid number: {number}")  