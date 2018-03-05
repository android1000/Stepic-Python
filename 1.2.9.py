ans = set()
objec = [1, 2, 1, 2, 3]
for obj in objec: # доступная переменная objects
        ans.add(id(obj))
print(ans)
print(len(ans))
