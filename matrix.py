import numpy as np
from scipy.linalg import null_space

def main():
    # m = Matrix(size=get_size())
    # set_coeff_matrix(m)
    # print(m.coefficient_matrix)
    # set_b_vector(m)
    # print(m.b_vector)
    # print("x vector")
    # print(m.solve())
    # print("determinant")
    # print(m.determinant())
    # print("Null space")
    # print(m.null_space())
    s = get_size()
    m = get_matrix(s[0], s[1])
    m = Matrix.matrix_from_list(m)
    print(m.coefficient_matrix)

class Matrix():
    def __init__(self, size=(1,1), b_vector=None, coeff_matrix=None):
        self.size = size
        self.b_vector = b_vector

        if isinstance(coeff_matrix, np.ndarray):
            self.coefficient_matrix = coeff_matrix
        else:
            self.coefficient_matrix = np.zeros(self.size)
    
    def solve(self):
        if isinstance(self.b_vector, np.ndarray) and round(self.determinant()) is not 0:
            return np.linalg.solve(self.coefficient_matrix, self.b_vector)
        return None
    
    def determinant(self):
        return np.linalg.det(self.coefficient_matrix)
    
    def null_space(self):
        return null_space(self.coefficient_matrix)
    
    @classmethod
    def matrix_from_list(cls, l):
        return cls(size=(len(l), len(l[0])), coeff_matrix=np.array(l))

def set_coeff_matrix(m):
    m.coefficient_matrix = get_matrix(m.size[0], m.size[1])

def set_b_vector(m):
    m.b_vector = get_solution_vector(m.coefficient_matrix.shape[0])

def get_size():
    y = int(input("Number of equations: "))
    x = int(input("Number of variables: "))
    return (x, y)

def get_matrix(equations, variables):
    m = []
    for i in range(equations):
        e = []
        for i in range(variables):
            e.append(int(input("coefficient? ")))
        m.append(e)

    return np.array(m)

def get_solution_vector(num_equations):
    s = []
    for i in range(num_equations):
        s.append(int(input("Solution: ")))
    return np.array(s)

def solve_matrix(m, s):
    return np.linalg.solve(m, s)

if __name__ == "__main__":
    main()