from twophase.cubes import cubiecube
from twophase.pieces import Edge, Corner, Color
import copy
import pickle
import threading

heuristic = {}

def build_heuristic_db(cube, startingMove, max_moves=4):
    global heuristic
    def get_f2l_state(cube):
        edgeArray = []
        edgeOrientaion = []

        for i in range(12):
            if cube.ep[i] == Edge.UB or cube.ep[i] == Edge.UR or cube.ep[i] == Edge.UF or cube.ep[i] == Edge.UL:
                edgeArray.append(cube.ep[i])
                edgeOrientaion.append(cube.eo[i])
            else:
                edgeArray.append(-1)
                edgeOrientaion.append(-1)

        return tuple(edgeArray + edgeOrientaion)

    current_Depth = 1

    cube = actions(startingMove, cube)

    que = [(1, get_f2l_state(cube), [])]
    while True:
        if not que:
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
            new_cube = copy.deepcopy(current_cube)
            new_cube = actions(action, new_cube)
            new_actions = previous_actions + [action]

            f2l_state = get_f2l_state(new_cube)

            if f2l_state == previous_state:
                continue

            if f2l_state not in heuristic or heuristic[f2l_state] > depth+1:
                # print(f"New state: {f2l_state}, depth: {depth+1}")
                heuristic[f2l_state] = depth+1

            if f2l_state in heuristic and heuristic[f2l_state] < depth:
                continue

            que.append((depth + 1, f2l_state, new_actions))

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

t1 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 0])
t2 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 1])
t3 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 2])
t4 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 3])
t5 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 4])
t6 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 5])
t7 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 6])
t8 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 7])
t9 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 8])
t10 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 9])
t11 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 10])
t12 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 11])
t13 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 12])
t14 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 13])
t15 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 14])
t16 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 15])
t17 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 16])
t18 = threading.Thread(target=build_heuristic_db, args=[cubiecube.CubieCube(), 17])

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()


t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()
t13.join()
t14.join()
t15.join()
t16.join()
t17.join()
t18.join()

print(f"Heuristic size: {len(heuristic)}")

# Dump the heuristics dictionary into a pickle file
with open('heuristicsEdgeCross.pickle', 'wb') as file:
    pickle.dump(heuristic, file)

# Load the heuristics dictionary from the pickle file
with open('heuristicsEdgeCross.pickle', 'rb') as file:
    heuristics = pickle.load(file)

print(f"Heuristic size: {len(heuristics)}")