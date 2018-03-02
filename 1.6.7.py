cl = {}

for i in range(int(input())):
    s = input().split(" : ", 1)
    if len(s) == 2:
        cl[s[0]] = set(s[1].split())
    else:
        cl[s[0]] = {}
print(cl)
res=[]
for i in range(int(input())):
    tmp = "No"
    s = input().split()
    if s[0] == s[1]:
        tmp = "Yes"
    elif s[1] not in cl:
        tmp = "No"
    elif s[0] in cl[s[1]]:
        tmp = "Yes"
    else:
        for cls in cl[s[1]]:
            if s[0] in cl[cls]:
                tmp = "Yes"
                break
    print(tmp)
    res.append(tmp)
print(res)
