import os.path

for cur_dir, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            print(cur_dir)
            break
