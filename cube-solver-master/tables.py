import pickle

class TableLoader():
    def __init__(self):
        self.heurUBR = self.loadHeuristic("heuristicsCornerUBR.pickle")
        self.heurULB = self.loadHeuristic("heuristicsCornerULB.pickle")
        self.heurUFL = self.loadHeuristic("heuristicsCornerUFL.pickle")
        self.heurURF = self.loadHeuristic("heuristicsCornerURF.pickle")
        self.heurBR = self.loadHeuristic("heuristicsEdgeBR.pickle")
        self.heurBL = self.loadHeuristic("heuristicsEdgeBL.pickle")
        self.heurFR = self.loadHeuristic("heuristicsEdgeFR.pickle")
        self.heurFL = self.loadHeuristic("heuristicsEdgeFL.pickle")

        self.heurCross = self.loadHeuristic("heuristicsEdgeCross.pickle")

        self.heurUBR_ULB = self.loadHeuristic("heuristicsCornerUBR_ULB.pickle")
        self.heurUFL_UBR = self.loadHeuristic("heuristicsCornerUFL_UBR.pickle")
        self.heurUFL_ULB = self.loadHeuristic("heuristicsCornerUFL_ULB.pickle")
        self.heurUFL_URF = self.loadHeuristic("heuristicsCornerUFL_URF.pickle")
        self.heurURF_UBR = self.loadHeuristic("heuristicsCornerURF_UBR.pickle")
        self.heurURF_ULB = self.loadHeuristic("heuristicsCornerURF_ULB.pickle")

        self.heurBR_BL = self.loadHeuristic("heuristicsEdgeBR_BL.pickle")
        self.heurFL_BL = self.loadHeuristic("heuristicsEdgeFL_BL.pickle")
        self.heurFL_BR = self.loadHeuristic("heuristicsEdgeFL_BR.pickle")
        self.heurFL_FR = self.loadHeuristic("heuristicsEdgeFL_FR.pickle")
        self.heurFR_BL = self.loadHeuristic("heuristicsEdgeFR_BL.pickle")
        self.heurFR_BR = self.loadHeuristic("heuristicsEdgeFR_BR.pickle")

    def loadHeuristic(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def checkHeuristics(self):
        print("UBR", len(self.heurUBR))
        print("ULB", len(self.heurULB))
        print("UFL", len(self.heurUFL))
        print("URF", len(self.heurURF))
        print("BR", len(self.heurBR))
        print("BL", len(self.heurBL))
        print("FR", len(self.heurFR))
        print("FL", len(self.heurFL))
        print("Cross", len(self.heurCross))
        print("UBR_ULB", len(self.heurUBR_ULB))
        print("UFL_UBR", len(self.heurUFL_UBR))
        print("UFL_ULB", len(self.heurUFL_ULB))
        print("UFL_URF", len(self.heurUFL_URF))
        print("URF_UBR", len(self.heurURF_UBR))
        print("URF_ULB", len(self.heurURF_ULB))
        print("BR_BL", len(self.heurBR_BL))
        print("FL_BL", len(self.heurFL_BL))
        print("FL_BR", len(self.heurFL_BR))
        print("FL_FR", len(self.heurFL_FR))
        print("FR_BL", len(self.heurFR_BL))
        print("FR_BR", len(self.heurFR_BR))

