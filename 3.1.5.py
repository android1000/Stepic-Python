s = input().lower()
a = input().lower()
b = input().lower()
res = 0
if a not in s:
    res = 0
elif a in b:
    res="Impossible"
else:
    while a in s:
       s=s.replace(a,b)
       res+=1
print(res)
