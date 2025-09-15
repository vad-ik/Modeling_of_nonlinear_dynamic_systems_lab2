class CD:
    def getAns(self, time, h, X, a, func):
        steps = int(time / h) + 1
        X1 = [[0.0] * 3 for _ in range(steps)]
        X1[0] = X.copy()

        for i in range(steps - 1):
            h1 = h * a[0]
            h2 = h * (1 - a[0])

            tmp0 = X1[i][0] + h1 * func.getdX(X1[i], a)
            tmp1 = X1[i][1] + h1 * func.getdY(X1[i], a)
            tmp2 = X1[i][2] + h1 * func.getdZ(X1[i], a)

            X1[i + 1][2] = (tmp2 + h2 * a[2]) / (1 - h2 * (tmp0 - a[3]))
            X1[i + 1][1] = (tmp1 + h2 * tmp0) / (1 - h2 * a[1])
            X1[i + 1][0] = tmp0 + h2 * (-X1[i + 1][1] - X1[i + 1][2])

        X_coords, Y_coords, Z_coords = zip(*X1)
        return [list(X_coords), list(Y_coords), list(Z_coords)]
