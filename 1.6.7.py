def fnd(classes, parrent, child):
    if parrent == child:
        return "Yes"
    elif child not in classes:
        return "No"
    elif parrent in classes[child]:
        return "Yes"
    else:
        for p in classes[child]:
            if fnd(classes,parrent,p)=="Yes":
                return "Yes"
    return "No"

cl = {}
for i in range(int(input())):
    s = input().split(" : ", 1)
    if len(s) == 2:
        cl[s[0]] = s[1].split()
    else:
        cl[s[0]] = []
for i in range(int(input())):
    s = input().split()
    print(fnd(cl,s[0],s[1]))
