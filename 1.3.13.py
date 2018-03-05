def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res


print(s(11, b=20)+100)
print(s(0, 0, 31)+200)
print(s(5, 5, 5, 5, 1)+300)
#print(s(b=31, 0)+400)
print(s(11, 10, 10)+500)
print(s(21)+600)
print(s(11, 10)+700)
#print(s(b=31)+800)
print(s(11, 10, b=10)+900)

