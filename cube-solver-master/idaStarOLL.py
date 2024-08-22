from twophase.cubes import cubiecube, facecube
from twophase.pieces import Edge, Corner, Color
import time
from tables import TableLoader
from itertools import permutations
from idaStarCross import IDA_star_cross
from idaStarF2L import IDA_star_F2L

tableLoader = TableLoader()

GOALOLLEDGE = "----------------------------D-D-D-D-------------------"
GOALOLLCORNER = "---------------------------D-D---D-D------------------"

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

def is_goal_state(crossState, edgeState, cornerState, edgeOllState, cornerOllState, goal_cross_stete, goal_edge_state, goal_corner_state):
    return crossState == goal_cross_stete and edgeState == goal_edge_state and cornerState == goal_corner_state and edgeOllState == GOALOLLEDGE and cornerOllState == GOALOLLCORNER

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

def to_facecube_state_corner(cube):
    ret = "------------------------------------------------------"
    for i in range(8):
        j = cube.cp[i]
        ori = cube.co[i]
        for k in range(3):
            if(facecube.corner_color[j][k] == Color.D):
                index = facecube.corner_facelet[i][(k + ori) % 3]
                ret= ret[:index] + facecube.corner_color[j][k].name + ret[index + 1:]
    return ret

def to_facecube_state_edge(cube):
    ret = "------------------------------------------------------"
    for i in range(12):
        j = cube.ep[i]
        ori = cube.eo[i]
        for k in range(2):
            if(facecube.edge_color[j][k] == Color.D):
                index = facecube.edge_facelet[i][(k + ori) % 2]
                ret = ret[:index] + facecube.edge_color[j][k].name + ret[index + 1:]
    return ret

class IDA_star(object):
    def __init__(self, max_depth=100):
        self.max_depth = max_depth
        self.moves = []
        self.transposition_table = {}
        cubeCheck = cubiecube.CubieCube()
        self.goal_cross_stete = tuple(cubeCheck.epc + cubeCheck.eoc)
        self.goal_edge_state = tuple(cubeCheck.epf + cubeCheck.eof)
        self.goal_corner_state = tuple(cubeCheck.cpf + cubeCheck.cof)
        self.cornerHeur = tableLoader.heurUFR_UFL_UBR_ULB
        self.edgeHeur = tableLoader.heurFR_FL_BR_BL
        self.crossHeur = tableLoader.heurCross
        self.edgeOLLHeur = tableLoader.heurEdgeOLL
        self.cornerOLLHeur = tableLoader.heurCornerOLL

    def run(self, cube):
        threshold = self.heuristic_value(cube)
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

        f_score = g_score + self.heuristic_value(cube)
        if f_score > threshold:
            self.transposition_table[cube_state] = (g_score, f_score)
            return f_score

        if is_goal_state(tuple(cube.epc + cube.eoc), tuple(cube.epf + cube.eof), tuple(cube.cpf + cube.cof), to_facecube_state_edge(cube), to_facecube_state_corner(cube), self.goal_cross_stete, self.goal_edge_state, self.goal_corner_state) == True:
            self.transposition_table[cube_state] = (g_score, True)
            return True

        min_cost = float('inf')
        for action in range(18):
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

        self.transposition_table[cube_state] = (g_score, min_cost)
        return min_cost

    def get_cube_state(self, cube):
        return (
            *cube.cpf, *cube.epf, *cube.to_facecube()
        )

    def heuristic_value(self, cube):
        stateEdge = (*cube.epf, *cube.eof)
        stateCross = (*cube.epc, *cube.eoc)
        stateCorner = (*cube.cpf, *cube.cof)
        stateOLLCorner = to_facecube_state_corner(cube)
        stateOLLEdge = to_facecube_state_edge(cube)

        h_corner = h_cross = h_edge = h_edge_oll = h_corner_oll = 8

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
            h_edge_oll = self.edgeOLLHeur[stateOLLEdge]
        except KeyError:
            pass

        try:
            h_corner_oll = self.cornerOLLHeur[stateOLLCorner]
        except KeyError:
            pass

        h_f2l = max(h_corner, h_cross, h_edge)

        # The heuristic for the OLL part is the sum of edge and corner OLL heuristics
        h_oll = h_edge_oll + h_corner_oll

        # The overall heuristic is the sum of the F2L heuristic and the OLL heuristic
        h_value = h_f2l + h_oll
        return h_value-5


import cProfile
import pstats

if __name__ == "__main__":
    with cProfile.Profile() as pr:
        # cube = cubiecube.CubieCube()
        # scramble = "F R2 U L' D B' D2 R' U' L' B2 U2 L2 F' D2 R F' U R2 B2 L"
        # cube = do_algorithm(scramble, cube)

        # crossSolver = IDA_star_cross()
        # crossSolution = crossSolver.run(cube)

        # crossSolutionString = ""
        # for move in crossSolution:
        #     crossSolutionString += ACTIONS[move] + " "

        # print("Cross solution:", crossSolutionString)
        # f2lSolutionString = "U2 L' D F2 L' F2 L2 U2 U B D2 B' D U' D B' D2 B2 D B' D B' D2 B D' B' D' B"

        # print("F2L solution:", f2lSolutionString)

        # cube = cubiecube.CubieCube()
        # cube = do_algorithm(scramble, cube)
        # cube = do_algorithm(crossSolutionString, cube)
        # cube = do_algorithm(f2lSolutionString, cube)

        # solver = IDA_star();
        # start_time = time.time()
        # moves = solver.run(cube)

        # for move in moves:
        #     print(ACTIONS[move], end=" ")
        # print()

        # end_time = time.time()
        # execution_time = end_time - start_time
        # print("Execution time:", execution_time, "seconds")


        cube = cubiecube.CubieCube()
        # F (R U R' U') (R U R' U') F'
        # scramble = "F L D L' D' L D L' D' F'"
        # scramble = "L D L' D L D' L' D L D2 L'"
        # scramble = "F D2 F L' F' L D L D L' D F'"
        scramble = "F L' F' L D2 F L' F' L2 D2 L'"
        # scramble = "F D L D' L' F'"
        cube = do_algorithm(scramble, cube)

        solver = IDA_star();
        start_time = time.time()
        moves = solver.run(cube)

        for move in moves:
            print(ACTIONS[move], end=" ")
        print()
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")


    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

