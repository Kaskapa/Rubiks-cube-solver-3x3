# Rubik's Cube CFOP Solver

A high-performance Rubik's Cube solver implemented in Python, utilizing the **CFOP method**. This project uses **Iterative Deepening A\* (IDA\*)** search algorithms guided by pre-computed pattern databases (heuristics) to find efficient solutions for each stage of the solve.

## Performance
The solver is optimized for speed, particularly when using JIT compilers:
* **F2L Solver (Standard Python):** ~32 seconds average.
* **F2L Solver (PyPy):** ~26 seconds average.

### Solver Logic Note
While IDA* is used for most stages, the `fullSolver.py` uses **Cheap Solvers** (table-based lookups) for the **OLL** and **PLL** steps. This is because the full IDA* search for these final layers can be computationally expensive and slow for a real-time "full solve" experience.

## Project Structure

### 1. Core Solvers (IDA\* & Table-based)
* `fullSolver.py`: The central orchestrator that manages the transition between Cross, F2L, OLL, and PLL.
* `idaStarCross.py`: IDA* implementation for solving the Cross.
* `idaStarF2L.py`: Advanced search for the First Two Layers.
* `idaStarOLL.py` & `idaStarPLL.py`: IDA* search for Last Layer orientation and permutation.
* `cheapOLLSolver.py` & `cheapPLLSolver.py`: Fast, table-based lookup solvers for standard OLL/PLL cases[cite: 1].

### 2. Heuristics & Data
* `tables.py`: Manages the loading of `.pickle` heuristic files into memory for the search algorithms.

### 3. API & Web
* `main.py`: A Flask-based REST API that accepts a scramble string and returns a full solution.
* `index.html`: A front-end example for interacting with the solver API.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kaskapa/Rubiks-cube-solver-3x3.git
   cd Rubiks-cube-solver-3x3
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```



## Usage

### Running the API
Start the Flask server:

```bash
python main.py
```

### Solving a Cube
Send a GET request to the local server:

```text
http://127.0.0.1:5000/solve/<your_scramble_here>
```

###  Testing Individual Stages
Each part of the CFOP method can be tested independently. If you want to run a full search for a specific stage (even OLL and PLL), you can execute the corresponding script directly:

```bash
python idaStarCross.py
python idaStarF2L.py
python idaStarOLL.py
python idaStarPLL.py
```

## Technical Details

* **Pruning:** The IDA* implementation uses move pruning to ignore redundant sequences (e.g., `U U'` or `R2 R2`).
* **Transposition Tables:** Optimized state tracking to avoid re-evaluating previously visited cube orientations.
* **Coordinates:** Built upon the `twophase` library for accurate cubie-level representation.
