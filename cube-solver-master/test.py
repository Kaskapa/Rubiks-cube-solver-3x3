from twophase.cubes import coordcube, cubiecube
from twophase.pieces import Edge, Corner, Color

# solution = solve("BUBDUFDDFDRLBRBBLFBRLRFULBUUDRUDURDDDLLLLBUFFURRLBFRFF")

# #  U1-U9, R1-R9, F1-F9, D1-D9, L1-L9, B1-B9.

# print(solution)

cubiecube = cubiecube.CubieCube()
cubiecube.move(5)

cornerArray = []
cornerOrientation = []

for i in range(8):
    if(cubiecube.cp[i] == Corner.DBL):
        cornerArray.append(Corner.DBL)
        cornerOrientation.append(cubiecube.co[i])
    else:
        cornerArray.append(-1)
        cornerOrientation.append(-1)

print(cornerArray)
print(cornerOrientation)
