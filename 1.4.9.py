nss={"global":["None"],"None":[]}

for i in(range(int(input()))):
    command,space,var=input().split()
    if command=="create":        
        nss[var].append(space)
        nss[space]=[var]
    elif command=="add":
        nss[space].append(var)
    elif command=="get":
        def get(obj,ns,v):
            if ns not in obj or ns=="None":
                print("None")
            elif v in obj[ns]:
                print(ns)
            else:
                get(obj,obj[ns][0],v)
        get(nss,space,var)
print(nss)

