from twophase.cubes import coordcube, cubiecube
from twophase.pieces import Edge, Corner, Color
import copy
from tables import TableLoader
# solution = solve("BUBDUFDDFDRLBRBBLFBRLRFULBUUDRUDURDDDLLLLBUFFURRLBFRFF")

# #  U1-U9, R1-R9, F1-F9, D1-D9, L1-L9, B1-B9.

# print(solution)


cubeOne = cubiecube.CubieCube(corners=[Corner.UBR], edges=[Edge.UR])

cubeOne.move(0)
