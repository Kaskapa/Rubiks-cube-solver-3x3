from twophase.cubes import cubiecube, facecube
from twophase.pieces import Edge, Corner, Color
import pickle
import threading


def build_heuristic_db(cube, edge, max_moves=4):
    heuristic = {}

    def get_edges(cube):
        ret = facecube.FaceCube()
        for i in range(8):
            for k in range(3):
                ret.f[facecube.corner_facelet[i][(k) % 3]] = Color.L
        for i in range(12):
            j = cube.ep[i]
            ori = cube.eo[i]
            for k in range(2):
                ret.f[facecube.edge_facelet[i][(k + ori) % 2]] = facecube.edge_color[j][k]
        ret.f[31] = Color.L
        return ret.to_string().replace("U", "-").replace("R", "-").replace("F", "-").replace("L", "-").replace("B", "-")

    def get_corners(cube):
        ret = facecube.FaceCube()
        for i in range(8):
            j = cube.cp[i]
            ori = cube.co[i]
            for k in range(3):
                ret.f[facecube.corner_facelet[i][(k + ori) % 3]] = facecube.corner_color[j][k]
        for i in range(12):
            for k in range(2):
                facelet_index = facecube.edge_facelet[i][(k) % 2]
                ret.f[facelet_index] = Color.L
        ret.f[31] = Color.L
        return ret.to_string().replace("U", "-").replace("R", "-").replace("F", "-").replace("L", "-").replace("B", "-")

    current_Depth = 0

    if(edge == True):
        state = get_edges(cube)
    else:
        state = get_corners(cube)

    que = [(0, state, [])]

    while True:
        if len(que) == 0:
            break
        depth, previous_state, previous_actions = que.pop(0)  # Using pop(0) for breadth-first search

        if depth > current_Depth:
            print(f"Current depth: {depth}")
            current_Depth = depth

        current_cube = cubiecube.CubieCube()
        for action in previous_actions:
            current_cube = actions(action, current_cube)

        if depth > max_moves:
            continue

        for action in range(18):
            new_cube = current_cube.__deepcopy__()
            new_cube = actions(action, new_cube)
            new_actions = previous_actions + [action]

            if(edge == True):
                f2l_state = get_edges(new_cube)
            else:
                f2l_state = get_corners(new_cube)

            if f2l_state == previous_state:
                continue

            if f2l_state not in heuristic or heuristic[f2l_state] > depth+1:
                # print(f"New state: {f2l_state}, depth: {depth+1}")
                heuristic[f2l_state] = depth+1

            if f2l_state in heuristic and heuristic[f2l_state] < depth:
                continue

            que.append((depth + 1, f2l_state, new_actions))

    print(f"Heuristic size: {len(heuristic)} {edge}")


    # Dump the heuristics dictionary into a pickle file
    if(edge == True):
        with open(f'heuristicsEdgeOLL.pickle', 'wb') as file:
            pickle.dump(heuristic, file)

        with open(f'heuristicsEdgeOLL.pickle', 'rb') as file:
            heuristics = pickle.load(file)
        print(f"Heuristic size: {len(heuristics)}")
    else:
        with open(f'heuristicsCornerOLL.pickle', 'wb') as file:
            pickle.dump(heuristic, file)

        with open(f'heuristicsCornerOLL.pickle', 'rb') as file:
            heuristics = pickle.load(file)

        print(f"Heuristic size: {len(heuristics)}")

def actions(action, cube):
    if(action == 0):
        cube.move(0)
    elif(action == 1):
        cube.move(1)
    elif(action == 2):
        cube.move(2)
    elif(action == 3):
        cube.move(3)
    elif(action == 4):
        cube.move(4)
    elif(action == 5):
        cube.move(5)
    elif(action == 6):
        cube.move(0)
        cube.move(0)
    elif(action == 7):
        cube.move(1)
        cube.move(1)
    elif(action == 8):
        cube.move(2)
        cube.move(2)
    elif(action == 9):
        cube.move(3)
        cube.move(3)
    elif(action == 10):
        cube.move(4)
        cube.move(4)
    elif(action == 11):
        cube.move(5)
        cube.move(5)
    elif(action == 12):
        cube.move(0)
        cube.move(0)
        cube.move(0)
    elif(action == 13):
        cube.move(1)
        cube.move(1)
        cube.move(1)
    elif(action == 14):
        cube.move(2)
        cube.move(2)
        cube.move(2)
    elif(action == 15):
        cube.move(3)
        cube.move(3)
        cube.move(3)
    elif(action == 16):
        cube.move(4)
        cube.move(4)
        cube.move(4)
    elif(action == 17):
        cube.move(5)
        cube.move(5)
        cube.move(5)

    return cube

t1 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), True])
t2 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), False])
# t3 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), True, edgeThree])
# t4 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), True, edgeFour])
# t5 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), False, cornerOne])
# t6 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), False, cornerTwo])
# t7 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), False, cornerThree])
# t8 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), False, cornerFour])


t1.start()
t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()

t1.join()
t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()