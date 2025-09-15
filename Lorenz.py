class LorenzAttractor:
    # Lorenz attractor
    def getdX(self, X, a):
        return a[1] * (X[1] - X[0])

    def getdY(self, X, a):
        return X[0] * (a[2] - X[2]) - X[1]

    def getdZ(self, X, a):
        return X[0] * X[1] - a[3] * X[2]
