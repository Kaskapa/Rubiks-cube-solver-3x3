from twophase.cubes import cubiecube, facecube
from twophase.pieces import Color, Facelet, Corner, Edge
import time
import random
from tables import TableLoader

table = TableLoader()

table.heuristicToCSV(table.heurEdgeOLL, "heuristicsJsonEdgeOLL.csv")

# def to_facecube_state_corner(cube):
#     ret = "-------------------------------------------------"
#     for i in range(8):
#         j = cube.cp[i]
#         ori = cube.co[i]
#         for k in range(3):
#             if(facecube.corner_color[j][k] == Color.D):
#                 index = facecube.corner_facelet[i][(k + ori) % 3]
#                 ret= ret[:index] + facecube.corner_color[j][k].name + ret[index + 1:]
#     return ret

# def to_facecube_state_edge(cube):
#     ret = "-------------------------------------------------"
#     print(len(ret))
#     for i in range(12):
#         j = cube.ep[i]
#         ori = cube.eo[i]
#         for k in range(2):
#             if(facecube.edge_color[j][k] == Color.D):
#                 index = facecube.edge_facelet[i][(k + ori) % 2]
#                 ret = ret[:index] + facecube.edge_color[j][k].name + ret[index + 1:]
#     return ret

# cube = cubiecube.CubieCube();
# cube.move(random.randint(0, 17))
# print(to_facecube_state_corner(cube))
# print(to_facecube_state_edge(cube))
