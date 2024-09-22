from twophase.cubes import cubiecube
from twophase.pieces import Edge, Corner
import time
from tables import TableLoader
from itertools import permutations
from idaStarCross import IDA_star_cross

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

class IDA_star_F2L(object):
    def __init__(self, corners, edges, cornerStr, edgeStr, max_depth=100):
        self.max_depth = max_depth
        self.moves = []
        self.transposition_table = {}
        self.corners = corners
        self.edges = edges
        cubeCheck = cubiecube.CubieCube(corners=self.corners, edges=self.edges)
        self.goal_cross_stete = tuple(cubeCheck.epc + cubeCheck.eoc)
        self.goal_edge_state = tuple(cubeCheck.epf + cubeCheck.eof)
        self.goal_corner_state = tuple(cubeCheck.cpf + cubeCheck.cof)
        self.cornerHeur = tableLoader.all_heur[cornerStr]
        self.edgeHeur = tableLoader.all_heur[edgeStr]
        self.crossHeur = tableLoader.heurCross

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

        if is_goal_state(tuple(cube.epc + cube.eoc), tuple(cube.epf + cube.eof), tuple(cube.cpf + cube.cof), self.goal_cross_stete, self.goal_edge_state, self.goal_corner_state) == True:
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
            *cube.cpf, *cube.cof, *cube.epf, *cube.eof, *cube.epc, *cube.eoc
        )

    def heuristic_value(self, cube):
        stateEdge = (*cube.epf, *cube.eof)
        stateCross = (*cube.epc, *cube.eoc)
        stateCorner = (*cube.cpf, *cube.cof)

        h_corner = h_cross = h_edge = 5

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

        h_value = h_corner + h_cross + h_edge

        return h_value

#Demo
if __name__ == "__main__":
    scramble = input("Enter scramble: ")

    cube = cubiecube.CubieCube()
    cube = do_algorithm(scramble, cube)

    cross_sovler = IDA_star_cross()
    cross_sol = cross_sovler.run(cube)
    cross_sol = " ".join([ACTIONS[move] for move in cross_sol])

    solved_f2l_corners = []
    solved_f2l_edges = []

    f2l_corners = [Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR]
    f2l_edges = [Edge.FR, Edge.FL, Edge.BL, Edge.BR]

    f2l_corners_combinations = list(permutations(f2l_corners, 4))
    f2l_edges_combinations = list(permutations(f2l_edges, 4))

    all_sol = []
    sol_heur = {}

    start_time_main = time.time()
    for j in range(len(f2l_corners_combinations)):
        f2l_sol = []
        f2l_corners = f2l_corners_combinations[j]
        f2l_edges= f2l_edges_combinations[j]
        for i, corner in enumerate(f2l_corners):
            corners = f2l_corners[:i+1]
            edges = f2l_edges[:i+1]

            cube = cubiecube.CubieCube(corners=corners, edges=edges)
            cube = do_algorithm(scramble, cube)
            cube = do_algorithm(cross_sol, cube)

            for alg in f2l_sol:
                for move in alg:
                    cube.move(move)

            cornerStr = [corner.value for corner in corners]
            edgeStr = [edge.value for edge in edges]

            cornerStr.sort()
            edgeStr.sort()

            cornerStr = "".join(str(x) for x in cornerStr)
            edgeStr = "".join(str(x) for x in edgeStr)

            if (cornerStr, edgeStr, str(cube.cof), str(cube.cpf), str(cube.eo), str(cube.ep)) in sol_heur:
                f2l_sol.append(sol_heur[(cornerStr, edgeStr, str(cube.cof), str(cube.cpf), str(cube.eo), str(cube.ep))])
                continue

            solver = IDA_star_F2L(corners, edges, cornerStr, edgeStr)
            start_time = time.time()
            moves = solver.run(cube)

            f2l_sol.append(moves)
            end_time = time.time()

            print("Execution time:", end_time - start_time, "seconds")

            sol_heur[(cornerStr, edgeStr, str(cube.cof), str(cube.cpf), str(cube.eo), str(cube.ep))] = moves
        print("Scramble:", scramble)

        print("Cross solution:" , cross_sol)


        for alg in f2l_sol:
            for move in alg:
                print(ACTIONS[move], end=" ")
            print()
        all_sol.append(f2l_sol)

    end_time_main = time.time()
    print("Execution time:", end_time_main - start_time_main, "seconds")
    print("All solutions:", all_sol)

    min_index = 0
    min_array = all_sol[0]
    min_cost = len(min_array[0]) + len(min_array[1]) + len(min_array[2])

    for i in range(1, len(all_sol)):
        cost = len(all_sol[i][0]) + len(all_sol[i][1]) + len(all_sol[i][2])
        if cost < min_cost:
            min_cost = cost
            min_index = i

    print("Min cost:", min_cost)
    print("Min index:", min_index)
    print("SHorteest solution:")
    for alg in all_sol[min_index]:
        for move in alg:
            print(ACTIONS[move], end=" ")
        print()

    # # with cProfile.Profile() as pr:
    # corners = [Corner.URF, Corner.UFL, Corner.ULB]
    # edges = [Edge.FR, Edge.FL, Edge.BL]

    # cornerStr = [corner.value for corner in corners]
    # edgeStr = [edge.value for edge in edges]

    # cornerStr.sort()
    # edgeStr.sort()

    # cornerStr = "".join(str(x) for x in cornerStr)
    # edgeStr = "".join(str(x) for x in edgeStr)

    # cube = cubiecube.CubieCube(corners=corners, edges=edges)
    # cube = do_algorithm(input("Enter scramble: "), cube)
    # cube = do_algorithm(input("Enter cross solution: "), cube)

    # solver = IDA_star_F2L(corners, edges, cornerStr, edgeStr)
    # start_time = time.time()
    # moves = solver.run(cube)

    # for move in moves:
    #     print(ACTIONS[move], end=" ")
    # print()

    # end_time = time.time()
    # execution_time = end_time - start_time
    # print("Execution time:", execution_time, "seconds")
    # # stats = pstats.Stats(pr)
    # # stats.sort_stats(pstats.SortKey.TIME)
    # # stats.print_stats()

