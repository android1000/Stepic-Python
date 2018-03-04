import simplecrypt

with open("D:\Downloads\encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    with open("D:\Downloads\passwords.txt","r") as k:
        for line in k:
            line=line.strip('\n')
            try:
                print(simplecrypt.decrypt(line,encrypted).decode('utf8'))
            except simplecrypt.DecryptionException:
                print(line, 'is wrong')
            else:
                print(line, 'is correct')
