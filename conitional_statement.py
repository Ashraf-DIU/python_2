age = int(input())

if(age >= 18):
    print("Can Vote")
    print("Can Drive")
elif(age >= 15):
    print("can marriage")
else:
    print("Go for Sleep")


# nesting
if(age >= 18):
    print("Can Vote")
    if(age >= 80):
        print("Can't Drive")
    else:
        print("Can Drive")
elif(age >= 15):
    print("can marriage")
else:
    print("Go for Sleep")
