from fullSolver import Solver
import time

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

    with open(f"solutions/solution{0}.txt", "a") as f:
        for solution in solutions:
            f.write(str(solution.getInspection()) + "\n")
            f.write(str(solution.getCross()) + "\n")
            f.write(str(solution.getF2L()) + "\n")
            f.write(str(solution.getPre()) + "\n")
            f.write(str(solution.getOLL()) + "\n")
            f.write(str(solution.getPrePLL()) + "\n")
            f.write(str(solution.getPLL()) + "\n")
            f.write(str(solution.getPost()) + "\n")
            f.write("\n")