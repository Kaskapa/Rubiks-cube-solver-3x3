from twophase.cubes.rubiks_cube import Cube
import pickle

oll = {}

with open("heuristics/ollNewIndex.txt", "r") as f:
    line = f.readline()
    while line:
        if("OLL" in line):
            ollID = line.replace("OLL ID: ", "")

            ollStates = [f.readline().replace("\n", "") for i in range(1)]

            with open("heuristics/ollNewAlgs.txt", "r") as f2:
                line2 = f2.readline()
                while(line2):
                    if(ollID in line2):
                        break
                    line2 = f2.readline()

                line2 = f2.readline()

                ollAlgs =[]

                while("OLL" not in line2 and line2):
                    print(line2)
                    ollAlgs.append(line2.replace("\n", ""))
                    line2 = f2.readline()

                for ollState in ollStates:
                    oll[ollState] = ollAlgs

        line = f.readline()

with open("heuristics/oll.pickle", "wb") as f:
    pickle.dump(oll, f)