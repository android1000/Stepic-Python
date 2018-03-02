def addsons(ex, obj):
    if ex in obj:
        useders.add(s)
    for e in obj:
        addsons(ex, e)


ers = {}
useders = set()
for i in range(int(input())):
    s = input().split(" : ", 1)
    if len(s) == 2:
        ers[s[0]] = s[1].split()
    else:
        ers[s[0]] = []
print(ers)
for i in range(int(input())):
    s = input()
    if s in useders:
        print(s)
    useders.add(s)
    addsons(s, ers)
    print(useders)
