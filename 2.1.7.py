def fnd(classes, parrent, child):
    if parrent == child:
        return True
    elif child not in classes:
        return False
    elif parrent in classes[child]:
        return True
    else:
        for p in classes[child]:
            if fnd(classes, parrent, p):
                return True
    return False


ers = {}
useders = []
for i in range(int(input())):
    s = input().split(" : ", 1)
    if len(s) == 2:
        ers[s[0]] = s[1].split()
    else:
        ers[s[0]] = []

for i in range(int(input())):
    s = input()
    if s in useders:
        print(s)
    else:
        useders.append(s)
        for ex in ers:
            if fnd(ers, s, ex):
                useders.append(ex)
