from twophase.cubes import cubiecube, facecube
from twophase.pieces import Color, Facelet, Corner, Edge
import time
import random
import copy
from tables import TableLoader
from twophase.cubes.rubiks_cube import Cube

with open("heuristics/pll.txt", "r") as f:
    line = f.readline()
    while(line):
        if(line.__contains__("pLL")):
            with(open("heuristics/pllNewAlgs.txt", "a")) as fi:
                fi.write(line)
            with(open("heuristics/pllNewIndex.txt", "a")) as fi:
                fi.write(line)
                cube = Cube(3)
                cube.do_moves("z2")
                line = f.readline()
                line = f.readline()
                line = f.readline()
                line = f.readline().replace("\n", "")

                lineArr = line.split(" ")
                lineArr = list(reversed(lineArr))
                print(lineArr)
                for move in lineArr:
                    cube.do_alternative_moves(move)

                fi.write(str(cube.cube))
                fi.write("\n")

                cube = Cube(3)
                cube.do_moves("z2")
                cube.do_moves("U")

                for move in lineArr:
                    cube.do_alternative_moves(move)

                fi.write(str(cube.cube))
                fi.write("\n")

                cube = Cube(3)
                cube.do_moves("z2")
                cube.do_moves("U2")

                for move in lineArr:
                    cube.do_alternative_moves(move)

                fi.write(str(cube.cube))
                fi.write("\n")

                cube = Cube(3)
                cube.do_moves("z2")
                cube.do_moves("U'")

                for move in lineArr:
                    cube.do_alternative_moves(move)

                fi.write(str(cube.cube))
                fi.write("\n")

            with(open("heuristics/pllNewAlgs.txt", "a")) as fi:
                line += "\n"

                while(line != "\n"):
                    print(line)
                    fi.write(line)
                    line = f.readline()

        line = f.readline()
