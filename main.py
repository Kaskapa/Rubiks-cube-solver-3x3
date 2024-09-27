from flask import Flask, request, jsonify
from flask_cors import CORS
from fullSolver import Solver


app = Flask(__name__)
CORS(app)

@app.route('/solve/<scramble>')
def solve(scramble):
    solver = Solver(scramble)
    solutions = solver.solve()

    return jsonify([solution.toDict() for solution in solutions])

if __name__ == "__main__":
    app.run(debug=True)