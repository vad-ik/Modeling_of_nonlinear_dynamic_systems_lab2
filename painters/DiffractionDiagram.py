from datetime import datetime
from multiprocessing import Pool, cpu_count

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from tqdm import tqdm

from models import TypeOfParam


def trim_first_n(X1, n):
    X_coords = X1[0]
    Y_coords = X1[1]
    Z_coords = X1[2]
    n_int = int(n)  # Преобразуем в integer
    return [
        list(X_coords)[n_int:],
        list(Y_coords)[n_int:],
        list(Z_coords)[n_int:]
    ]


def find_peaks_amplitudes(Ft):
    Ft = np.array(Ft)
    t = np.arange(len(Ft))
    peaks, properties = find_peaks(Ft, height=-999)  # height - минимальная высота пика

    peak_amplitudes = Ft[peaks]  # амплитуды пиков

    return peak_amplitudes


def getData(method, X, a, h, time, start, finish, step, type, skip, func):
    data = []
    tasks = []
    for i in np.arange(start, finish, step):
        match type:
            case TypeOfParam.param.h:
                h=i
                # h = start*(1.02216**i) # log шкала
                skip=60 / h
            case TypeOfParam.param.a0:
                a = a.copy()
                a[0] = i
            case TypeOfParam.param.a1:
                a = a.copy()
                a[1] = i
            case TypeOfParam.param.a2:
                a = a.copy()
                a[2] = i
            case TypeOfParam.param.a3:
                a = a.copy()
                a[3] = i
            case TypeOfParam.param.a4:
                a = a.copy()
                a[4] = i
        tasks.append((method, time, h, X, a, func, skip))



    with Pool(processes=cpu_count()-2) as pool:
        # imap для последовательного получения результатов
        data = list(tqdm(
            pool.imap(getSrez, tasks),
            total=len(tasks),
            desc="method: "+method.getName()
        ))
    return data


def getSrez(args):
    method, time, h, X, a, func, skip = args
    x1 = method.getAns(time, h, X, a, func)
    x2 = trim_first_n(x1, skip)
    data = []
    for i in range(3):
        amplitudes = find_peaks_amplitudes(x2[i])
        if len(amplitudes) == 0:
            amplitudes = np.array([x2[i][0]])
        data.append(amplitudes)
    return data


def plot(metod, X, a, h, time, start, finish, step, type, name, skip, func):
    data = getData(metod, X, a, h, time, start, finish, step, type, skip, func)
    drawData(data, start, finish, step, name, metod.getName())


def drawData(data, start, finish, step, type, methodName):
    for j in range(3):
        # Подготовка данных для графика
        x_values = []
        y_values = []
        # x=[]
        # for i in  np.arange(start, finish, step):
        #     x.append( start * (1.02216 ** i)) # лог шкала для h
        x=np.arange(start, finish, step)
        for i, (values, t) in enumerate(zip(data, x)):
            for value in values[j]:
                y_values.append(value)
                x_values.append(t)

        # Построение графика
        plt.figure(figsize=(10, 6))
        plt.scatter(x_values, y_values, color='black', s=0.1, alpha=0.7)
        plt.xlabel('Значения переменной ' + type)
        plt.ylabel('амплитуда по оси ' + getChar(j))
        plt.title('Дифракционная диаграмма ' + methodName)
        # plt.xscale('log', base=1.02216)  # лог шкала для h
        plt.grid(True, alpha=0.3)
        # plt.show()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"C:\\Users\\Dark Cat\\PycharmProjects\\ModNelDC\\out\\{methodName}\\diagram_{getChar(j)}_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()  # Важно закрыть фигуру!


def getChar(j):
    match j:
        case 0:
            return 'x'
        case 1:
            return 'y'
        case 2:
            return 'z'
    return " "
