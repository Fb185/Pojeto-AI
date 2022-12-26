def sdk():
    '''puzzle=[
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]'''
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
    csp = create_sudoku_csp(puzzle)
    csp.curr_domains = {var: csp.domains[var].copy() for var in csp.variables}
    print("Given Sudoku:")
    
    for i in range(len(puzzle)):
        txt =""
        for j in range(len(puzzle[i])):
            txt +=  str(puzzle[i][j]) + " " 
        print(txt)
    
    if AC3(csp):
        print("Solution found:")
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                var = f"V{i},{j}"
                print(next(iter(csp.curr_domains[var])), end=" ")
            print()
    else:
        print("No solution found.")

def create_sudoku_csp(puzzle):
    n = len(puzzle)
    variables = [f"V{i},{j}" for i in range(n) for j in range(n)]
    domains = {var: set(range(1, n+1)) for var in variables}
    neighbors = {var: set() for var in variables}
    for i, row in enumerate(puzzle):
        for j, value in enumerate(row):
            if value == 0:
                continue
            var = f"V{i},{j}"
            domains[var] = {value}
    for i in range(n):
        for j in range(n):
            var = f"V{i},{j}"
            for k in range(n):
                if k != j:
                    neighbors[var].add(f"V{i},{k}")
                if k != i:
                    neighbors[var].add(f"V{k},{j}")
            i_start, j_start = 3 * (i // 3), 3 * (j // 3)
            for di in range(3):
                for dj in range(3):
                    if (i_start+di, j_start+dj) != (i, j):
                        neighbors[var].add(f"V{i_start+di},{j_start+dj}")
    return CSP(variables, domains, neighbors, puzzle)

class CSP:
    def __init__(self, variables, domains, neighbors, puzzle):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.puzzle = puzzle
        self.curr_domains = None

    def update_curr_domains(self):
        self.curr_domains = {var: set(self.domains[var]) for var in self.variables}

    def constraints(self, Xi, x, Xj, y):
        i, j = map(int, Xi[1:].split(","))
        if self.puzzle[i][j] != 0:
            return self.puzzle[i][j] == x
        if x == y:
            return False
        return True

def AC3(csp, arcs=None):
    if arcs is None:
        arcs = [(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]]
    while arcs:
        Xi, Xj = arcs.pop()
        if revise(csp, Xi, Xj):
            if not csp.curr_domains[Xi]:
                return False
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    arcs.append((Xk, Xi))
    return True

def revise(csp, Xi, Xj):
    revised = False
    for x in csp.curr_domains[Xi].copy():
        if not any(csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
            csp.curr_domains[Xi].remove(x)
            revised = True
    return revised

if __name__ == "__main__":
    sdk()

