from twophase.cubes.rubiks_cube import Cube

# scramble = ["F'", 'R', 'F', "R'", "U'", 'S', "R'", 'U', 'R', "S'", 'y']
# scramble = ["y'", "S'", "R", 'U', "R'", "S", "U'", "R'", "F", "R", "F'"]
scramble = ["E"]
cube = Cube(0)


for move in scramble:       
    cube.do_moves(move)

print(cube.cube)    