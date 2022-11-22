from base64 import b64encode
  
s = b'BITSCTF{h1gh_l3v31_b4SeD_3NCrYP710N}'

with open("flag.txt","wb") as f:
    for i in range(42):
        s = b64encode(s)
    print(s)
    f.write(s)
