import numpy as np

from Lorenz import LorenzAttractor
from method.CD import CD
from method.Eiler import *
from method.RungeKutta2 import RungeKutta2
from method.RungeKutta4 import RungeKutta4
from models import TypeOfParam
from painters import Painter, DiffractionDiagram, D2Difraction


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


def getDiffraction(metod, time, h, X, a, attractor):
    print(metod.getName()+" старт")
    DiffractionDiagram.plot(metod, X, a, h, time, 0, 25, 25 / 1000, TypeOfParam.param.a1, "a1"
                            , 60 / h, attractor)
    print("параметр 1")
    DiffractionDiagram.plot(metod, X, a, h, time, 20, 350, 330 / 1000, TypeOfParam.param.a2, "a2"
                            , 60 / h, attractor)
    print("параметр 2")
    DiffractionDiagram.plot(metod, X, a, h, time, 0, 4.5, 4.5 / 1000, TypeOfParam.param.a3, "a3"
                            , 60 / h, attractor)
    print("параметр 3")
    DiffractionDiagram.plot(metod, X, a, h, time, 0.0001, 0.024, 0.0241/250, TypeOfParam.param.h, "h"
                            , 60 / h, attractor)
    print("шаг")
    print(metod.getName()+" готов")


if __name__ == "__main__":
    # attractor = RosslerAttractor()
    # a = [0, 0.2, 0.2, 5.7]

    attractor = LorenzAttractor()
    a = [1, 10, 28, 8 / 3]

    X = [0.1, 0.1, 0.1]
    time = 100
    h = 0.0001

    # solve(Eiler(), time, h, X, a, attractor, "Метод эйлера")
    # solve(RungeKutta2(), time, h, X, a, attractor, "Неявный метод Рунге — Кутты второго порядка")
    # solve(CD(), time, h, X, a, attractor, "Метод Бутусова")
    # solve(RungeKutta4(), time, h, X, a, attractor, "Классический метод Рунге — Кутты четвёртого порядка")
    # time = 10
    # getDeviation(Eiler(), time, h, X, a, attractor, "Погрешность метода эйлера")
    # getDeviation(RungeKutta2(), time, h, X, a, attractor, "Погрешность неявного метода Рунге — Кутты второго порядка")
    # getDeviation(CD(), time, h, X, a, attractor, "Погрешность метода Бутусова")
    # getDiffraction(Eiler(), time, h, X, a, attractor)
    # getDiffraction(RungeKutta2(), time, h, X, a, attractor)
    # getDiffraction(CD(), time, h, X, a, attractor)
    # getDiffraction(RungeKutta4(), time, h, X, a, attractor)
    D2Difraction.plot(Eiler(), X, a, h, time, 0, 15, 15 / 100, TypeOfParam.param.a3, "a3"
                            , 60 / h, attractor)
    D2Difraction.plot(RungeKutta2(), X, a, h, time, 0, 15, 15 / 100, TypeOfParam.param.a3, "a3"
                            , 60 / h, attractor)
    D2Difraction.plot(CD(), X, a, h, time, 0, 15, 15 / 100, TypeOfParam.param.a3, "a3"
                            , 60 / h, attractor)
    D2Difraction.plot(RungeKutta4(), X, a, h, time, 0, 15, 15 / 100, TypeOfParam.param.a3, "a3"
                            , 60 / h, attractor)
# #
