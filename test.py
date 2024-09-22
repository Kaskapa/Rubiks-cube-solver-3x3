from fullSolver import Solver
import time
import json

def solve(scramble):
    solver = Solver(scramble)
    solutions = solver.solve()
    return solutions

if __name__ == "__main__":
    with open("scrambles.txt", "r") as f:
        scrambles = f.readlines()

    # for i, scramble in enumerate(scrambles):
    scramble = scrambles[0].replace("\n", "")
    startTime = time.time()
    solutions = solve(scramble)
    print("Solved in", time.time() - startTime, "seconds")

    solutionsAsDict = [solution.toDict() for solution in solutions]

    with open(f"solutions/solution{0}.json", "a") as f:
        json.dump(solutionsAsDict, f, indent=4)