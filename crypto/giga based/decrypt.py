from base64 import b64decode

with open("flag.txt","rb") as f:
    s = f.read()
    for i in range(42):
        s = b64decode(s)
    print(s)

