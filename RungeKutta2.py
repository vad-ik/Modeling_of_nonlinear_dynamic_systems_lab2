class RungeKutta2:
    def getAns(self, time, h, X, a, func):
        steps = int(time / h) + 1
        X1 = [[0.0] * 3 for _ in range(steps)]  # 3 столбца (x, y, z)

        X1[0] = X.copy()
        Xtemp=[0.0,0.0,0.0]

        for i in range(steps - 1):
            dx = func.getdX(X1[i], a)
            dy = func.getdY(X1[i], a)
            dz = func.getdZ(X1[i], a)

            Xtemp[0] = X1[i][0] + 0.5 * h * dx
            Xtemp[1] = X1[i][1] + 0.5 * h * dy
            Xtemp[2] = X1[i][2] + 0.5 * h * dz

            dx = func.getdX(Xtemp, a)
            dy = func.getdY(Xtemp, a)
            dz = func.getdZ(Xtemp, a)

            X1[i + 1][0] = X1[i][0] + h * dx
            X1[i + 1][1] = X1[i][1] + h * dy
            X1[i + 1][2] = X1[i][2] + h * dz

        X_coords, Y_coords, Z_coords = zip(*X1)

        return [list(X_coords), list(Y_coords), list(Z_coords)]
