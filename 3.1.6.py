s = input().lower()
t = input().lower()
res = 0
index = 0
while s.find(t, index) >= 0:
    res += 1
    index = s.find(t, index) + 1
print(res)
