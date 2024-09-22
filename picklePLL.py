import pickle

pll = {}

with open("heuristics/pllNewIndex.txt", "r") as f:
    line = f.readline()
    while line:
        if("pLL" in line):
            pllID = line.replace("pLL ID: ", "")

            pllStates = [f.readline().replace("\n", "") for i in range(4)]

            with open("heuristics/pllNewAlgs.txt", "r") as f2:
                line2 = f2.readline()
                while(line2):
                    if(pllID in line2):
                        break
                    line2 = f2.readline()

                line2 = f2.readline()

                pllAlgs =[]

                while("pLL" not in line2 and line2):
                    print(line2)
                    pllAlgs.append(line2.replace("\n", ""))
                    line2 = f2.readline()

                for pllState in pllStates:
                    pll[pllState] = pllAlgs

        line = f.readline()

print(pll)

with open("heuristics/pll.pickle", "wb") as f:
    pickle.dump(pll, f)