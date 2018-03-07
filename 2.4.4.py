path1="1.txt"
path2="2.txt"
with open(path1,"r") as f1:
    with open(path2,"w") as f2:
        res=[]
        for line in f1:
            res+=[line.strip("\n")+"\n"]
        i=len(res)
        while i>0:
            f2.write(res[i-1])
            i-=1
