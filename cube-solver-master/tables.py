import pickle

class TableLoader():
    def __init__(self):
        self.heurUBR = self.loadHeuristic("heuristics/heuristicsCornerUBR.pickle")
        self.heurULB = self.loadHeuristic("heuristics/heuristicsCornerULB.pickle")
        self.heurUFL = self.loadHeuristic("heuristics/heuristicsCornerUFL.pickle")
        self.heurURF = self.loadHeuristic("heuristics/heuristicsCornerURF.pickle")
        self.heurBR = self.loadHeuristic("heuristics/heuristicsEdgeBR.pickle")
        self.heurBL = self.loadHeuristic("heuristics/heuristicsEdgeBL.pickle")
        self.heurFR = self.loadHeuristic("heuristics/heuristicsEdgeFR.pickle")
        self.heurFL = self.loadHeuristic("heuristics/heuristicsEdgeFL.pickle")

        self.heurCross = self.loadHeuristic("heuristics/heuristicsEdgeCross.pickle")

        self.heurUBR_ULB = self.loadHeuristic("heuristics/heuristicsCornerUBR_ULB.pickle")
        self.heurUFL_UBR = self.loadHeuristic("heuristics/heuristicsCornerUFL_UBR.pickle")
        self.heurUFL_ULB = self.loadHeuristic("heuristics/heuristicsCornerUFL_ULB.pickle")
        self.heurUFL_URF = self.loadHeuristic("heuristics/heuristicsCornerUFL_URF.pickle")
        self.heurURF_UBR = self.loadHeuristic("heuristics/heuristicsCornerURF_UBR.pickle")
        self.heurURF_ULB = self.loadHeuristic("heuristics/heuristicsCornerURF_ULB.pickle")

        self.heurBR_BL = self.loadHeuristic("heuristics/heuristicsEdgeBR_BL.pickle")
        self.heurFL_BR = self.loadHeuristic("heuristics/heuristicsEdgeFL_BR.pickle")
        self.heurFL_BL = self.loadHeuristic("heuristics/heuristicsEdgeFL_BL.pickle")
        self.heurFL_FR = self.loadHeuristic("heuristics/heuristicsEdgeFL_FR.pickle")
        self.heurFR_BL = self.loadHeuristic("heuristics/heuristicsEdgeFR_BL.pickle")
        self.heurFR_BR = self.loadHeuristic("heuristics/heuristicsEdgeFR_BR.pickle")

        self.heurFR_FL_BL = self.loadHeuristic("heuristics/heuristicsEdge_8_9_10.pickle")
        self.heurFR_FL_BR = self.loadHeuristic("heuristics/heuristicsEdge_8_9_11.pickle")
        self.heurBR_FL_BL = self.loadHeuristic("heuristics/heuristicsEdge_11_9_10.pickle")
        self.heurBR_BL_FR = self.loadHeuristic("heuristics/heuristicsEdge_11_10_8.pickle")

        self.heurURF_UFL_ULB = self.loadHeuristic("heuristics/heuristicsCorner_0_1_2.pickle")
        self.heurURF_UFL_UBR = self.loadHeuristic("heuristics/heuristicsCorner_0_1_3.pickle")
        self.heurUBR_UFL_ULB = self.loadHeuristic("heuristics/heuristicsCorner_3_1_2.pickle")
        self.heurUBR_ULB_URF = self.loadHeuristic("heuristics/heuristicsCorner_3_2_0.pickle")

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
        print("FR_FL_BL", len(self.heurFR_FL_BL))
        print("FR_FL_BR", len(self.heurFR_FL_BR))
        print("BR_FL_BL", len(self.heurBR_FL_BL))
        print("BR_BL_FR", len(self.heurBR_BL_FR))
        print("URF_UFL_ULB", len(self.heurURF_UFL_ULB))
        print("URF_UFL_UBR", len(self.heurURF_UFL_UBR))
        print("UBR_UFL_ULB", len(self.heurUBR_UFL_ULB))
        print("UBR_ULB_URF", len(self.heurUBR_ULB_URF))