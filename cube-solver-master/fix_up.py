from twophase.cubes import cubiecube, facecube
from twophase.pieces import Color, Facelet, Corner, Edge
import time
import random
import copy
from tables import TableLoader
from twophase.cubes.rubiks_cube import Cube

with open("heuristics/oll.txt", "r") as f:
    line = f.readline()
    while(line):
        if(line.__contains__("OLL")):
            with(open("heuristics/ollNewAlgs.txt", "a")) as fi:
                fi.write(line)
            with(open("heuristics/ollNewIndex.txt", "a")) as fi:
                fi.write(line)
                cube = Cube(2)
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

            with(open("heuristics/ollNewAlgs.txt", "a")) as fi:
                line += "\n"
                fi.write(line)

                while(line != "\n"):
                    print(line)
                    fi.write(line)
                    line = f.readline()

        line = f.readline()
