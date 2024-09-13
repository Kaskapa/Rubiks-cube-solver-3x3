from twophase.cubes.rubiks_cube import Cube
from tables import TableLoader

table = TableLoader()

class OLLSolver:
    def __init__(self):
        self.table = table.oll

    def solve(self, cube):
        checkCube = Cube(2)
        checkCube.do_moves("z2")
        if(str(cube.cube[0]) == str(checkCube.cube[0])):
            return ["Cube is already solved"]

        cube_state = str(cube.cube)
        counter = 0
        while cube_state not in self.table:
            if(counter > 4):
                return ["Error: OLL not found", cube_state]
            cube.do_moves("U")
            cube_state = str(cube.cube)
            counter += 1

        u_moves = ["U" for i in range(counter)]

        solutions = self.table[cube_state]
        solutions.append(" ".join(u_moves))

        return solutions

if __name__ == "__main__":

    scramble = "F B' R U2 L2 B R' D' L' U F' R' D' B L U B2 D' R2 B L' F U2 R B' L' U' D F B2 D' F' D L B2 L' R D' R' L2 D2 L' D2 L D' L F2 D' F D' F' D2 F2"
    # scramble = ""
    cube = Cube(2)
    scrambleArr = scramble.split(" ")
    for move in scrambleArr:
        cube.do_moves(move)
    cube.do_moves("z2")

    print(cube.cube)

    solver = OLLSolver()
    solutions = solver.solve(cube)

    for solution in solutions:
        print(solution)
