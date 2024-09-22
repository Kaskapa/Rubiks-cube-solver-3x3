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
        self.inspection = "z2"
        self.cross_solution = ""
        self.f2l_solutions = []
        self.preMoves = ""
        self.oll_solution = ""
        self.prePLLMoves = ""
        self.pll_solution = ""
        self.postMoves = ""

    def getCross(self):
        return self.cross_solution
    
    def getF2L(self):
        return self.f2l_solutions

    def getPre(self):
        return self.preMoves
    
    def getOLL(self):
        return self.oll_solution

    def getPrePLL(self):
        return self.prePLLMoves

    def getPLL(self):
        return self.pll_solution

    def getInspection(self):
        return self.inspection
    
    def getPost(self):
        return self.postMoves

    def setCross(self, crossSol):
        self.cross_solution = crossSol

    def setF2L(self, f2lSolutions):
        for f2lSol in f2lSolutions:
            self.f2l_solutions.append(f2lSol)
    
    def setPre(self, pre):
        self.preMoves = pre

    def setOLL(self, oll):
        self.oll_solution = oll

    def setPrePLL(self, prePLL):
        self.prePLLMoves = prePLL

    def setPLL(self, pll):
        self.pll_solution = pll

    def setPost(self, post):
        self.postMoves = post

    def toDict(self):
        return {
            "inspection": self.inspection,
            "cross": self.cross_solution,
            "f2l": self.f2l_solutions,
            "pre": self.preMoves,
            "oll": self.oll_solution,
            "prePLL": self.prePLLMoves,
            "pll": self.pll_solution,
            "post": self.postMoves
        }

class Solver:
    def __init__(self, scramble):
        self.scramble = scramble
        self.cube = CubieCube()
        self.cube = do_algorithm(scramble, self.cube)
        
        self.f2l_corners = [Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR]
        self.f2l_edges = [Edge.FR, Edge.FL, Edge.BL, Edge.BR]
        self.f2l_corners_combinations = list(permutations(self.f2l_corners, 4))
        self.f2l_edges_combinations = list(permutations(self.f2l_edges, 4))

    def crossSolver(self):
        crossSolver = IDA_star_cross()
        crossSolution = crossSolver.run(self.cube)
        crossSolution = " ".join([ACTIONS[move] for move in crossSolution])

        solution = Solution()
        solution.setCross(crossSolution)

        return solution
    
    def _toStringArray(self, array):
        string = [value.value for value in array]
        string.sort()
        string = "".join(str(x) for x in string)

        return string

    def f2lSolver(self, crossSolution):
        f2l_solutions = []

        sol_mem = {}

        for j in range(len(self.f2l_corners_combinations)):
            f2l_sol = []
            f2l_corners = self.f2l_corners_combinations[j]
            f2l_edges= self.f2l_edges_combinations[j]
            for i in range(len(f2l_corners)):
                corners = f2l_corners[:i+1]
                edges = f2l_edges[:i+1]

                cube = CubieCube(corners=corners, edges=edges)
                cube = do_algorithm(self.scramble, cube)
                cube = do_algorithm(crossSolution.getCross(), cube)

                for alg in f2l_sol:
                    for move in alg:
                        cube.move(move)

                cornerStr = self._toStringArray(corners)
                edgeStr = self._toStringArray(edges)

                if (cornerStr, edgeStr, str(cube.cof), str(cube.cpf), str(cube.eo), str(cube.ep)) in sol_mem:
                    f2l_sol.append(sol_mem[(cornerStr, edgeStr, str(cube.cof), str(cube.cpf), str(cube.eo), str(cube.ep))])
                    continue

                solver = IDA_star_F2L(corners, edges, cornerStr, edgeStr)
                moves = solver.run(cube)

                f2l_sol.append(moves)

                sol_mem[(cornerStr, edgeStr, str(cube.cof), str(cube.cpf), str(cube.eo), str(cube.ep))] = moves

            f2lSolutionArray = []
            for alg in f2l_sol:
                solutionString = ""
                for move in alg:
                    solutionString += ACTIONS[move] + " "
                f2lSolutionArray.append(solutionString)

            f2l_solution = copy.deepcopy(crossSolution)
            f2l_solution.setF2L(f2lSolutionArray)
            f2l_solutions.append(f2l_solution)

        return f2l_solutions

    def _isPreMoves(self, moves):
        return "U" in moves and "L" not in moves and "R" not in moves and "F" not in moves and "B" not in moves and "D" not in moves and "M" not in moves and "S" not in moves and "E" not in moves

    def ollSolver(self, f2l_solutions):
        oll_all = []
        scrambleArr = self.scramble.split(" ")
        for solution_f2l in f2l_solutions:
            self.cube = Cube(2)
            for move in scrambleArr:
                self.cube.do_moves(move)
            
            for move in solution_f2l.getCross().split(" "):
                self.cube.do_moves(move)
            
            for alg in solution_f2l.getF2L():
                for move in alg.split(" "):
                    self.cube.do_moves(move)
            
            self.cube.do_moves("z2")

            solver = OLLSolver()
            OLL_solutions = solver.solve(self.cube)

            if(self._isPreMoves(OLL_solutions[-1])):
                solution_f2l.setPre(OLL_solutions[-1])
            for oll_solution in OLL_solutions:
                if((oll_solution == OLL_solutions[-1] and self._isPreMoves(oll_solution)) or oll_solution == ""):
                    continue
                solution_f2l.setOLL(oll_solution)
                oll_all.append(copy.deepcopy(solution_f2l))
        
        return oll_all

    def pllSolver(self, oll_all):
        all_pll = []
        scrambleArr = self.scramble.split(" ")
        for solution_oll in oll_all:
            self.cube = Cube(3)
            for move in scrambleArr:
                self.cube.do_moves(move)
            
            crossSolutionArr = solution_oll.getCross().split(" ")
            for move in crossSolutionArr:
                self.cube.do_moves(move)
            
            for alg in solution_oll.getF2L():
                for move in alg.split(" "):
                    self.cube.do_moves(move)
            
            self.cube.do_moves("z2")

            if("Cube is already solved" not in solution_oll.getOLL()):
                for move in solution_oll.getPre().split(" "):
                    self.cube.do_moves(move)

                for move in solution_oll.getOLL().split(" "):
                    self.cube.do_moves(move)

            solver = PLLSolver()
            PLLSolutions = solver.solve(self.cube)

            if(self._isPreMoves(PLLSolutions[-1])):
                solution_oll.setPrePLL(PLLSolutions[-1])
            for pll_solution in PLLSolutions:
                pllCube = copy.deepcopy(self.cube)

                for move in solution_oll.getPrePLL().split(" "):
                    pllCube.do_moves(move)
                
                for move in pll_solution.split(" "):
                    pllCube.do_moves(move)

                checkCube = Cube(3)
                checkCube.do_moves("z2")

                postMoves = ""
                counter = 0

                while str(checkCube.cube) != str(pllCube.cube) and counter < 5:
                    pllCube.do_moves("U")
                    postMoves += "U "
                    counter += 1

                if((pll_solution == PLLSolutions[-1] and self._isPreMoves(PLLSolutions)) or pll_solution == ""):
                    continue
                solution_oll.setPLL(pll_solution)
                solution_oll.setPost(postMoves)
                all_pll.append(copy.deepcopy(solution_oll))

        return all_pll
    
    def _convertToZ2(self, string):
        stringArr = string.split(" ")
        final = ""
        for move in stringArr:
            if "U" in move:
                final += move.replace("U", "D") + " "
            elif "D" in move:
                final += move.replace("D", "U") + " "
            elif "L" in move:
                final += move.replace("L", "R") + " "
            elif "R" in move:
                final += move.replace("R", "L") + " "
            elif "F" in move:
                final += move.replace("F", "F") + " "
            elif "B" in move:
                final += move.replace("B", "B") + " "
        return final

    def solve(self):
        crossSolution = self.crossSolver()
        f2l_solutions = self.f2lSolver(crossSolution)
        oll_all = self.ollSolver(f2l_solutions)
        all_pll = self.pllSolver(oll_all)

        for i, solution in enumerate(all_pll):
            solution.setCross(self._convertToZ2(solution.getCross()))
            for j, f2l in enumerate(solution.getF2L()):
                solution.getF2L()[j] = self._convertToZ2(f2l)
            
            all_pll[i] = copy.deepcopy(solution)

        return all_pll
    

if __name__ == "__main__":
    scramble = input("Enter scramble: ")

    startTime = time.time()

    solver = Solver(scramble)
    solutions = solver.solve()

    print("Time taken: " + str(time.time() - startTime))

    for solution in solutions:
        print("Scramble: " + scramble)
        print("Cross: " + solution.getCross())
        for f2l in solution.getF2L():
            print("F2L: " + f2l)
        print("OLL: " + solution.getPre() + " " + solution.getOLL())
        print("PLL: " + solution.getPrePLL() + " " + solution.getPLL())

        print()
        print()