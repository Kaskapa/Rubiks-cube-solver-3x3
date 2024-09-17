from idaStarCross import IDA_star_cross
from idaStarF2L import IDA_star_F2L
from cheapOLLSolver import OLLSolver
from cheapPLLSolver import PLLSolver
from twophase.cubes.cubiecube import CubieCube
from twophase.cubes.rubiks_cube import Cube
from twophase.pieces import Corner, Edge
from itertools import permutations
import time
import copy

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

class Solution:
    def __init__(self):
        self.cross_solution = ""
        self.f2l_solution = ""
        self.preMoves = ""
        self.oll_solution = ""
        self.prePLLMoves = ""
        self.pll_solution = ""

    def getCross(self):
        return self.cross_solution
    
    def getF2L(self):
        return self.f2l_solution

    def getPre(self):
        return self.preMoves
    
    def getOLL(self):
        return self.oll_solution

    def getPrePLL(self):
        return self.prePLLMoves

    def getPLL(self):
        return self.pll_solution

    def setCross(self, crossSol):
        self.cross_solution = crossSol

    def setF2L(self, f2lSol):
        self.f2l_solution = f2lSol
    
    def setPre(self, pre):
        self.preMoves = pre

    def setOLL(self, oll):
        self.oll_solution = oll

    def setPrePLL(self, prePLL):
        self.prePLLMoves = prePLL

    def setPLL(self, pll):
        self.pll_solution = pll

scramble = input("Enter scramble: ")

# Cross
cube = CubieCube()
cube = do_algorithm(scramble, cube)

crossSolver = IDA_star_cross()
crossSolution = crossSolver.run(cube)
crossSolution = " ".join([ACTIONS[move] for move in crossSolution])

newSol = Solution()
newSol.setCross(crossSolution)

# F2L
f2l_solutions = []

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

    f2lSTRING = ""

    for alg in f2l_sol:
        for move in alg:
            f2lSTRING += ACTIONS[move] + " "
            print(ACTIONS[move], end=" ")
        print()
    all_sol.append(f2l_sol)

    f2l_solution = copy.deepcopy(newSol)
    f2l_solution.setF2L(f2lSTRING)
    f2l_solutions.append(f2l_solution)

end_time_main = time.time()
print("Execution time:", end_time_main - start_time_main, "seconds")

# OLL

oll_all = []
scrambleArr = scramble.split(" ")
for solution_f2l in f2l_solutions:
    cube = Cube(2)
    for move in scrambleArr:
        cube.do_moves(move)
    
    crossSolutionArr = crossSolution.split(" ")
    for move in solution_f2l.getCross().split(" "):
        cube.do_moves(move)
    
    for move in solution_f2l.getF2L().split(" "):
        cube.do_moves(move)
    
    cube.do_moves("z2")

    solver = OLLSolver()
    OLL_solutions = solver.solve(cube)

    if("U" in OLL_solutions[-1] and "L" not in OLL_solutions[-1] and "R" not in OLL_solutions[-1] and "F" not in OLL_solutions[-1] and "B" not in OLL_solutions[-1] and "D" not in OLL_solutions[-1] and "M" not in OLL_solutions[-1] and "S" not in OLL_solutions[-1] and "E" not in OLL_solutions[-1]):
        solution_f2l.setPre(OLL_solutions[-1])
    for oll_solution in OLL_solutions:
        solution_f2l.setOLL(oll_solution)
        oll_all.append(copy.deepcopy(solution_f2l))

# PLL
all_pll = []
scrambleArr = scramble.split(" ")
for solution_oll in oll_all:
    cube = Cube(3)
    for move in scrambleArr:
        cube.do_moves(move)
    
    crossSolutionArr = solution_oll.getCross().split(" ")
    for move in crossSolutionArr:
        cube.do_moves(move)
    
    for move in solution_oll.getF2L().split(" "):
        cube.do_moves(move)
    
    cube.do_moves("z2")

    if("Cube is already solved" not in solution_oll.getOLL()):
        for move in solution_oll.getPre().split(" "):
            cube.do_moves(move)

        for move in solution_oll.getOLL().split(" "):
            cube.do_moves(move)

    solver = PLLSolver()
    PLLSolutions = solver.solve(cube)

    if("U" in PLLSolutions[-1] and "L" not in PLLSolutions[-1] and "R" not in PLLSolutions[-1] and "F" not in PLLSolutions[-1] and "B" not in PLLSolutions[-1] and "D" not in PLLSolutions[-1] and "M" not in PLLSolutions[-1] and "S" not in PLLSolutions[-1] and "E" not in PLLSolutions[-1]):
        solution_oll.setPrePLL(PLLSolutions[-1])
    for pll_solution in PLLSolutions:
        solution_oll.setPLL(pll_solution)
        all_pll.append(copy.deepcopy(solution_oll))

for pll in all_pll:
    print("Cross solution: " + pll.getCross())
    print("F2L Solution: " + pll.getF2L())
    print("Pre OLL Moves: " + pll.getPre())
    print("OLL solution: " + pll.getOLL())
    print("Pre PLL Moves: " + pll.getPrePLL())
    print("PLL solution: " + pll.getPLL()) 
    print()

print(len(all_pll))