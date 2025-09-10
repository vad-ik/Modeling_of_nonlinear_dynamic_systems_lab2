import Painter
import numpy as np

from Eiler import *
from RosslerAttractor import RosslerAttractor
from RungeKutta2 import RungeKutta2
from RungeKutta4 import RungeKutta4


def solve(metod, time, h, X, a, rossler, name):
    X1 = metod.getAns(time, h, X, a, rossler)
    Painter.draw(X1, h, name)
    Painter.draw_3d(X1, name)


def getDeviation(metod, time, h, X, a, rossler, name):
    X1 = metod.getAns(time, h, X, a, rossler)
    X2 = RungeKutta4().getAns(time, h, X, a, rossler)
    X1_np = np.array(X1)
    X2_np = np.array(X2)

    # Разница между массивами
    difference = X2_np - X1_np
    Painter.draw(difference, h, name, True)
    Painter.draw_3d(difference, name)


if __name__ == "__main__":
    rossler = RosslerAttractor()  # Создаем экземпляр класса
    X = [0.1, 0.1, 0.1]
    a = [0, 0.2, 0.2, 5.7]
    time = 100
    h = 0.0001

    solve(Eiler(), time, h, X, a, rossler, "Метод эйлера")
    solve(RungeKutta2(), time, h, X, a, rossler, "Неявный метод Рунге — Кутты второго порядка")
    solve(RungeKutta4(), time, h, X, a, rossler, "Классический метод Рунге — Кутты четвёртого порядка")
    getDeviation(RungeKutta2(), time, h, X, a, rossler, "Неявный метод Рунге — Кутты второго порядка")
    getDeviation(Eiler(), time, h, X, a, rossler, "Метод эйлера")
#
