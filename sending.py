import pywhatkit
import os
data = os.popen("type DB.txt").read()
lines = data.splitlines()
os.popen("type nul > DB.txt")
def fun():
    for i in lines:
        if "Done!" not in i:
            a, message = i.split(",")
            print(f"sending msg to {a}")
            pywhatkit.sendwhatmsg_instantly(f"+91{a}", message)
            
            e = f"{a},{message},Done!"
            os.popen(f"echo {e} >> DB.txt")
            os.popen(f"echo {e} >> data_base.txt")
        else:
            print(f"Already sent: {i}")
fun()