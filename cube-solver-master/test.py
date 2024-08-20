from twophase.cubes import cubiecube, facecube
from twophase.pieces import Color, Facelet, Corner, Edge

def to_facecube_state(cube):
    """
    Convert CubieCube to FaceCube.
    """
    ret = facecube.FaceCube()
    for i in range(8):
        j = cube.cp[i]
        ori = cube.co[i]
        for k in range(3):
            ret.f[facecube.corner_facelet[i][(k + ori) % 3]] = facecube.corner_color[j][k]
    for i in range(12):
        j = cube.ep[i]
        ori = cube.eo[i]
        for k in range(2):
            facelet_index = facecube.edge_facelet[i][(k + ori) % 2]
            ret.f[facelet_index] = facecube.edge_color[j][k]
    return ret.to_string().replace("U", "-").replace("R", "-").replace("F", "-").replace("L", "-").replace("B", "-")

cube = cubiecube.CubieCube();

cube.move(1)

print(to_facecube_state(cube))