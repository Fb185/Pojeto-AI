def main(puzzle):
    csp = create_sudoku_csp(puzzle)  #criar o CSP para usar no ac3 a partir do puzzle input
    for i in range(len(puzzle)):
        text=""
        for j in range(len(puzzle[i])):
            text+=str(puzzle[i][j]) + " "
        print(text)
        
    if AC3(csp):
        print("Solution found:")
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                var = f"V{i},{j}"
                print(next(iter(csp.domains[var])), end=" ")
            print()
    else:
        print("No solution found.")

def create_sudoku_csp(puzzle):

    n = len(puzzle)

    variables = [f"V{i},{j}" for i in range(n) for j in range(n)]
    domains = {var: list(range(1, n + 1)) for var in variables}
    neighbors = {var: set() for var in variables}

    # Set domains for variables that have a value in the puzzle
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == 0:                 
                continue
            var = f"V{i},{j}"
            domains[var] = [puzzle[i][j]]

    # Set neighbors for each variable
    for i in range(n):
        for j in range(n):
            var = f"V{i},{j}"
            # Add variables in the same row and column as neighbors
            for k in range(n):
                if k != j:
                    neighbors[var].add(f"V{i},{k}")
                if k != i:
                    neighbors[var].add(f"V{k},{j}")
            # Add variables in the same 3x3 grid as neighbors
            i_start, j_start = 3 * (i // 3), 3 * (j // 3)
            for di in range(3):
                for dj in range(3):
                    if (i_start + di, j_start + dj) != (i, j):
                        neighbors[var].add(f"V{i_start+ di},{j_start +dj}")
    return CSP(variables, domains, neighbors, puzzle)

def AC3(csp, arcs=None):
    if arcs is None:
        arcs = [(Xi, Xj) for Xi in csp.variables for Xj in csp.neighbors[Xi]]
    # count1=0
    while arcs:
        Xi, Xj = arcs.pop()
        if revise(csp, Xi, Xj):
            if len(csp.domains[Xi]) == 0:
                return False
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    arcs.append((Xk, Xi))
    return True

def revise(csp, Xi, Xj): 
    revised = False
    if(len(csp.domains[Xi]) > 1 and len(csp.domains[Xj]) >1):
        return False

    for x in csp.domains[Xi]:
        if not any( x!=y for y in csp.domains[Xj]):
            csp.domains[Xi].remove(x)
            revised = True
    return revised

class CSP:
    def __init__(self, variables, domains, neighbors, puzzle):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.puzzle = puzzle

if __name__ == "__main__":
    puzzle = [
        [0, 0, 3, 0, 2, 0, 6, 0, 0],
        [9, 0, 0, 3, 0, 5, 0, 0, 1],
        [0, 0, 1, 8, 0, 6, 4, 0, 0],
        [0, 0, 8, 1, 0, 2, 9, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 6, 7, 0, 8, 2, 0, 0],
        [0, 0, 2, 6, 0, 9, 5, 0, 0],
        [8, 0, 0, 2, 0, 3, 0, 0, 9],
        [0, 0, 5, 0, 1, 0, 3, 0, 0]
        ]
    main(puzzle)
