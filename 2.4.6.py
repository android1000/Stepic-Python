import os.path

print(os.getcwd())
print(os.listdir("main"))

for cur_dir, dirs, files in os.walk("main"):
    for file in files:
        if file[len(file)-3:]==".py":
            print(cur_dir)
            break
