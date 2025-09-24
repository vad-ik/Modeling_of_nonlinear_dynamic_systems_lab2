class RungeKutta4:
    def getAns(self, time, h, X, a, func):
        steps = int(time / h) + 1
        X1 = [[0.0] * 3 for _ in range(steps)]

        X1[0] = X.copy()

        for i in range(steps - 1):
            k1 = [
                func.getdX(X1[i], a),
                func.getdY(X1[i], a),
                func.getdZ(X1[i], a)
            ]

            X_temp_k2 = [
                X1[i][0] + 0.5 * h * k1[0],
                X1[i][1] + 0.5 * h * k1[1],
                X1[i][2] + 0.5 * h * k1[2]
            ]
            k2 = [
                func.getdX(X_temp_k2, a),
                func.getdY(X_temp_k2, a),
                func.getdZ(X_temp_k2, a)
            ]

            X_temp_k3 = [
                X1[i][0] + 0.5 * h * k2[0],
                X1[i][1] + 0.5 * h * k2[1],
                X1[i][2] + 0.5 * h * k2[2]
            ]
            k3 = [
                func.getdX(X_temp_k3, a),
                func.getdY(X_temp_k3, a),
                func.getdZ(X_temp_k3, a)
            ]

            X_temp_k4 = [
                X1[i][0] + h * k3[0],
                X1[i][1] + h * k3[1],
                X1[i][2] + h * k3[2]
            ]
            k4 = [
                func.getdX(X_temp_k4, a),
                func.getdY(X_temp_k4, a),
                func.getdZ(X_temp_k4, a)
            ]

            for j in range(3):
                X1[i + 1][j] = X1[i][j] + (h / 6.0) * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j])
        X_coords, Y_coords, Z_coords = zip(*X1)

        return [list(X_coords), list(Y_coords), list(Z_coords)]

    def getName(self):
        return 'RungeKutta4'
