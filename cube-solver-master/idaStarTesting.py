from twophase.cubes import cubiecube
from twophase.pieces import Edge, Corner
from random import choice
import time
from tables import TableLoader
# import cProfile
# import pstats

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

REDUNDANT_ACTIONS = {
    0: [0, 6, 12],
    1: [1, 7, 13],
    2: [2, 8, 14],
    3: [3, 9, 15],
    4: [4, 10, 16],
    5: [5, 11, 17],
    6: [0, 6, 12],
    7: [1, 7, 13],
    8: [2, 8, 14],
    9: [3, 9, 15],
    10: [4, 10, 16],
    11: [5, 11, 17],
    12: [0, 6, 12],
    13: [1, 7, 13],
    14: [2, 8, 14],
    15: [3, 9, 15],
    16: [4, 10, 16],
    17: [5, 11, 17]
}

REDUNDANT_ACTIONS_2 = {
    0: [3, 9, 15],
    1: [4, 10, 16],
    2: [5, 11, 17],
    3: [0, 6, 12],
    4: [1, 7, 13],
    5: [2, 8, 14],
    6: [3, 9, 15],
    7: [4, 10, 16],
    8: [5, 11, 17],
    9: [0, 6, 12],
    10: [1, 7, 13],
    11: [2, 8, 14],
    12: [3, 9, 15],
    13: [4, 10, 16],
    14: [5, 11, 17],
    15: [0, 6, 12],
    16: [1, 7, 13],
    17: [2, 8, 14]
}

def is_goal_state(crossState, edgeState, cornerState, goal_cross_stete, goal_edge_state, goal_corner_state):
    return crossState == goal_cross_stete and edgeState == goal_edge_state and cornerState == goal_corner_state

def get_edge_state(cube, edges):
    edgeArray = [-1]*12
    edgeOrientaion = [-1]*12

    for i in range(12):
        if cube.ep[i] in edges:
            edgeArray[i] = cube.ep[i]
            edgeOrientaion[i] = cube.eo[i]

    return tuple(edgeArray + edgeOrientaion)

def get_cross_state(cube):
    # edgeArray = [i if i in [Edge.UB, Edge.UR, Edge.UF, Edge.UL] else -1 for i in cube.ep]
    # edgeOrientaion = [cube.eo[i] if cube.ep[i] in [Edge.UB, Edge.UR, Edge.UF, Edge.UL] else -1 for i in range(len(cube.eo))]

    edgeArray = [-1]*12
    edgeOrientaion = [-1]*12

    edges = [Edge.UB , Edge.UR, Edge.UF, Edge.UL]

    for i in range(12):
        if cube.ep[i] in edges:
            edgeArray[i] = cube.ep[i]
            edgeOrientaion[i] = cube.eo[i]

    return tuple(edgeArray + edgeOrientaion)

def get_corner_state(cube, corners):
    cornerArray = [-1]*8
    cornerOrientation = [-1]*8

    for i in range(8):
        if cube.cp[i] in corners:
            cornerArray[i] = cube.cp[i]
            cornerOrientation[i] = cube.co[i]

    return tuple(cornerArray + cornerOrientation)

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
        cube.move(12)
    elif(action == "R'"):
        cube.move(13)
    elif(action == "F'"):
        cube.move(14)
    elif(action == "D'"):
        cube.move(15)
    elif(action == "L'"):
        cube.move(16)
    elif(action == "B'"):
        cube.move(17)
    elif(action == "U2"):
        cube.move(6)
    elif(action == "R2"):
        cube.move(7)
    elif(action == "F2"):
        cube.move(8)
    elif(action == "D2"):
        cube.move(9)
    elif(action == "L2"):
        cube.move(10)
    elif(action == "B2"):
        cube.move(11)
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
        cubeCheck = cubiecube.CubieCube(corners=corners, edges=edges)
        self.goal_cross_stete = tuple(cubeCheck.epc + cubeCheck.eoc)
        self.goal_edge_state = tuple(cubeCheck.epf + cubeCheck.eof)
        self.goal_corner_state = tuple(cubeCheck.cp + cubeCheck.co)

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

        if is_goal_state(tuple(cube.epc + cube.eoc), tuple(cube.epf + cube.eof), tuple(cube.cp + cube.co), self.goal_cross_stete, self.goal_edge_state, self.goal_corner_state):
            self.transposition_table[cube_state] = (g_score, True)
            return True

        min_cost = float('inf')
        for action in range(18):
            cube_copy = cube.__deepcopy__()
            # cube_copy = copy.copy(cube)
            cube_copy.move(action)

            if len(self.moves) > 0 and action in REDUNDANT_ACTIONS[self.moves[-1]]:
                continue

            if len(self.moves) > 1 and action in REDUNDANT_ACTIONS_2[self.moves[-1]] and action in REDUNDANT_ACTIONS[self.moves[-2]]:
                continue

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
        # Use tuple concatenation instead of creating separate tuples
        return (
            *cube.cp, *cube.co, *cube.ep, *cube.eo
        )


def heuristic_value(cube, corners, edges):
    # stateEdge = get_edge_state(cube, edges)
    # stateCross = get_cross_state(cube)
    # stateCorner = get_corner_state(cube, corners)

    stateEdge = (*cube.epf, *cube.eof)
    stateCross = (*cube.epc, *cube.eoc)
    stateCorner = (*cube.cp, *cube.co)

    h_corner = tableLoader.heurURF_UFL_ULB[stateCorner]
    h_edge = tableLoader.heurFR_FL_BL[stateEdge]

    if stateCross in tableLoader.heurCross:
        h_cross = tableLoader.heurCross[stateCross] - 1
    else:
        h_cross = 6

    h_value = h_corner + h_cross + h_edge

    return h_value

if __name__ == "__main__":
    # with cProfile.Profile() as pr:
    corners = [Corner.ULB, Corner.URF, Corner.UFL]
    edges = [Edge.BL, Edge.FR, Edge.FL]
    cube = cubiecube.CubieCube(corners=corners, edges=edges)
    cube = do_algorithm("F' L' U' B D L U2 D B L2 D2 B' R2 U' B2 R' F2 D' R B2 U", cube)


    solver = IDA_star(corners, edges)
    start_time = time.time()
    moves = solver.run(cube)

    for move in moves:
        print(ACTIONS[move], end=" ")
    print()

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    # stats = pstats.Stats(pr)
    # stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()

