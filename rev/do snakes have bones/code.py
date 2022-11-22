# alphabets = "0123456789abcdefghijklmnopqrstuvwxyz"

# f = "sn4k3_di5as5embl3d"

# print("\"BITSCTF{\"",end="+")
# for i in f:
#     if i in alphabets:
#         print(f"alphabets[{alphabets.index(i)}]",end="+")
#     else:
#         print(f"\"{i}\"",end="+")
# print("\"}\"")

# flag = "BITSCTF{"+alphabets[28]+alphabets[23]+alphabets[4]+alphabets[20]+alphabets[3]+"_"+alphabets[13]+alphabets[18]+alphabets[5]+alphabets[10]+alphabets[28]+alphabets[5]+alphabets[14]+alphabets[22]+alphabets[11]+alphabets[21]+alphabets[3]+alphabets[13]+"}"
# print(flag)

def flag():
    alphabets = "0123456789abcdefghijklmnopqrstuvwxyz"
    print("BITSCTF{"+alphabets[28]+alphabets[23]+alphabets[4]+alphabets[20]+alphabets[3]+"_"+alphabets[13]+alphabets[18]+alphabets[5]+alphabets[10]+alphabets[28]+alphabets[5]+alphabets[14]+alphabets[22]+alphabets[11]+alphabets[21]+alphabets[3]+alphabets[13]+"}")

import dis
print(dis.dis(flag))