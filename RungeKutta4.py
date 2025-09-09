class RungeKutta4:
    def getAns(self, time, h, X, a, func):
        steps = int(time / h) + 1
        X1 = [[0.0] * 3 for _ in range(steps)]  # 3 столбца (x, y, z)

        X1[0] = X.copy()

        for i in range(steps - 1):
            k = [[0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0],
                 [0.0, 0.0, 0.0]]

            for l in range(4):
                Xtemp = X1[i].copy()
                k[l][0] = func.getdX(X1[i], a)
                k[l][1] = func.getdY(X1[i], a)
                k[l][2] = func.getdZ(X1[i], a)

                for j in range(3):
                    Xtemp[j] = Xtemp[j] + 0.5 * h * k[l][j]

            for j in range(3):
                X1[i + 1][j] = X1[i][j] + h / 6 * (k[0][j] + 2 * k[1][j] + 2 * k[2][j] + k[3][j])

        X_coords, Y_coords, Z_coords = zip(*X1)

        return [list(X_coords), list(Y_coords), list(Z_coords)]
