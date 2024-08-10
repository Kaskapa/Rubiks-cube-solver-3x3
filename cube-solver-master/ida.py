import json
import pickle
from twophase.cubes import cubiecube
from twophase.pieces import Edge, Corner
import copy
from random import choice
import time

with open("heuristicsEdgeCross.pickle", 'rb') as file:
    heuristicEdgeCross = pickle.load(file)

with open("heuristicsCornerUFL_UBR.pickle", 'rb') as file:
    heuristicCorner= pickle.load(file)

with open("heuristicsEdgeFL_BR.pickle", 'rb') as file:
    heuristicEdge = pickle.load(file)

ACTIONS = {
    0: "U",
    1: "R",
    2: "F",
    3: "D",
    4: "L",
    5: "B",
    6: "U'",
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
    def __init__(self, max_depth=20):
        self.max_depth = max_depth
        self.moves = []
        self.transposition_table = {}

    def run(self, cube):
        threshold = heuristic_value(cube)
        while threshold <= self.max_depth:
            self.moves = []
            self.transposition_table = {}  # Clear the table for each iteration
            distance = self.search(cube, 0, threshold)
            if distance == True:
                return self.moves
            if distance == float('inf'):
                return None  # No solution found within max_depth
            threshold = distance
        return None  # No solution found within max_depth

    def search(self, cube, g_score, threshold):
        cube_state = self.get_cube_state(cube)

        # Check if this state has been explored before
        if cube_state in self.transposition_table:
            stored_g_score, stored_result = self.transposition_table[cube_state]
            if stored_g_score <= g_score:
                return stored_result

        f_score = g_score + heuristic_value(cube)
        if f_score > threshold:
            self.transposition_table[cube_state] = (g_score, f_score)
            return f_score

        if is_goal_state(get_cross_state(cube), get_edge_state(cube), get_corner_state(cube)):
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
        # Return a hashable representation of the cube state
        return (tuple(cube.cp), tuple(cube.co), tuple(cube.ep), tuple(cube.eo))

def heuristic_value(cube):
    stateEdge = get_edge_state(cube)
    stateCross = get_cross_state(cube)
    stateCorner = get_corner_state(cube)

    h_corner = heuristicCorner.get(stateCorner, 6)
    h_cross = heuristicEdgeCross.get(stateCross, 7) - 1  # Subtracting 1 here instead of in the if statement
    h_edge = heuristicEdge.get(stateEdge, 6)

    # Weighted sum
    weighted_sum = (3 * h_corner + 2 * h_cross + h_edge) / 6

    h_value = max(h_corner, h_cross, h_edge, weighted_sum)

    return h_value

goal_cross_stete = (Edge.UR, Edge.UF, Edge.UL, Edge.UB, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1)
goal_edge_state = (-1, -1, -1, -1, -1, -1, -1, -1, Edge.FR, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1)
goal_corner_state = (Corner.URF, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1)

heuristicCorner[goal_corner_state] = 0
heuristicEdgeCross[goal_cross_stete] = 0
heuristicEdge[goal_edge_state] = 0

def is_goal_state(crossState, edgeState, cornerState):
    return crossState == goal_cross_stete and edgeState == goal_edge_state and cornerState == goal_corner_state

def get_edge_state(cube):
    edgeArray = []
    edgeOrientaion = []

    for i in range(12):
        if cube.ep[i] == Edge.FR:
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

def get_corner_state(cube):
    cornerArray = []
    cornerOrientation = []

    for i in range(8):
        if cube.cp[i] == Corner.URF:
            cornerArray.append(cube.cp[i])
            cornerOrientation.append(cube.co[i])
        else:
            cornerArray.append(-1)
            cornerOrientation.append(-1)

    return tuple(cornerArray + cornerOrientation)

cube = cubiecube.CubieCube()

# U move
# cube.move(0)

# R move
# cube.move(1)

# F move
# cube.move(2)

# D move
# cube.move(3)

# L move
# cube.move(4)

# B move
# cube.move(5)

# cube = do_algorithm("B D' R2 B' U2 L F' R B' D R2 F2 L2 U' F' L2 B U2 L F R", cube)
cube = do_algorithm("F' L' U' B D L U2 D B L2 D2 B' R2 U' B2 R' F2 D' R B2 U", cube)
cube = do_algorithm("U R F' U' B D", cube)

# cube = do_algorithm("L' D2 F L' D", cube)
# cube = do_algorithm("F' D2 R F D", cube)
solver = IDA_star()
start_time = time.time()
moves = solver.run(cube)

for move in moves:
    print(ACTIONS[move], end=" ")
print()

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")