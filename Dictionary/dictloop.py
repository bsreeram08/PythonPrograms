import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def isthere(key):
    key=key.lower()
    check=get_close_matches(key,data.keys(),cutoff=0.8)
    if(key in data):
        output=data[key]
        for item in output:
            print(item)
    elif(key.title() in data):
        output=data[key.title()]
        for item in output:
            print(item)
    elif(key.upper() in data):
        output=data[key.upper()]
        for item in output:
            print(item)
    elif(len(check)>0):
        choice=input ("Did You Mean %s instead? (press [y:yes,n:no]):" % check[0])
        if choice=="y" or choice=="Y":
            isthere(check[0])
        elif choice=="n" or choice=="N":
            print ("The Word Does not Exist, Please Double Check it!")
        else:
            print("Wrong Choice!")
    else:
        print("Data is not Present. Please Double Check it!")
while True:
    key=input("Enter a Word to Find its Meaning:")
    isthere(key)
