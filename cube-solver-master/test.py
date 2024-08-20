from twophase.cubes import cubiecube
from twophase.pieces import Color, Facelet, Corner, Edge

cube = cubiecube.CubieCube(corners=[Corner.UFL, Corner.URF], edges=[Edge.FL, Edge.FR]);

print(cube.to_facecube().to_string())