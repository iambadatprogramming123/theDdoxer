#code written by Toto The Cat

import time
from pyfiglet import figlet_format as f
import webbrowser as wb
from googlesearch import search

print(f("theDoxxer"))
print("=============================================")
print("type --usage for help. ")
print("\n"*2)

cmd=input()

if (cmd=="--atk"):
    target=input() 
    for i in search(target, tld="com", num=20, stop=None):
        print(i),

elif (cmd=="--atkpn"):
    phone=input()
    print("Note: the first link accepts only US-based phone numbers. ")
    print("Note2: the second link is a tool named Phoneinfoga, specialised in phone number lookup. You need to select your country code and type in the phone number as shown in the example from the website. \n \n")
    time.sleep(1)
    print("https://whocallsme.com/Phone-Number.aspx/"+phone)
    time.sleep(1)
    print("\n \nhttps://demo.phoneinfoga.crvx.fr/#/")
    
    
elif (cmd=="--usage"):
    print(2*"\n")
    print("Usage (for names): --atk [target]")
    print("Example: --atk John Smith \n \n")
    print("Usage (for phone numbers): --atkpn [phone number]")
    print("Example: --atkpn (201) 555-0123")
    print("\n"*2)

else:
    print("This command is unavailable. ")
