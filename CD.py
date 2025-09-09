class CD:
    def getAns(self, time, h, X, a, func):
        steps = int(time / h) + 1
        X1 = [[0.0] * 3 for _ in range(steps)]

        X1[0] = X.copy()

        for i in range(steps - 1):
            # вообще хз что тут происходит
            i=i

        X_coords, Y_coords, Z_coords = zip(*X1)

        return [list(X_coords), list(Y_coords), list(Z_coords)]