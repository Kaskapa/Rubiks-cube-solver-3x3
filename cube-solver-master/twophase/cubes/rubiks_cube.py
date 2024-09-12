import copy

class Cube:
    def __init__(self, type):
        self.cateogry = [0,0,0,0]
        self.corners = []
        self.edges = []
        self.pairs = []
        self.CORNERTEMPLATE = [[[0,0], [1,0], [4,1]], [[0,1], [3,1], [4,0]], [[0,2], [1,1], [2,0]], [[0,3],[2,1], [3,0]], [[5,2], [1,2], [4,3]], [[5,3], [3,3], [4,2]], [[5,0], [1,3], [2,2]], [[5,1], [2,3], [3,2]]]
        self.EDGETEMPLATE = [[[0,0], [4,0]], [[0,1], [1,0]], [[0,2],[3,0]], [[0,3], [2,0]], [[4,2], [1,1]], [[2,1], [1,2]], [[3,1], [2,2]], [[4,1], [3,2]], [[5,0], [2,3]], [[5,1], [1,3]], [[5,2], [3,3]], [[5,3], [4,3]]]
        self.PAIRTEMPLATE = [[0,4],[1,7],[2, 5], [3,6], [4, 4], [5, 7], [6, 5], [7,6], [0,0], [2,3], [4, 11], [6,8], [1, 0], [3,3], [7, 8], [5, 11], [0, 1], [1, 2], [4, 9], [5, 10], [2, 1], [3,2], [6,9], [7, 10]]
        self.CORRECTPAIRTEMPLATE = [[2,1], [2,1], [2,1], [2,1], [2,1], [2,1], [2,1], [2,1], [0, 2], [0,2], [0,2], [0,2], [0,2], [0,1], [0,1], [0,2], [0, 1], [0,1], [0,1], [0,1], [0,1], [0,2], [0,1], [0,2]];
        self.WHITEF2L = [[1,2], [2,3], [3,4], [4,1]]
        self.previousMoves = []
        if(type == 0):
            self.cube = [
                [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]],

                [[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]],

                [[2, 2, 2],
                    [2, 2, 2],
                    [2, 2, 2]],

                [[3, 3, 3],
                    [3, 3, 3],
                    [3, 3, 3]],

                [[4, 4, 4],
                    [4, 4, 4],
                    [4, 4, 4]],

                [[5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5]]
            ]
        elif(type== 1):
            self.cube = [
                [[-1, 0, -1],
                [0, -1, 0],
                [-1, 0, -1]],

                [[-1, 1, -1],
                [-1, 1, -1],
                [-1, -1, -1]],

                [[-1, 2, -1],
                [-1, 2, -1],
                [-1, -1, -1]],

                [[-1, 3, -1],
                [-1, 3, -1],
                [-1, -1, -1]],

                [[-1, 4, -1],
                [-1, 4, -1],
                [-1, -1, -1]],

                [[-1, -1, -1],
                [-1, -1, -1],
                [-1, -1, -1]]
            ]
        elif(type == 2):
            self.cube = [
                [
                    [-1,-1,-1],
                    [-1,-1,-1],
                    [-1,-1,-1]
                ],
                [
                    [-1, -1, -1],
                    [-1, -1, -1],
                    [-1, -1, -1]
                ],
                [
                    [-1, -1, -1],
                    [-1, -1, -1],
                    [-1, -1, -1]
                ],
                [
                    [-1, -1, -1],
                    [-1, -1, -1],
                    [-1, -1, -1]
                ],
                [
                    [-1, -1, -1],
                    [-1, -1, -1],
                    [-1, -1, -1]
                ],
                [
                    [5, 5, 5],
                    [5, -1, 5],
                    [5, 5, 5]
                ]
            ]
        elif(type == 3):
            self.cube = [
                [
                    [-1, -1, -1],
                    [-1, -1, -1],
                    [-1, -1, -1]
                ],
                [
                    [-1, -1, -1],
                    [-1, -1, -1],
                    [1, 1, 1]
                ],
                [
                    [-1, -1, -1],
                    [-1, -1, -1],
                    [2, 2, 2]
                ],
                [
                    [-1, -1, -1],
                    [-1, -1, -1],
                    [3, 3, 3]
                ],
                [
                    [-1, -1, -1],
                    [-1, -1, -1],
                    [4, 4, 4]
                ],
                [
                    [5,5,5],
                    [5,-1,5],
                    [5,5,5]
                ]
            ]
    def reset(self):
        self.cube = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
            [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
            [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
            [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        ]

    def is_up_cross_solved(self, color):
        return (self.cube[0][0][1] == color and
                self.cube[0][1][0] == color and
                self.cube[0][1][1] == color and
                self.cube[0][1][2] == color and
                self.cube[0][2][1] == color and
                self.cube[1][0][1] == self.cube[1][1][1] and
                self.cube[2][0][1] == self.cube[2][1][1] and
                self.cube[3][0][1] == self.cube[3][1][1] and
                self.cube[4][0][1] == self.cube[4][1][1])

    def is_left_cross_solved(self, color):
        return (self.cube[1][0][1] == color and
                self.cube[1][1][0] == color and
                self.cube[1][1][1] == color and
                self.cube[1][1][2] == color and
                self.cube[1][2][1] == color and
                self.cube[0][1][0] == self.cube[0][1][1] and
                self.cube[2][1][0] == self.cube[2][1][1] and
                self.cube[4][1][2] == self.cube[4][1][1] and
                self.cube[5][1][0] == self.cube[5][1][1])

    def is_front_cross_solved(self, color):
        return (self.cube[2][0][1] == color and
                self.cube[2][1][0] == color and
                self.cube[2][1][1] == color and
                self.cube[2][1][2] == color and
                self.cube[2][2][1] == color and
                self.cube[0][2][1] == self.cube[0][1][1] and
                self.cube[1][1][2] == self.cube[1][1][1] and
                self.cube[3][1][0] == self.cube[3][1][1] and
                self.cube[5][0][1] == self.cube[5][1][1])

    def is_right_cross_solved(self, color):
        return (self.cube[3][0][1] == color and
                self.cube[3][1][0] == color and
                self.cube[3][1][1] == color and
                self.cube[3][1][2] == color and
                self.cube[3][2][1] == color and
                self.cube[0][1][2] == self.cube[0][1][1] and
                self.cube[2][1][2] == self.cube[2][1][1] and
                self.cube[4][1][0] == self.cube[4][1][1] and
                self.cube[5][1][2] == self.cube[5][1][1])

    def is_back_cross_solved(self, color):
        return (self.cube[4][0][1] == color and
                self.cube[4][1][0] == color and
                self.cube[4][1][1] == color and
                self.cube[4][1][2] == color and
                self.cube[4][2][1] == color and
                self.cube[0][0][1] == self.cube[0][1][1] and
                self.cube[1][1][0] == self.cube[1][1][1] and
                self.cube[3][1][2] == self.cube[3][1][1] and
                self.cube[5][2][1] == self.cube[5][1][1])

    def is_down_cross_solved(self, color):
        return (self.cube[5][0][1] == color and
                self.cube[5][1][0] == color and
                self.cube[5][1][1] == color and
                self.cube[5][1][2] == color and
                self.cube[5][2][1] == color and
                self.cube[1][2][1] == self.cube[1][1][1] and
                self.cube[2][2][1] == self.cube[2][1][1] and
                self.cube[3][2][1] == self.cube[3][1][1] and
                self.cube[4][2][1] == self.cube[4][1][1])

    def is_white_cross_solved(self):
        for i in range(len(self.cube)):
            if self.cube[i][1][1] == 0:
                return self.switch(i, 0)

    def is_orange_cross_solved(self):
        for i in range(len(self.cube)):
            if self.cube[i][1][1] == 1:
                return self.switch(i, 1)

    def is_green_cross_solved(self):
        for i in range(len(self.cube)):
            if self.cube[i][1][1] == 2:
                return self.switch(i, 2)

    def is_red_cross_solved(self):
        for i in range(len(self.cube)):
            if self.cube[i][1][1] == 3:
                return self.switch(i, 3)

    def is_blue_cross_solved(self):
        for i in range(len(self.cube)):
            if self.cube[i][1][1] == 4:
                return self.switch(i, 4)

    def is_yellow_cross_solved(self):
        for i in range(len(self.cube)):
            if self.cube[i][1][1] == 5:
                return self.switch(i, 5)

    def switch(self, i, color):
        if i == 0:
            return self.is_up_cross_solved(color)
        elif i == 1:
            return self.is_left_cross_solved(color)
        elif i == 2:
            return self.is_front_cross_solved(color)
        elif i == 3:
            return self.is_right_cross_solved(color)
        elif i == 4:
            return self.is_back_cross_solved(color)
        elif i == 5:
            return self.is_down_cross_solved(color)

    def y_rotation(self):
        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[1][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[1][i][j] = copy.deepcopy(self.cube[2][i][j])
                self.cube[2][i][j] = copy.deepcopy(self.cube[3][i][j])
                self.cube[3][i][j] = copy.deepcopy(self.cube[4][i][j])
                self.cube[4][i][j] = copy.deepcopy(temp[i][j])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[0][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[0][i][j] = copy.deepcopy(temp[2-j][i])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[5][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[5][i][j] = copy.deepcopy(temp[j][2-i])

    def x_rotation(self):
        temp = [[0]*3 for _ in range(3)]

        temp = copy.deepcopy(self.cube[0])

        self.cube[0] = copy.deepcopy(self.cube[2])
        self.cube[2] = copy.deepcopy(self.cube[5])
        for i in range(3):
            self.cube[5][i] = copy.deepcopy(self.cube[4][2-i][::-1])
        for i in range(3):
            self.cube[4][i] = copy.deepcopy(temp[2-i][::-1])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[1][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[1][i][j] = copy.deepcopy(temp[j][2-i])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[3][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[3][i][j] = copy.deepcopy(temp[2-j][i])

    def z_rotation(self):
        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[0][i][j])

        temp0 = copy.deepcopy(self.cube[1])
        temp1 = copy.deepcopy(self.cube[5])
        temp2 = copy.deepcopy(self.cube[3])
        temp3 = copy.deepcopy(temp)

        for i in range(3):
            for j in range(3):

                self.cube[0][i][j] = temp0[2-j][i]
                self.cube[1][i][j] = temp1[2-j][i]
                self.cube[5][i][j] = temp2[2-j][i]
                self.cube[3][i][j] = temp3[2-j][i]

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[2][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[2][i][j] = copy.deepcopy(temp[2-j][i])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[4][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[4][i][j] = copy.deepcopy(temp[j][2-i])

    def right_turn(self):
        temp = [[0]*3 for _ in range(4)]
        for i in range(3):
            temp[0][i] = copy.deepcopy(self.cube[5][i][2])
            temp[1][i] = copy.deepcopy(self.cube[2][i][2])
            temp[2][i] = copy.deepcopy(self.cube[0][2 - i][2])
            temp[3][i] = copy.deepcopy(self.cube[4][2 - i][0])
        for i in range(3):
            self.cube[2][i][2] = copy.deepcopy(temp[0][i])
            self.cube[0][i][2] = copy.deepcopy(temp[1][i])
            self.cube[4][i][0] = copy.deepcopy(temp[2][i])
            self.cube[5][i][2] = copy.deepcopy(temp[3][i])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[3][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[3][i][j] = copy.deepcopy(temp[2 - j][i])

    def left_turn(self):
        temp = [[0]*3 for _ in range(4)]
        for i in range(3):
            temp[0][i] = copy.deepcopy(self.cube[5][2-i][0])
            temp[1][i] = copy.deepcopy(self.cube[2][i][0])
            temp[2][i] = copy.deepcopy(self.cube[0][i][0])
            temp[3][i] = copy.deepcopy(self.cube[4][2- i][2])
        for i in range(3):
            self.cube[2][i][0] = copy.deepcopy(temp[2][i])
            self.cube[0][i][0] = copy.deepcopy(temp[3][i])
            self.cube[4][i][2] = copy.deepcopy(temp[0][i])
            self.cube[5][i][0] = copy.deepcopy(temp[1][i])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[1][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[1][i][j] = copy.deepcopy(temp[2-j][i])

    def up_turn(self):
        temp = [[0]*3 for _ in range(4)]
        for i in range(3):
            temp[0][i] = copy.deepcopy(self.cube[1][0][i])
            temp[1][i] = copy.deepcopy(self.cube[2][0][i])
            temp[2][i] = copy.deepcopy(self.cube[3][0][i])
            temp[3][i] = copy.deepcopy(self.cube[4][0][i])
        for i in range(3):
            self.cube[1][0][i] = copy.deepcopy(temp[1][i])
            self.cube[2][0][i] = copy.deepcopy(temp[2][i])
            self.cube[3][0][i] = copy.deepcopy(temp[3][i])
            self.cube[4][0][i] = copy.deepcopy(temp[0][i])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[0][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[0][i][j] = copy.deepcopy(temp[2-j][i])

    def down_turn(self):
        temp = [[0]*3 for _ in range(4)]
        for i in range(3):
            temp[0][i] = copy.deepcopy(self.cube[1][2][i])
            temp[1][i] = copy.deepcopy(self.cube[2][2][i])
            temp[2][i] = copy.deepcopy(self.cube[3][2][i])
            temp[3][i] = copy.deepcopy(self.cube[4][2][i])
        for i in range(3):
            self.cube[1][2][i] = copy.deepcopy(temp[3][i])
            self.cube[2][2][i] = copy.deepcopy(temp[0][i])
            self.cube[3][2][i] = copy.deepcopy(temp[1][i])
            self.cube[4][2][i] = copy.deepcopy(temp[2][i])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[5][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[5][i][j] = copy.deepcopy(temp[2-j][i])

    def front_turn(self):
        temp = [[0]*3 for _ in range(4)]
        for i in range(3):
            temp[0][i] = copy.deepcopy(self.cube[1][i][2])
            temp[1][i] = copy.deepcopy(self.cube[0][2][i])
            temp[2][i] = copy.deepcopy(self.cube[3][i][0])
            temp[3][i] = copy.deepcopy(self.cube[5][0][i])
        for i in range(3):
            self.cube[1][i][2] = copy.deepcopy(temp[3][i])
            self.cube[0][2][i] = copy.deepcopy(temp[0][2-i])
            self.cube[3][i][0] = copy.deepcopy(temp[1][i])
            self.cube[5][0][i] = copy.deepcopy(temp[2][2-i])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[2][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[2][i][j] = copy.deepcopy(temp[2-j][i])

    def back_turn(self):
        temp = [[0]*3 for _ in range(4)]
        for i in range(3):
            temp[0][i] = copy.deepcopy(self.cube[1][i][0])
            temp[1][i] = copy.deepcopy(self.cube[0][0][i])
            temp[2][i] = copy.deepcopy(self.cube[3][i][2])
            temp[3][i] = copy.deepcopy(self.cube[5][2][i])
        for i in range(3):
            self.cube[1][i][0] = copy.deepcopy(temp[1][2-i])
            self.cube[0][0][i] = copy.deepcopy(temp[2][i])
            self.cube[3][i][2] = copy.deepcopy(temp[3][2-i])
            self.cube[5][2][i] = copy.deepcopy(temp[0][i])

        temp = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[i][j] = copy.deepcopy(self.cube[4][i][j])
        for i in range(3):
            for j in range(3):
                self.cube[4][i][j] = copy.deepcopy(temp[2-j][i])

    def middle_turn(self):
        self.left_turn()
        self.left_turn()
        self.left_turn()
        self.right_turn()
        self.x_rotation()
        self.x_rotation()
        self.x_rotation()

    def equatorial_turn(self):
        self.up_turn()
        self.down_turn()
        self.down_turn()
        self.down_turn()
        self.y_rotation()
        self.y_rotation()
        self.y_rotation()

    def standing_turn(self):
        self.front_turn()
        self.front_turn()
        self.front_turn()
        self.back_turn()
        self.z_rotation()
        self.z_rotation()
        self.z_rotation()

    def d_small_turn(self):
        self.up_turn()
        self.y_rotation()
        self.y_rotation()
        self.y_rotation()

    def u_small_turn(self):
        self.down_turn()
        self.y_rotation()

    def r_small_turn(self):
        self.x_rotation()
        self.left_turn()

    def l_small_turn(self):
        self.x_rotation()
        self.x_rotation()
        self.x_rotation()
        self.right_turn()

    def f_small_turn(self):
        self.z_rotation()
        self.back_turn()

    def b_small_turn(self):
        self.z_rotation()
        self.z_rotation()
        self.z_rotation()
        self.front_turn()

    def do_moves(self, action):
        self.previousMoves.append(action)
        if(action == "L"):
            self.left_turn()
        elif(action == "L'"):
            self.left_turn()
            self.left_turn()
            self.left_turn()
        elif(action == "L2"):
            self.left_turn()
            self.left_turn()
        elif(action == "R"):
            self.right_turn()
        elif(action == "R'"):
            self.right_turn()
            self.right_turn()
            self.right_turn()
        elif(action == "R2"):
            self.right_turn()
            self.right_turn()
        elif(action == "U"):
            self.up_turn()
        elif(action == "U'"):
            self.up_turn()
            self.up_turn()
            self.up_turn()
        elif(action == "U2"):
            self.up_turn()
            self.up_turn()
        elif(action == "D"):
            self.down_turn()
        elif(action == "D'"):
            self.down_turn()
            self.down_turn()
            self.down_turn()
        elif(action == "D2"):
            self.down_turn()
            self.down_turn()
        elif(action == "F"):
            self.front_turn()
        elif(action == "F'"):
            self.front_turn()
            self.front_turn()
            self.front_turn()
        elif(action == "F2"):
            self.front_turn()
            self.front_turn()
        elif(action == "B"):
            self.back_turn()
        elif(action == "B'"):
            self.back_turn()
            self.back_turn()
            self.back_turn()
        elif(action == "B2"):
            self.back_turn()
            self.back_turn()
        elif(action == "M"):
            self.middle_turn()
        elif(action == "E"):
            self.equatorial_turn()
        elif(action == "S"):
            self.standing_turn()
        elif(action == "M2"):
            self.middle_turn()
            self.middle_turn()
        elif(action == "E2"):
            self.equatorial_turn()
            self.equatorial_turn()
        elif(action == "S2"):
            self.standing_turn()
            self.standing_turn()
        elif(action == "M'"):
            self.middle_turn()
            self.middle_turn()
            self.middle_turn()
        elif(action == "E'"):
            self.equatorial_turn()
            self.equatorial_turn()
            self.equatorial_turn()
        elif(action == "S'"):
            self.standing_turn()
            self.standing_turn()
            self.standing_turn()
        elif(action == "d"):
            self.d_small_turn()
        elif(action == "u"):
            self.u_small_turn()
        elif(action == "r"):
            self.r_small_turn()
        elif(action == "l"):
            self.l_small_turn()
        elif(action == "f"):
            self.f_small_turn()
        elif(action == "b"):
            self.b_small_turn()
        elif(action == "d'"):
            self.d_small_turn()
            self.d_small_turn()
            self.d_small_turn()
        elif(action == "u'"):
            self.u_small_turn()
            self.u_small_turn()
            self.u_small_turn()
        elif(action == "r'"):
            self.r_small_turn()
            self.r_small_turn()
            self.r_small_turn()
        elif(action == "l'"):
            self.l_small_turn()
            self.l_small_turn()
            self.l_small_turn()
        elif(action == "f'"):
            self.f_small_turn()
            self.f_small_turn()
            self.f_small_turn()
        elif(action == "b'"):
            self.b_small_turn()
            self.b_small_turn()
            self.b_small_turn()
        elif(action == "d2"):
            self.d_small_turn()
            self.d_small_turn()
        elif(action == "u2"):
            self.u_small_turn()
            self.u_small_turn()
        elif(action == "r2"):
            self.r_small_turn()
            self.r_small_turn()
        elif(action == "l2"):
            self.l_small_turn()
            self.l_small_turn()
        elif(action == "f2"):
            self.f_small_turn()
            self.f_small_turn()
        elif(action == "b2"):
            self.b_small_turn()
            self.b_small_turn()
        elif(action == "y"):
            self.y_rotation()
        elif(action == "x"):
            self.x_rotation()
        elif(action == "z"):
            self.z_rotation()
        elif(action == "y'"):
            self.y_rotation()
            self.y_rotation()
            self.y_rotation()
        elif(action == "x'"):
            self.x_rotation()
            self.x_rotation()
            self.x_rotation()
        elif(action == "z'"):
            self.z_rotation()
            self.z_rotation()
            self.z_rotation()
        elif(action == "y2"):
            self.y_rotation()
            self.y_rotation()
        elif(action == "x2"):
            self.x_rotation()
            self.x_rotation()
        elif(action == "z2"):
            self.z_rotation()
            self.z_rotation()
        return self

    def do_moves_numerical(self, action):
        self.previousMoves.append(action)
        if(action == 0):  # L move
            self.left_turn()
        elif(action == 1):  # L' move
            self.left_turn()
            self.left_turn()
            self.left_turn()
        elif(action == 2):  # L2 move
            self.left_turn()
            self.left_turn()
        elif(action == 3):  # R move
            self.right_turn()
        elif(action == 4):  # R' move
            self.right_turn()
            self.right_turn()
            self.right_turn()
        elif(action == 5):  # R2 move
            self.right_turn()
            self.right_turn()
        elif(action == 6):  # U move
            self.up_turn()
        elif(action == 7):  # U' move
            self.up_turn()
            self.up_turn()
            self.up_turn()
        elif(action == 8):  # U2 move
            self.up_turn()
            self.up_turn()
        elif(action == 9):  # D move
            self.down_turn()
        elif(action == 10):  # D' move
            self.down_turn()
            self.down_turn()
            self.down_turn()
        elif(action == 11):  # D2 move
            self.down_turn()
            self.down_turn()
        elif(action == 12):  # F move
            self.front_turn()
        elif(action == 13):  # F' move
            self.front_turn()
            self.front_turn()
            self.front_turn()
        elif(action == 14):  # F2 move
            self.front_turn()
            self.front_turn()
        elif(action == 15):  # B move
            self.back_turn()
        elif(action == 16):  # B' move
            self.back_turn()
            self.back_turn()
            self.back_turn()
        elif(action == 17):  # B2 move
            self.back_turn()
            self.back_turn()
        elif(action == 18):  # M move
            self.middle_turn()
        elif(action == 19):  # E move
            self.equatorial_turn()
        elif(action == 20):  # S move
            self.standing_turn()
        elif(action == 21):  # M2 move
            self.middle_turn()
            self.middle_turn()
        elif(action == 22):  # E2 move
            self.equatorial_turn()
            self.equatorial_turn()
        elif(action == 23):  # S2 move
            self.standing_turn()
            self.standing_turn()
        elif(action == 24):  # M' move
            self.middle_turn()
            self.middle_turn()
            self.middle_turn()
        elif(action == 25):  # E' move
            self.equatorial_turn()
            self.equatorial_turn()
            self.equatorial_turn()
        elif(action == 26):  # S' move
            self.standing_turn()
            self.standing_turn()
            self.standing_turn()
        elif(action == 27):  # d move
            self.d_small_turn()
        elif(action == 28):  # u move
            self.u_small_turn()
        elif(action == 29):  # r move
            self.r_small_turn()
        elif(action == 30):  # l move
            self.l_small_turn()
        elif(action == 31):  # f move
            self.f_small_turn()
        elif(action == 32):  # b move
            self.b_small_turn()
        elif(action == 33):  # d' move
            self.d_small_turn()
            self.d_small_turn()
            self.d_small_turn()
        elif(action == 34):  # u' move
            self.u_small_turn()
            self.u_small_turn()
            self.u_small_turn()
        elif(action == 35):  # r' move
            self.r_small_turn()
            self.r_small_turn()
            self.r_small_turn()
        elif(action == 36):  # l' move
            self.l_small_turn()
            self.l_small_turn()
            self.l_small_turn()
        elif(action == 37):  # f' move
            self.f_small_turn()
            self.f_small_turn()
            self.f_small_turn()
        elif(action == 38):  # b' move
            self.b_small_turn()
            self.b_small_turn()
            self.b_small_turn()
        elif(action == 39):  # d2 move
            self.d_small_turn()
            self.d_small_turn()
        elif(action == 40):  # u2 move
            self.u_small_turn()
            self.u_small_turn()
        elif(action == 41):  # r2 move
            self.r_small_turn()
            self.r_small_turn()
        elif(action == 42):  # l2 move
            self.l_small_turn()
            self.l_small_turn()
        elif(action == 43):  # f2 move
            self.f_small_turn()
            self.f_small_turn()
        elif(action == 44):  # b2 move
            self.b_small_turn()
            self.b_small_turn()
        elif(action == 45):  # y move
            self.y_rotation()
        elif(action == 46):  # x move
            self.x_rotation()
        elif(action == 47):  # z move
            self.z_rotation()
        elif(action == 48):  # y' move
            self.y_rotation()
            self.y_rotation()
            self.y_rotation()
        elif(action == 49):  # x' move
            self.x_rotation()
            self.x_rotation()
            self.x_rotation()
        elif(action == 50):  # z' move
            self.z_rotation()
            self.z_rotation()
            self.z_rotation()
        elif(action == 51):  # y2 move
            self.y_rotation()
            self.y_rotation()
        elif(action == 52):  # x2 move
            self.x_rotation()
            self.x_rotation()
        elif(action == 53):  # z2 move
            self.z_rotation()
            self.z_rotation()
        return self

    def do_algorithm(self, algorithm):
        algorithmArr  = algorithm.split(" ")
        for action in algorithmArr:
            self.do_moves(action)
        return self

    def do_alternative_moves(self, action):
        self.previousMoves.append(action)
        if(action == "L'"):
            self.left_turn()
        elif(action == "L"):
            self.left_turn()
            self.left_turn()
            self.left_turn()
        elif(action == "L2"):
            self.left_turn()
            self.left_turn()
        elif(action == "R'"):
            self.right_turn()
        elif(action == "R"):
            self.right_turn()
            self.right_turn()
            self.right_turn()
        elif(action == "R2"):
            self.right_turn()
            self.right_turn()
        elif(action == "U'"):
            self.up_turn()
        elif(action == "U"):
            self.up_turn()
            self.up_turn()
            self.up_turn()
        elif(action == "U2"):
            self.up_turn()
            self.up_turn()
        elif(action == "D'"):
            self.down_turn()
        elif(action == "D"):
            self.down_turn()
            self.down_turn()
            self.down_turn()
        elif(action == "D2"):
            self.down_turn()
            self.down_turn()
        elif(action == "F'"):
            self.front_turn()
        elif(action == "F"):
            self.front_turn()
            self.front_turn()
            self.front_turn()
        elif(action == "F2"):
            self.front_turn()
            self.front_turn()
        elif(action == "B'"):
            self.back_turn()
        elif(action == "B"):
            self.back_turn()
            self.back_turn()
            self.back_turn()
        elif(action == "B2"):
            self.back_turn()
            self.back_turn()
        elif(action == "M'"):
            self.middle_turn()
        elif(action == "E'"):
            self.equatorial_turn()
        elif(action == "S'"):
            self.standing_turn()
        elif(action == "M2"):
            self.middle_turn()
            self.middle_turn()
        elif(action == "E2"):
            self.equatorial_turn()
            self.equatorial_turn()
        elif(action == "S2"):
            self.standing_turn()
            self.standing_turn()
        elif(action == "M"):
            self.middle_turn()
            self.middle_turn()
            self.middle_turn()
        elif(action == "E"):
            self.equatorial_turn()
            self.equatorial_turn()
            self.equatorial_turn()
        elif(action == "S"):
            self.standing_turn()
            self.standing_turn()
            self.standing_turn()
        elif(action == "d'"):
            self.d_small_turn()
        elif(action == "u'"):
            self.u_small_turn()
        elif(action == "r'"):
            self.r_small_turn()
        elif(action == "l'"):
            self.l_small_turn()
        elif(action == "f'"):
            self.f_small_turn()
        elif(action == "b'"):
            self.b_small_turn()
        elif(action == "d"):
            self.d_small_turn()
            self.d_small_turn()
            self.d_small_turn()
        elif(action == "u"):
            self.u_small_turn()
            self.u_small_turn()
            self.u_small_turn()
        elif(action == "r"):
            self.r_small_turn()
            self.r_small_turn()
            self.r_small_turn()
        elif(action == "l"):
            self.l_small_turn()
            self.l_small_turn()
            self.l_small_turn()
        elif(action == "f"):
            self.f_small_turn()
            self.f_small_turn()
            self.f_small_turn()
        elif(action == "b"):
            self.b_small_turn()
            self.b_small_turn()
            self.b_small_turn()
        elif(action == "d2"):
            self.d_small_turn()
            self.d_small_turn()
        elif(action == "u2"):
            self.u_small_turn()
            self.u_small_turn()
        elif(action == "r2"):
            self.r_small_turn()
            self.r_small_turn()
        elif(action == "l2"):
            self.l_small_turn()
            self.l_small_turn()
        elif(action == "f2"):
            self.f_small_turn()
            self.f_small_turn()
        elif(action == "b2"):
            self.b_small_turn()
            self.b_small_turn()
        elif(action == "y'"):
            self.y_rotation()
        elif(action == "x'"):
            self.x_rotation()
        elif(action == "z'"):
            self.z_rotation()
        elif(action == "y"):
            self.y_rotation()
            self.y_rotation()
            self.y_rotation()
        elif(action == "x"):
            self.x_rotation()
            self.x_rotation()
            self.x_rotation()
        elif(action == "z"):
            self.z_rotation()
            self.z_rotation()
            self.z_rotation()
        elif(action == "y2"):
            self.y_rotation()
            self.y_rotation()
        elif(action == "x2"):
            self.x_rotation()
            self.x_rotation()
        elif(action == "z2"):
            self.z_rotation()
            self.z_rotation()

        return self

    def cateogrize(self):
        saveCube = [0,0,0,0]
        for face in range(len(self.cube)):
            for row in range(len(self.cube[face])):
                for i in range(len(self.cube[face][row])):
                    if 0 == self.cube[face][row][i]:
                        if face == 0:
                            if row == 0:
                                saveCube[self.cube[4][0][1] - 1] = 11
                            if row == 1 and i == 0:
                                saveCube[self.cube[1][0][1] - 1] = 10
                            if row == 1 and i == 2:
                                saveCube[self.cube[3][0][1] - 1] = 12
                            if row == 2:
                                saveCube[self.cube[2][0][1] - 1] = 13
                        if face == 1:
                            if row == 0:
                                saveCube[self.cube[0][1][0] - 1] = 21
                            if row == 1 and i == 0:
                                saveCube[self.cube[4][1][2] - 1] = 310
                            if row == 1 and i == 2:
                                saveCube[self.cube[2][1][0] - 1] = 312
                            if row == 2:
                                saveCube[self.cube[5][1][0] - 1] = 41
                        if face == 2:
                            if row == 0:
                                saveCube[self.cube[0][2][1] - 1] = 22
                            if row == 1 and i == 0:
                                saveCube[self.cube[1][1][2] - 1] = 320
                            if row == 1 and i == 2:
                                saveCube[self.cube[3][1][0] - 1] = 322
                            if row == 2:
                                saveCube[self.cube[5][0][1] - 1] = 42
                        if face == 3:
                            if row == 0:
                                saveCube[self.cube[0][1][2] - 1] = 23
                            if row == 1 and i == 0:
                                saveCube[self.cube[2][1][2] - 1] = 330
                            if row == 1 and i == 2:
                                saveCube[self.cube[4][1][0] - 1] = 332
                            if row == 2:
                                saveCube[self.cube[5][1][2] - 1] = 43
                        if face == 4:
                            if row == 0:
                                saveCube[self.cube[0][0][1] - 1] = 24
                            if row == 1 and i == 0:
                                saveCube[self.cube[3][1][2] - 1] = 340
                            if row == 1 and i == 2:
                                saveCube[self.cube[1][1][0] - 1] = 342
                            if row == 2:
                                saveCube[self.cube[5][2][1] - 1] = 44
                        if face == 5:
                            if row == 0:
                                saveCube[self.cube[2][2][1] - 1] = 51
                            if row == 1 and i == 0:
                                saveCube[self.cube[1][2][1] - 1] = 50
                            if row == 1 and i == 2:
                                saveCube[self.cube[3][2][1] - 1] = 52
                            if row == 2:
                                saveCube[self.cube[4][2][1] - 1] = 53
        self.cateogry = copy.deepcopy(saveCube)

    def put_corners_in_array(self):
        corners_array_array = []
        for face in range(len(self.cube)):
            corners_array = []
            for row in range(len(self.cube[face])):
                for col in range(len(self.cube[face][row])):
                    if (row == 0 or row == 2) and (col == 0 or col == 2):
                        corners_array.append(self.cube[face][row][col])
            corners_array_array.append(corners_array)
        self.corners = corners_array_array

    def get_corner(self, which):
        cornerTuple = [self.corners[self.CORNERTEMPLATE[which][0][0]][self.CORNERTEMPLATE[which][0][1]], self.corners[self.CORNERTEMPLATE[which][1][0]][self.CORNERTEMPLATE[which][1][1]], self.corners[self.CORNERTEMPLATE[which][2][0]][self.CORNERTEMPLATE[which][2][1]]]
        return cornerTuple

    def put_edges_in_array(self):
        edges_array_array = []
        for face in range(len(self.cube)):
            edges_array = []
            for row in range(len(self.cube[face])):
                for col in range(len(self.cube[face][row])):
                    if (row == 0 or row == 2) and col == 1:
                        edges_array.append(self.cube[face][row][col])
                    if row == 1 and (col == 0 or col == 2):
                        edges_array.append(self.cube[face][row][col])
            edges_array_array.append(edges_array)
        self.edges = edges_array_array

    def get_edge(self, which):
        edgeTuple = [self.edges[self.EDGETEMPLATE[which][0][0]][self.EDGETEMPLATE[which][0][1]], self.edges[self.EDGETEMPLATE[which][1][0]][self.EDGETEMPLATE[which][1][1]]]
        return edgeTuple

    def get_pair(self, which):
        self.put_corners_in_array()
        self.put_edges_in_array()
        pairTuple = [self.get_corner(self.PAIRTEMPLATE[which][0]), self.get_edge(self.PAIRTEMPLATE[which][1])]
        return pairTuple

    def get_inserted_pairs(self):
        self.put_corners_in_array()
        self.put_edges_in_array()
        correctlyInsertedPairs = []
        for i in range(24):
            if(self.is_pair_paired(i)):
                pair = self.get_pair(i)
                firstFaceToCheck = self.cube[self.CORNERTEMPLATE[self.PAIRTEMPLATE[i][0]][self.CORRECTPAIRTEMPLATE[i][0]][0]][1][1]
                secondFaceToCheck = self.cube[self.CORNERTEMPLATE[self.PAIRTEMPLATE[i][0]][self.CORRECTPAIRTEMPLATE[i][1]][0]][1][1]

                firstColorOfPair = pair[1][0]
                secondColorOfPair = pair[1][1]

                if((firstFaceToCheck == firstColorOfPair or secondFaceToCheck == firstColorOfPair) and (firstFaceToCheck == secondColorOfPair or secondFaceToCheck == secondColorOfPair)):
                    # print (firstFaceToCheck, secondFaceToCheck)
                    # print (pair[1][0], pair[1][1])
                    correctlyInsertedPairs.append(i)
        return correctlyInsertedPairs

    def is_pair_paired(self, which):
        if(self.get_pair(which)[0][self.CORRECTPAIRTEMPLATE[which][0]] == self.get_pair(which)[1][0] and self.get_pair(which)[0][self.CORRECTPAIRTEMPLATE[which][1]] == self.get_pair(which)[1][1]):
            return True
        return False

    def get_white_inserted_pairs(self):
        self.put_corners_in_array()
        self.put_edges_in_array()
        correctlyInsertedPairs = self.get_inserted_pairs()
        whiteInsertedPairs = []
        for i in correctlyInsertedPairs:
            if(0 in self.get_pair(i)[0] and 0 not in self.get_pair(i)[1]):
                whiteInsertedPairs.append(i)

        return whiteInsertedPairs