from twophase.cubes.rubiks_cube import Cube
from tables import TableLoader

table = TableLoader()

scramble = "R U2 R' R' F R F' U2 R' F R F'"

cube = Cube(2)

cube.do_moves("z2")
scrambleArr = scramble.split(" ")

for move in scrambleArr:
    cube.do_moves(move)
cube.do_moves("U2")

cube_state = str(cube.cube)
value = table.oll[cube_state]

cube = Cube(3)

cube.do_moves("z2")
scrambleArr = scramble.split(" ")

for move in scrambleArr:
    cube.do_moves(move)
cube.do_moves("U2")
solution = value[11]

solutionArr = solution.split(" ")

for move in solutionArr:
    cube.do_moves(move)

cube.do_moves("U")

cube_state = str(cube.cube)

value = table.pll[cube_state]

print(solution)

print(value[0])
