from twophase.cubes.rubiks_cube import Cube
from tables import TableLoader
import copy

table = TableLoader()

class PLLSolver:
    def __init__(self):
        self.table = table.pll
        self.solutions = []

    def solve(self, cube):
        checkCube = Cube(3)
        checkCube.do_moves("z2")
        if(str(cube.cube) == str(checkCube.cube)):
            return ["Cube is already solved"]

        cube_state = str(cube.cube)
        counter = 0
        while cube_state not in self.table:
            if(counter > 4):
                return ["Error: PLL not found", cube_state]
            cube.do_moves("U")
            cube_state = str(cube.cube)
            counter += 1

        u_moves = ["U" for i in range(counter)]

        self.solutions = copy.deepcopy(self.table[cube_state])
        self.solutions.append(" ".join(u_moves))

        return self.solutions

if __name__ == "__main__":

    scramble = "x R2 D2 R U R' D2 R U' R x'"
    # scramble = ""
    cube = Cube(3)
    scrambleArr = scramble.split(" ")
    cube.do_moves("z2")
    for move in scrambleArr:
        cube.do_moves(move)

    print(cube.cube)    

    solver = PLLSolver()
    solutions = solver.solve(cube)

    for solution in solutions:
        print(solution)
