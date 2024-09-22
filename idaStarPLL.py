from twophase.cubes import cubiecube
import time
from tables import TableLoader
from collections import OrderedDict


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

def is_goal_state(crossState, edgeState, cornerState, edgePLLState, cornerPLLState, goal_cross_stete, goal_edge_state, goal_corner_state, goal_edge_pll_state, goal_corner_pll_state):
    return crossState == goal_cross_stete and edgeState == goal_edge_state and cornerState == goal_corner_state and edgePLLState == goal_edge_pll_state and cornerPLLState == goal_corner_pll_state

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

class TranspositionTable:
    def __init__(self, max_size=10**6):
        self.max_size = max_size
        self.table = OrderedDict()

    def get(self, key):
        if key in self.table:
            value = self.table[key]
            self.table.move_to_end(key)
            return value
        return None

    def put(self, key, value):
        if key in self.table:
            self.table.move_to_end(key)
        elif len(self.table) >= self.max_size:
            self.table.popitem(last=False)
        self.table[key] = value

actionsForLoop = [0, 3, 7, 10, 8, 11]

class IDA_star(object):
    def __init__(self, max_depth=100, table_size=10**6):
        self.max_depth = max_depth
        self.moves = []

        cubeCheck = cubiecube.CubieCube(type=3)
        self.goal_cross_stete = tuple(cubeCheck.epc + cubeCheck.eoc)
        self.goal_edge_state = tuple(cubeCheck.epf + cubeCheck.eof)
        self.goal_corner_state = tuple(cubeCheck.cpf + cubeCheck.cof)
        self.goal_edge_pll_state = tuple(cubeCheck.eppll + cubeCheck.eopll)
        self.goal_corner_pll_state = tuple(cubeCheck.cppll + cubeCheck.copll)

        self.cornerHeur = tableLoader.heurUFR_UFL_UBR_ULB
        self.edgeHeur = tableLoader.heurFR_FL_BR_BL
        self.crossHeur = tableLoader.heurCross
        self.edgePLLHeur = tableLoader.heurEdgePLL
        self.cornerPLLHeur = tableLoader.heurCornerPLL
        self.transposition_table = TranspositionTable(max_size=table_size)

    def cube_to_key(self, cube):
        return hash((tuple(cube.cp), tuple(cube.ep), tuple(cube.cppll), tuple(cube.eppll), tuple(cube.copll), tuple(cube.eopll)))

    def run(self, cube):
        threshold = self.heuristic_value(cube)
        while threshold <= self.max_depth:
            print("Threshold:", threshold)
            self.moves = []
            self.transposition_table = TranspositionTable(max_size=10**6)
            distance = self.search(cube, 0, threshold)
            if distance == True:
                print("Solution found")
                return self.moves
            if distance == float('inf'):
                return None
            threshold = distance
        return None

    def search(self, cube, g_score, threshold):
        cube_key = self.cube_to_key(cube)
        tt_entry = self.transposition_table.get(cube_key)

        if tt_entry is not None:
            stored_g_score = tt_entry['g_score']
            stored_f_score = tt_entry['f_score']
            if stored_g_score <= g_score:
                return stored_f_score

        f_score = g_score + self.heuristic_value(cube)
        if f_score > threshold:
            self.transposition_table.put(cube_key, {'g_score': g_score, 'f_score': f_score})
            return f_score

        if is_goal_state(tuple(cube.epc + cube.eoc), tuple(cube.epf + cube.eof), tuple(cube.cpf + cube.cof), tuple(cube.eppll+cube.eopll), tuple(cube.cppll + cube.copll), self.goal_cross_stete, self.goal_edge_state, self.goal_corner_state, self.goal_edge_pll_state, self.goal_corner_pll_state) == True:
            self.transposition_table.put(cube_key, {'g_score': g_score, 'f_score': True})
            return True

        min_cost = float('inf')
        for action in actionsForLoop:
            cube_copy = cube.__deepcopy__()
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

        self.transposition_table.put(cube_key, {'g_score': g_score, 'f_score': min_cost})
        return min_cost

    def heuristic_value(self, cube):
        stateEdge = (*cube.epf, *cube.eof)
        stateCross = (*cube.epc, *cube.eoc)
        stateCorner = (*cube.cpf, *cube.cof)
        statePLLCorner = (*cube.cppll, *cube.copll)
        statePLLEdge = (*cube.eppll, *cube.eopll)

        h_corner = h_cross = h_edge = 5
        h_edge_pll = h_corner_pll = 8

        try:
            h_corner = self.cornerHeur[stateCorner]
        except KeyError:
            pass

        try:
            h_edge = self.edgeHeur[stateEdge]
        except KeyError:
            pass

        try:
            h_cross = self.crossHeur[stateCross] - 1
        except KeyError:
            pass

        try:
            h_edge_pll = self.edgePLLHeur[statePLLEdge]
        except KeyError:
            pass

        try:
            h_corner_pll = self.cornerPLLHeur[statePLLCorner]
        except KeyError:
            pass

        # h_f2l = max(h_corner, h_cross, h_edge)

        h_pll = h_edge_pll + h_corner_pll

        h_value = h_pll
        return h_value

all_sol = []

def main_func():
    cube = cubiecube.CubieCube(type=3)

    # scramble = "L D L' D' L' F L2 D' L' D' L D L' F'"
    # scramble = "L D L' D L' D' L2 D' L' D L' D L L"
    scramble = "L' D' F' L D L' D' L' F L2 D' L' D' L D L' D L"
    cube = do_algorithm(scramble, cube)

    ida_star = IDA_star()
    start = time.time()
    solution = ida_star.run(cube)
    end = time.time()

    all_sol.append(solution)

    print("Time:", end - start)
if __name__ == "__main__":

    main_func()

    for sol in all_sol:
        for move in sol:
            print(ACTIONS[move], end=" ")
        print()