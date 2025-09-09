class RosslerAttractor:
    # Rössler attractor
    def getdX(self, X, a):
        return -X[1] - X[2]

    def getdY(self, X, a):
        return X[0] + a[1] * X[1]

    def getdZ(self, X, a):
        return a[2] + X[2] * (X[0] - a[3])