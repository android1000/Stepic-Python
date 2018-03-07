path1="1.txt"
path2="2.txt"
with open(path1,"r") as f1:
    with open(path2,"w") as f2:
        res=f1.read().splitlines()
        res.reverse()
        f2.write("\n".join(res))
