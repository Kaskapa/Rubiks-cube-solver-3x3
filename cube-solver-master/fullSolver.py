from idaStarCross import IDA_star_cross
from idaStarF2L import IDA_star_F2L
from cheapOLLSolver import OLLSolver
from twophase.cubes.cubiecube import CubieCube
from twophase.cubes.rubiks_cube import Cube
from twophase.pieces import Corner, Edge
from itertools import permutations
import time

# R L2 U F2 L2 B2 D R2 U' F R U B' R F L' B' U2 F' D2 R' U2 B'

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


scramble = input("Enter scramble: ")

# Cross
cube = CubieCube()
cube = do_algorithm(scramble, cube)

crossSolver = IDA_star_cross()
crossSolution = crossSolver.run(cube)
crossSolution = " ".join([ACTIONS[move] for move in crossSolution])

# F2L
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

        cube = CubieCube(corners=corners, edges=edges)
        cube = do_algorithm(scramble, cube)
        cube = do_algorithm(crossSolution, cube)

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

    print("Cross solution:" , crossSolution)

    for alg in f2l_sol:
        for move in alg:
            print(ACTIONS[move], end=" ")
        print()
    all_sol.append(f2l_sol)

end_time_main = time.time()
print("Execution time:", end_time_main - start_time_main, "seconds")

better_sol = []

for solution in all_sol:
    new_sol = []
    for alg in solution:
        new_alg = []
        for move in alg:
            new_alg.append(ACTIONS[move])
        new_sol.append(new_alg)
    better_sol.append(new_sol)

all_sol = []

# OLL
scrambleArr = scramble.split(" ")
for solution_f2l in better_sol:
    cube = Cube(2)
    for move in scrambleArr:
        cube.do_moves(move)
    
    crossSolutionArr = crossSolution.split(" ")
    for move in crossSolutionArr:
        cube.do_moves(move)
    
    for alg in solution_f2l:
        for move in alg:
            cube.do_moves(move)
    
    cube.do_moves("z2")

    solver = OLLSolver()
    solutions = solver.solve(cube)

    for solution in solutions:
        print(solution)