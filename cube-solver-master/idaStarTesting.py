import json
import pickle
from twophase.cubes import cubiecube
from twophase.pieces import Edge, Corner
import copy
from random import choice
import time
from tables import TableLoader

tableLoader = TableLoader()

ACTIONS = {
    0: "U",
    1: "R",
    2: "F",
    3: "D",
    4: "L",
    5: "B",
    6: "U2",
    7: "R2",
    8: "F2",
    9: "D2",
    10: "L2",
    11: "B2",
    12: "U'",
    13: "R'",
    14: "F'",
    15: "D'",
    16: "L'",
    17: "B'"
}
def is_goal_state(crossState, edgeState, cornerState, corners, edges):
    cubeCheck = cubiecube.CubieCube()
    goal_cross_stete = get_cross_state(cubeCheck)
    goal_edge_state = get_edge_state(cubeCheck, edges)
    goal_corner_state = get_corner_state(cubeCheck, corners)

    return crossState == goal_cross_stete and edgeState == goal_edge_state and cornerState == goal_corner_state

def get_edge_state(cube, edges):
    edgeArray = []
    edgeOrientaion = []

    for i in range(12):
        if cube.ep[i] in edges:
            edgeArray.append(cube.ep[i])
            edgeOrientaion.append(cube.eo[i])
        else:
            edgeArray.append(-1)
            edgeOrientaion.append(-1)

    return tuple(edgeArray + edgeOrientaion)

def get_cross_state(cube):
    edgeArray = []
    edgeOrientaion = []

    for i in range(12):
        if cube.ep[i] == Edge.UB or cube.ep[i] == Edge.UR or cube.ep[i] == Edge.UF or cube.ep[i] == Edge.UL:
            edgeArray.append(cube.ep[i])
            edgeOrientaion.append(cube.eo[i])
        else:
            edgeArray.append(-1)
            edgeOrientaion.append(-1)

    return tuple(edgeArray + edgeOrientaion)

def get_corner_state(cube, corners):
    cornerArray = []
    cornerOrientation = []

    for i in range(8):
        if cube.cp[i] in corners:
            cornerArray.append(cube.cp[i])
            cornerOrientation.append(cube.co[i])
        else:
            cornerArray.append(-1)
            cornerOrientation.append(-1)

    return tuple(cornerArray + cornerOrientation)

def actions(action, cube):
    if(action == 0):
        cube.move(0)
    elif(action == 1):
        cube.move(1)
    elif(action == 2):
        cube.move(2)
    elif(action == 3):
        cube.move(3)
    elif(action == 4):
        cube.move(4)
    elif(action == 5):
        cube.move(5)
    elif(action == 6):
        cube.move(0)
        cube.move(0)
    elif(action == 7):
        cube.move(1)
        cube.move(1)
    elif(action == 8):
        cube.move(2)
        cube.move(2)
    elif(action == 9):
        cube.move(3)
        cube.move(3)
    elif(action == 10):
        cube.move(4)
        cube.move(4)
    elif(action == 11):
        cube.move(5)
        cube.move(5)
    elif(action == 12):
        cube.move(0)
        cube.move(0)
        cube.move(0)
    elif(action == 13):
        cube.move(1)
        cube.move(1)
        cube.move(1)
    elif(action == 14):
        cube.move(2)
        cube.move(2)
        cube.move(2)
    elif(action == 15):
        cube.move(3)
        cube.move(3)
        cube.move(3)
    elif(action == 16):
        cube.move(4)
        cube.move(4)
        cube.move(4)
    elif(action == 17):
        cube.move(5)
        cube.move(5)
        cube.move(5)

    return cube

def actionsWithNotations(action, cube):
    if(action == "U"):
        cube.move(0)
    elif(action == "R"):
        cube.move(1)
    elif(action == "F"):
        cube.move(2)
    elif(action == "D"):
        cube.move(3)
    elif(action == "L"):
        cube.move(4)
    elif(action == "B"):
        cube.move(5)
    elif(action == "U'"):
        cube.move(0)
        cube.move(0)
        cube.move(0)
    elif(action == "R'"):
        cube.move(1)
        cube.move(1)
        cube.move(1)
    elif(action == "F'"):
        cube.move(2)
        cube.move(2)
        cube.move(2)
    elif(action == "D'"):
        cube.move(3)
        cube.move(3)
        cube.move(3)
    elif(action == "L'"):
        cube.move(4)
        cube.move(4)
        cube.move(4)
    elif(action == "B'"):
        cube.move(5)
        cube.move(5)
        cube.move(5)
    elif(action == "U2"):
        cube.move(0)
        cube.move(0)
    elif(action == "R2"):
        cube.move(1)
        cube.move(1)
    elif(action == "F2"):
        cube.move(2)
        cube.move(2)
    elif(action == "D2"):
        cube.move(3)
        cube.move(3)
    elif(action == "L2"):
        cube.move(4)
        cube.move(4)
    elif(action == "B2"):
        cube.move(5)
        cube.move(5)

    return cube

def do_algorithm(algorithm, cube):
    algorithmArray = algorithm.split(" ")
    for move in algorithmArray:
        cube = actionsWithNotations(move, cube)
    return cube

class IDA_star(object):
    def __init__(self, corners, edges, max_depth=100):
        self.max_depth = max_depth
        self.moves = []
        self.transposition_table = {}
        self.corners = corners
        self.edges = edges

    def run(self, cube):
        threshold = heuristic_value(cube, self.corners, self.edges)
        while threshold <= self.max_depth:
            print("Threshold:", threshold)
            self.moves = []
            self.transposition_table = {}
            distance = self.search(cube, 0, threshold)
            if distance == True:
                print("Solution found")
                return self.moves
            if distance == float('inf'):
                return None
            threshold = distance
        return None

    def search(self, cube, g_score, threshold):
        cube_state = self.get_cube_state(cube)

        if cube_state in self.transposition_table:
            stored_g_score, stored_result = self.transposition_table[cube_state]
            if stored_g_score <= g_score:
                return stored_result

        f_score = g_score + heuristic_value(cube, self.corners, self.edges)
        if f_score > threshold:
            self.transposition_table[cube_state] = (g_score, f_score)
            return f_score

        if is_goal_state(get_cross_state(cube), get_edge_state(cube, self.edges), get_corner_state(cube, self.corners), self.corners, self.edges):
            self.transposition_table[cube_state] = (g_score, True)
            return True

        min_cost = float('inf')
        for action in range(18):
            cube_copy = copy.deepcopy(cube)
            cube_copy = actions(action, cube_copy)

            self.moves.append(action)
            distance = self.search(cube_copy, g_score + 1, threshold)
            if distance == True:
                return True
            if distance < min_cost:
                min_cost = distance
            self.moves.pop()

        self.transposition_table[cube_state] = (g_score, min_cost)
        return min_cost

    def get_cube_state(self, cube):
        return (tuple(cube.cp), tuple(cube.co), tuple(cube.ep), tuple(cube.eo))

def heuristic_value(cube, corners, edges):
    startingCube = cubiecube.CubieCube()

    startingStateCross = get_cross_state(startingCube)
    startingStateEdge = get_edge_state(startingCube, edges)
    startingStateCorner = get_corner_state(startingCube, corners)

    tableLoader.heurCross[startingStateCross] = 1
    tableLoader.heurFL_BR[startingStateEdge] = 0
    tableLoader.heurUFL_UBR[startingStateCorner] = 0

    stateEdge = get_edge_state(cube, edges)
    stateCross = get_cross_state(cube)
    stateCorner = get_corner_state(cube, corners)

    h_corner = tableLoader.heurUFL_UBR.get(stateCorner, 6)
    h_edge = tableLoader.heurFL_BR.get(stateEdge, 6)
    h_cross = tableLoader.heurCross.get(stateCross, 7) - 1

    # Weighted sum
    weighted_sum = (3 * h_corner + 2 * h_cross + h_edge) / 6

    # h_value = max(h_corner, h_cross, h_edge, weighted_sum)

    h_value = h_corner + h_cross + h_edge

    return h_value

cube = cubiecube.CubieCube()

# cube = do_algorithm("B D' R2 B' U2 L F' R B' D R2 F2 L2 U' F' L2 B U2 L F R", cube)
# cube = do_algorithm("L' D2 F L' D", cube)
# cube = do_algorithm("R2 B2 R2 B2", cube)
# cube = do_algorithm("B D L2 B L2 B'", cube)
# cube = do_algorithm("L' D L2 B' L' D2 B", cube)
# cube = do_algorithm("B2 D B D' B2", cube)
# cube = do_algorithm("R D' R'", cube)

cube = do_algorithm("F' L' U' B D L U2 D B L2 D2 B' R2 U' B2 R' F2 D' R B2 U", cube)
cube = do_algorithm("U R F' U' B D", cube)
cube = do_algorithm("F2 R2 F2 R2", cube)

# cube = do_algorithm("U L' F R B L D F' R U' L F D L D2 F2 U' R2 D' F2 D' B R' U'", cube)
# cube = do_algorithm("R F L' U' F L' B' D", cube)
# cube = do_algorithm("R' D' R", cube)
# cube = do_algorithm("B D' B B2", cube)

corners = [Corner.UBR, Corner.UFL]
edges = [Edge.BR, Edge.FL]

solver = IDA_star(corners, edges)
start_time = time.time()
moves = solver.run(cube)

for move in moves:
    print(ACTIONS[move], end=" ")
print()

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")


# cube = cubiecube.CubieCube()

# cube = do_algorithm("U L' F R B L D F' R U' L F D L D2 F2 U' R2 D' F2 D' B R' U'", cube)
# cube = do_algorithm("R F L' U' F L' B' D", cube)
# cube = do_algorithm("R' D' R", cube)
# cube = do_algorithm("B D' B B2", cube)

# moves = "U' F' D' F' R2 F2 U' D"

# movesArr = moves.split(" ")

# corners = [Corner.UBR]
# edges = [Edge.BR]

# for move in movesArr:
#     cube = actionsWithNotations(move, cube)

#     h = heuristic_value(cube, [Corner.URF], [Edge.FR])

#     print("Heuristic value:", h)
#     print(is_goal_state(get_cross_state(cube), get_edge_state(cube, edges), get_corner_state(cube, corners), corners, edges))

