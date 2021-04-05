import numpy as np

def LevSim (firstWord, secondWord):
    fLengthIncr = len(firstWord)+1
    sLengthIncr = len(secondWord)+1
    matrix = np.zeros((fLengthIncr, sLengthIncr), dtype=int)
    for i in range(fLengthIncr):
        matrix[i, 0] = i
    for i in range(1, sLengthIncr):
        matrix[0, i] = i
    for i in range(1, fLengthIncr):
        for j in range(1, sLengthIncr):
            if firstWord[i-1] == secondWord[j-1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i-1, j] + 1, matrix[i, j-1] + 1, matrix[i-1, j-1] + cost)
    return matrix[fLengthIncr-1, sLengthIncr-1]


if __name__ == '__main__':
    print(LevSim("pies", "pies"))
    print(LevSim("granat", "granit"))
    print(LevSim("orczyk", "oracz"))
    print(LevSim("marka", "ariada"))