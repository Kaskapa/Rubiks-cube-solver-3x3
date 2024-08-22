from ..pieces import Corner, Edge, Color
from . import facecube

_cpU = (
    Corner.UBR,
    Corner.URF,
    Corner.UFL,
    Corner.ULB,
    Corner.DFR,
    Corner.DLF,
    Corner.DBL,
    Corner.DRB,
)
_coU = (0, 0, 0, 0, 0, 0, 0, 0)
_epU = (
    Edge.UB,
    Edge.UR,
    Edge.UF,
    Edge.UL,
    Edge.DR,
    Edge.DF,
    Edge.DL,
    Edge.DB,
    Edge.FR,
    Edge.FL,
    Edge.BL,
    Edge.BR,
)
_eoU = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

_cpU2 = (
    Corner.ULB,
    Corner.UBR,
    Corner.URF,
    Corner.UFL,
    Corner.DFR,
    Corner.DLF,
    Corner.DBL,
    Corner.DRB
)

_coU2 = (0, 0, 0, 0, 0, 0, 0, 0)

_epU2 = (
    Edge.UL,
    Edge.UB,
    Edge.UR,
    Edge.UF,
    Edge.DR,
    Edge.DF,
    Edge.DL,
    Edge.DB,
    Edge.FR,
    Edge.FL,
    Edge.BL,
    Edge.BR
)

_eoU2 = (0,0,0,0,0,0,0,0,0,0,0,0)

_cpUP = (
    Corner.UFL,
    Corner.ULB,
    Corner.UBR,
    Corner.URF,
    Corner.DFR,
    Corner.DLF,
    Corner.DBL,
    Corner.DRB
)

_coUP = (0, 0, 0, 0, 0, 0, 0, 0)

_epUP = (
    Edge.UF,
    Edge.UL,
    Edge.UB,
    Edge.UR,
    Edge.DR,
    Edge.DF,
    Edge.DL,
    Edge.DB,
    Edge.FR,
    Edge.FL,
    Edge.BL,
    Edge.BR
)

_eoUP = (0,0,0,0,0,0,0,0,0,0,0,0)

_cpR = (
    Corner.DFR,
    Corner.UFL,
    Corner.ULB,
    Corner.URF,
    Corner.DRB,
    Corner.DLF,
    Corner.DBL,
    Corner.UBR,
)
_coR = (2, 0, 0, 1, 1, 0, 0, 2)
_epR = (
    Edge.FR,
    Edge.UF,
    Edge.UL,
    Edge.UB,
    Edge.BR,
    Edge.DF,
    Edge.DL,
    Edge.DB,
    Edge.DR,
    Edge.FL,
    Edge.BL,
    Edge.UR,
)
_eoR = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

_cpR2 = (
    Corner.DRB,
    Corner.UFL,
    Corner.ULB,
    Corner.DFR,
    Corner.UBR,
    Corner.DLF,
    Corner.DBL,
    Corner.URF
)

_coR2 = (0,0,0,0,0,0,0,0)

_epR2 = (
    Edge.DR,
    Edge.UF,
    Edge.UL,
    Edge.UB,
    Edge.UR,
    Edge.DF,
    Edge.DL,
    Edge.DB,
    Edge.BR,
    Edge.FL,
    Edge.BL,
    Edge.FR
)

_eoR2 = (0,0,0,0,0,0,0,0,0,0,0,0)

_cpRP = (
    Corner.UBR,
    Corner.UFL,
    Corner.ULB,
    Corner.DRB,
    Corner.URF,
    Corner.DLF,
    Corner.DBL,
    Corner.DFR
)

_coRP = (2,0,0,1,1,0,0,2)

_epRP = (
    Edge.BR,
    Edge.UF,
    Edge.UL,
    Edge.UB,
    Edge.FR,
    Edge.DF,
    Edge.DL,
    Edge.DB,
    Edge.UR,
    Edge.FL,
    Edge.BL,
    Edge.DR
)

_eoRP = (0,0,0,0,0,0,0,0,0,0,0,0)

_cpF = (
    Corner.UFL,
    Corner.DLF,
    Corner.ULB,
    Corner.UBR,
    Corner.URF,
    Corner.DFR,
    Corner.DBL,
    Corner.DRB,
)
_coF = (1, 2, 0, 0, 2, 1, 0, 0)
_epF = (
    Edge.UR,
    Edge.FL,
    Edge.UL,
    Edge.UB,
    Edge.DR,
    Edge.FR,
    Edge.DL,
    Edge.DB,
    Edge.UF,
    Edge.DF,
    Edge.BL,
    Edge.BR,
)
_eoF = (0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0)

_cpF2 = (
    Corner.DLF,
    Corner.DFR,
    Corner.ULB,
    Corner.UBR,
    Corner.UFL,
    Corner.URF,
    Corner.DBL,
    Corner.DRB
)

_coF2 = (0,0,0,0,0,0,0,0)

_epF2 = (
    Edge.UR,
    Edge.DF,
    Edge.UL,
    Edge.UB,
    Edge.DR,
    Edge.UF,
    Edge.DL,
    Edge.DB,
    Edge.FL,
    Edge.FR,
    Edge.BL,
    Edge.BR
)

_eoF2 = (0,0,0,0,0,0,0,0,0,0,0,0)

_cpFP = (
    Corner.DFR,
    Corner.URF,
    Corner.ULB,
    Corner.UBR,
    Corner.DLF,
    Corner.UFL,
    Corner.DBL,
    Corner.DRB
)

_coFP = (1,2,0,0,2,1,0,0)

_epFP = (
    Edge.UR,
    Edge.FR,
    Edge.UL,
    Edge.UB,
    Edge.DR,
    Edge.FL,
    Edge.DL,
    Edge.DB,
    Edge.DF,
    Edge.UF,
    Edge.BL,
    Edge.BR
)

_eoFP = (0,1,0,0,0,1,0,0,1,1,0,0)

_cpD = (
    Corner.URF,
    Corner.UFL,
    Corner.ULB,
    Corner.UBR,
    Corner.DLF,
    Corner.DBL,
    Corner.DRB,
    Corner.DFR,
)
_coD = (0, 0, 0, 0, 0, 0, 0, 0)
_epD = (
    Edge.UR,
    Edge.UF,
    Edge.UL,
    Edge.UB,
    Edge.DF,
    Edge.DL,
    Edge.DB,
    Edge.DR,
    Edge.FR,
    Edge.FL,
    Edge.BL,
    Edge.BR,
)
_eoD = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

_cpD2 = (
    Corner.URF,
    Corner.UFL,
    Corner.ULB,
    Corner.UBR,
    Corner.DBL,
    Corner.DRB,
    Corner.DFR,
    Corner.DLF
)

_coD2 = (0,0,0,0,0,0,0,0)

_epD2 = (
    Edge.UR,
    Edge.UF,
    Edge.UL,
    Edge.UB,
    Edge.DL,
    Edge.DB,
    Edge.DR,
    Edge.DF,
    Edge.FR,
    Edge.FL,
    Edge.BL,
    Edge.BR
)

_eoD2 = (0,0,0,0,0,0,0,0,0,0,0,0)

_cpDP = (
    Corner.URF,
    Corner.UFL,
    Corner.ULB,
    Corner.UBR,
    Corner.DRB,
    Corner.DFR,
    Corner.DLF,
    Corner.DBL
)

_coDP = (0,0,0,0,0,0,0,0)

_epDP = (
    Edge.UR,
    Edge.UF,
    Edge.UL,
    Edge.UB,
    Edge.DB,
    Edge.DR,
    Edge.DF,
    Edge.DL,
    Edge.FR,
    Edge.FL,
    Edge.BL,
    Edge.BR
)

_eoDP = (0,0,0,0,0,0,0,0,0,0,0,0)

_cpL = (
    Corner.URF,
    Corner.ULB,
    Corner.DBL,
    Corner.UBR,
    Corner.DFR,
    Corner.UFL,
    Corner.DLF,
    Corner.DRB,
)
_coL = (0, 1, 2, 0, 0, 2, 1, 0)
_epL = (
    Edge.UR,
    Edge.UF,
    Edge.BL,
    Edge.UB,
    Edge.DR,
    Edge.DF,
    Edge.FL,
    Edge.DB,
    Edge.FR,
    Edge.UL,
    Edge.DL,
    Edge.BR,
)
_eoL = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

_cpL2 = (
    Corner.URF,
    Corner.DBL,
    Corner.DLF,
    Corner.UBR,
    Corner.DFR,
    Corner.ULB,
    Corner.UFL,
    Corner.DRB
)

_coL2 = (0,0,0,0,0,0,0,0)

_epL2 = (
    Edge.UR,
    Edge.UF,
    Edge.DL,
    Edge.UB,
    Edge.DR,
    Edge.DF,
    Edge.UL,
    Edge.DB,
    Edge.FR,
    Edge.BL,
    Edge.FL,
    Edge.BR
)

_eoL2 = (0,0,0,0,0,0,0,0,0,0,0,0)

_cpLP = (
    Corner.URF,
    Corner.DLF,
    Corner.UFL,
    Corner.UBR,
    Corner.DFR,
    Corner.DBL,
    Corner.ULB,
    Corner.DRB
)

_coLP = (0,1,2,0,0,2,1,0)

_epLP = (
    Edge.UR,
    Edge.UF,
    Edge.FL,
    Edge.UB,
    Edge.DR,
    Edge.DF,
    Edge.BL,
    Edge.DB,
    Edge.FR,
    Edge.DL,
    Edge.UL,
    Edge.BR
)

_eoLP = (0,0,0,0,0,0,0,0,0,0,0,0)

_cpB = (
    Corner.URF,
    Corner.UFL,
    Corner.UBR,
    Corner.DRB,
    Corner.DFR,
    Corner.DLF,
    Corner.ULB,
    Corner.DBL,
)
_coB = (0, 0, 1, 2, 0, 0, 2, 1)
_epB = (
    Edge.UR,
    Edge.UF,
    Edge.UL,
    Edge.BR,
    Edge.DR,
    Edge.DF,
    Edge.DL,
    Edge.BL,
    Edge.FR,
    Edge.FL,
    Edge.UB,
    Edge.DB,
)
_eoB = (0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1)

_cpB2 = (
    Corner.URF,
    Corner.UFL,
    Corner.DRB,
    Corner.DBL,
    Corner.DFR,
    Corner.DLF,
    Corner.UBR,
    Corner.ULB
)

_coB2 = (0,0,0,0,0,0,0,0)

_epB2 = (
    Edge.UR,
    Edge.UF,
    Edge.UL,
    Edge.DB,
    Edge.DR,
    Edge.DF,
    Edge.DL,
    Edge.UB,
    Edge.FR,
    Edge.FL,
    Edge.BR,
    Edge.BL
)

_eoB2 = (0,0,0,0,0,0,0,0,0,0,0,0)

_cpBP = (
    Corner.URF,
    Corner.UFL,
    Corner.DBL,
    Corner.ULB,
    Corner.DFR,
    Corner.DLF,
    Corner.DRB,
    Corner.UBR
)

_coBP = (0,0,1,2,0,0,2,1)

_epBP = (
    Edge.UR,
    Edge.UF,
    Edge.UL,
    Edge.BL,
    Edge.DR,
    Edge.DF,
    Edge.DL,
    Edge.BR,
    Edge.FR,
    Edge.FL,
    Edge.DB,
    Edge.UB
)

_eoBP = (0,0,0,1,0,0,0,1,0,0,1,1)

_corners = [
    Corner.URF,
    Corner.UFL,
    Corner.ULB,
    Corner.UBR,
    Corner.DFR,
    Corner.DLF,
    Corner.DBL,
    Corner.DRB
]

_edges = [
    Edge.UR,
    Edge.UF,
    Edge.UL,
    Edge.UB,
    Edge.DR,
    Edge.DF,
    Edge.DL,
    Edge.DB,
    Edge.FR,
    Edge.FL,
    Edge.BL,
    Edge.BR
]
_edgesCross_set = set([Edge.UF, Edge.UR, Edge.UL, Edge.UB])

class CubieCube:
    def __init__(self, corners=None, edges=None, cp=None, co=None, ep=None, eo=None, epc=None, eoc=None, epf=None, eof=None, cpf=None, cof=None):
        if corners and edges and cp and co and ep and eo and epc and eoc and epf and eof and cpf and cof:
            self.cp = cp
            self.co = co
            self.ep = ep
            self.eo = eo
            self.epc = epc
            self.eoc = eoc
            self.epf = epf
            self.eof = eof
            self.corners = corners
            self.edges = edges
            self.cpf = cpf
            self.cof = cof
        else:
            self.cp = [
                Corner.URF,
                Corner.UFL,
                Corner.ULB,
                Corner.UBR,
                Corner.DFR,
                Corner.DLF,
                Corner.DBL,
                Corner.DRB
            ]
            self.co = [0,0,0,0,0,0,0,0]
            if corners:
                self.cpf = [_corners[i] if(_corners[i] in corners) else -1 for i in range(8)]
                self.cof = [0 if _corners[i] in corners else -1 for i in range(8)]
                self.corners = corners[:]
            else:
                self.cpf = [
                    Corner.URF,
                    Corner.UFL,
                    Corner.ULB,
                    Corner.UBR,
                    -1,
                    -1,
                    -1,
                    -1
                ]
                self.cof = [0, 0, 0, 0, -1, -1, -1, -1]
                self.corners = [Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR]

            self.ep = [
                Edge.UR,
                Edge.UF,
                Edge.UL,
                Edge.UB,
                Edge.DR,
                Edge.DF,
                Edge.DL,
                Edge.DB,
                Edge.FR,
                Edge.FL,
                Edge.BL,
                Edge.BR,
            ]
            self.eo = [0,0,0,0,0,0,0,0,0,0,0,0]
            self.epc = [
                Edge.UR,
                Edge.UF,
                Edge.UL,
                Edge.UB,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
                -1,
            ]
            self.eoc = [0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1]

            if edges:
                self.epf = [_edges[i] if(_edges[i] in edges) else -1 for i in range(12)]
                self.eof = [0 if _edges[i] in edges else -1 for i in range(12)]
                self.edges = edges[:]
            else:
                self.epf = [
                    -1,
                    -1,
                    -1,
                    -1,
                    -1,
                    -1,
                    -1,
                    -1,
                    Edge.FR,
                    Edge.FL,
                    Edge.BL,
                    Edge.BR,
                ]
                self.eof = [-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0]
                self.edges = [Edge.BL, Edge.BR, Edge.FR, Edge.FL]


    def __deepcopy__(self, memodict={}):
        copy_object = CubieCube(self.corners, self.edges, self.cp, self.co, self.ep, self.eo, self.epc, self.eoc, self.epf, self.eof, self.cpf, self.cof)

        return copy_object

    def corner_multiply(self, b):
        corner_perm = [0,0,0,0,0,0,0,0]
        corner_ori = [0,0,0,0,0,0,0,0]

        for i in range(8):
            corner_perm[i]=(self.cp[b.cp[i]])
            corner_ori[i]=((self.co[b.cp[i]] + b.co[i]) % 3)

        self.cp = corner_perm
        self.co = corner_ori

        corner_f2l_perm = [-1, -1, -1, -1, -1, -1, -1, -1]
        corner_f2l_ori = [-1, -1, -1, -1, -1, -1, -1, -1]

        f2l_i = 0

        for i in range(8):
            if f2l_i == len(self.corners):
                break

            cp_i = corner_perm[i]
            co_i = corner_ori[i]

            if cp_i in self.corners:
                corner_f2l_perm[i] = cp_i
                corner_f2l_ori[i] = co_i
                f2l_i += 1

        self.cof = corner_f2l_ori
        self.cpf = corner_f2l_perm

    def edge_multiply(self, b):
        edge_perm = [0,0,0,0,0,0,0,0,0,0,0,0]
        edge_ori = [0,0,0,0,0,0,0,0,0,0,0,0]

        for i in range(12):
            edge_perm[i]=(self.ep[b.ep[i]])
            edge_ori[i]=((self.eo[b.ep[i]] + b.eo[i]) % 2)

        self.eo = edge_ori
        self.ep = edge_perm

        edge_cross_perm = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        edge_cross_ori = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        edge_f2l_perm = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        edge_f2l_ori = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

        cross_i = 0
        f2l_i = 0
        self_edges_len = len(self.edges)

        for i in range(12):
            if cross_i == 4 and f2l_i == self_edges_len:
                break

            ep_i = edge_perm[i]
            eo_i = edge_ori[i]

            if ep_i in _edgesCross_set:
                edge_cross_perm[i] = ep_i
                edge_cross_ori[i] = eo_i
                cross_i += 1

            if ep_i in self.edges:
                edge_f2l_perm[i] = ep_i
                edge_f2l_ori[i] = eo_i
                f2l_i += 1

        self.eoc = edge_cross_ori
        self.epc = edge_cross_perm
        self.eof = edge_f2l_ori
        self.epf = edge_f2l_perm

    def move(self, i):
        b = MOVE_CUBE[i]
        self.corner_multiply(b)
        self.edge_multiply(b)

    def to_facecube(self):
        face = "------------------------------------------------------"
        for i in range(8):
            j = self.cp[i]
            ori = self.co[i]
            for k in range(3):
                if(facecube.corner_color[j][k] == Color.D):
                    index = facecube.corner_facelet[i][(k + ori) % 3]
                    face= face[:index] + facecube.corner_color[j][k].name + face[index + 1:]
        for i in range(12):
            j = self.ep[i]
            ori = self.eo[i]
            for k in range(2):
                if(facecube.edge_color[j][k] == Color.D):
                    index = facecube.edge_facelet[i][(k + ori) % 2]
                    face = face[:index] + facecube.edge_color[j][k].name + face[index + 1:]
        return face

# we store the six possible clockwise 1/4 turn moves in the following array.
MOVE_CUBE = [CubieCube() for i in range(18)]

MOVE_CUBE[0].cp = _cpU
MOVE_CUBE[0].co = _coU
MOVE_CUBE[0].ep = _epU
MOVE_CUBE[0].eo = _eoU

MOVE_CUBE[1].cp = _cpR
MOVE_CUBE[1].co = _coR
MOVE_CUBE[1].ep = _epR
MOVE_CUBE[1].eo = _eoR

MOVE_CUBE[2].cp = _cpF
MOVE_CUBE[2].co = _coF
MOVE_CUBE[2].ep = _epF
MOVE_CUBE[2].eo = _eoF

MOVE_CUBE[3].cp = _cpD
MOVE_CUBE[3].co = _coD
MOVE_CUBE[3].ep = _epD
MOVE_CUBE[3].eo = _eoD

MOVE_CUBE[4].cp = _cpL
MOVE_CUBE[4].co = _coL
MOVE_CUBE[4].ep = _epL
MOVE_CUBE[4].eo = _eoL

MOVE_CUBE[5].cp = _cpB
MOVE_CUBE[5].co = _coB
MOVE_CUBE[5].ep = _epB
MOVE_CUBE[5].eo = _eoB


MOVE_CUBE[6].cp = _cpU2
MOVE_CUBE[6].co = _coU2
MOVE_CUBE[6].ep = _epU2
MOVE_CUBE[6].eo = _eoU2

MOVE_CUBE[7].cp = _cpR2
MOVE_CUBE[7].co = _coR2
MOVE_CUBE[7].ep = _epR2
MOVE_CUBE[7].eo = _eoR2

MOVE_CUBE[8].cp = _cpF2
MOVE_CUBE[8].co = _coF2
MOVE_CUBE[8].ep = _epF2
MOVE_CUBE[8].eo = _eoF2

MOVE_CUBE[9].cp = _cpD2
MOVE_CUBE[9].co = _coD2
MOVE_CUBE[9].ep = _epD2
MOVE_CUBE[9].eo = _eoD2

MOVE_CUBE[10].cp = _cpL2
MOVE_CUBE[10].co = _coL2
MOVE_CUBE[10].ep = _epL2
MOVE_CUBE[10].eo = _eoL2

MOVE_CUBE[11].cp = _cpB2
MOVE_CUBE[11].co = _coB2
MOVE_CUBE[11].ep = _epB2
MOVE_CUBE[11].eo = _eoB2


MOVE_CUBE[12].cp = _cpUP
MOVE_CUBE[12].co = _coUP
MOVE_CUBE[12].ep = _epUP
MOVE_CUBE[12].eo = _eoUP

MOVE_CUBE[13].cp = _cpRP
MOVE_CUBE[13].co = _coRP
MOVE_CUBE[13].ep = _epRP
MOVE_CUBE[13].eo = _eoRP

MOVE_CUBE[14].cp = _cpFP
MOVE_CUBE[14].co = _coFP
MOVE_CUBE[14].ep = _epFP
MOVE_CUBE[14].eo = _eoFP

MOVE_CUBE[15].cp = _cpDP
MOVE_CUBE[15].co = _coDP
MOVE_CUBE[15].ep = _epDP
MOVE_CUBE[15].eo = _eoDP

MOVE_CUBE[16].cp = _cpLP
MOVE_CUBE[16].co = _coLP
MOVE_CUBE[16].ep = _epLP
MOVE_CUBE[16].eo = _eoLP

MOVE_CUBE[17].cp = _cpBP
MOVE_CUBE[17].co = _coBP
MOVE_CUBE[17].ep = _epBP
MOVE_CUBE[17].eo = _eoBP