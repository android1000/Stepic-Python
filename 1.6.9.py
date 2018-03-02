import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list,Loggable):
    def append(self, p_object):
        list.append(self, p_object)
        #super(LoggableList,self).append(p_object)
        self.log(p_object)

a=[]
a.append(1)
print(a)
a=LoggableList(a)
print(a)
a.append(3)
a.append(input().split())
print(a)

