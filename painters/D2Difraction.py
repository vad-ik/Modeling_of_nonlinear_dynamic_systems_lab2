import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.cluster import DBSCAN

from painters import DiffractionDiagram


def cluster_peaks(peaks, eps=0.1, min_samples=1):
    """
    Кластеризация пиков с помощью DBSCAN

    Parameters:
    peaks - список пиков
    eps - максимальное расстояние между пиками в одном кластере
    min_samples - минимальное количество пиков в кластере
    """
    peaks = np.array(peaks).reshape(-1, 1)

    # DBSCAN кластеризация
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(peaks)

    # Вычисляем центры кластеров (усредненные значения пиков)
    unique_labels = set(labels)
    clusters = []

    for label in unique_labels:
        if label == -1:  # Шумовые точки
            continue
        cluster_points = peaks[labels == label].flatten()
        cluster_center = np.mean(cluster_points)
        clusters.append(cluster_center)

    return np.array(clusters)


def plot(method, X, a, h, time, start, finish, step, type, name, skip, func):
    data = []
    debag = 0
    maxA2=600

    for i in np.arange(0, maxA2, maxA2/ 100):  # перебор a2
        print(debag)
        debag = debag + 1

        a = a.copy()
        a[2] = i
        peaks = DiffractionDiagram.getData(method, X, a, h, time, start, finish, step, type, skip, func)

        result = [
            [len(cluster_peaks(peak)) for peak in row]  # row = список из 3 списков с k элементами
            for row in peaks  # data = список длины n
        ]

        data.append(np.array(result))  # теперь это массив формы [n, 3]

    # Сохранение
    np.save('data.npy', data)
    save(data, method.getName(),  np.arange(start, finish, step),np.arange(0, maxA2, maxA2 / 100))

    print(method.getName()+" готов")
def fromFile(method,start, finish, step):
    data = np.load('data.npy')
    save(data,method.getName(),np.arange(start, finish, step),np.arange(0, 260, 260 / 10))


def save(data, name, a2_values=None, a3_values=None):
    file_path = "C:\\Users\\Dark Cat\\PycharmProjects\\ModNelDC\\out\\2d\\"+name+"\\"
    base_name = "параметр a2 и a3 " + name + " ось "

    data = np.array(data)
    for i in range(3):
        fig, ax = plt.subplots(figsize=(12, 9))

        heatmap_data = data[:, :, i]

        # Настройка внешнего вида
        sns.set_style("whitegrid")
        sns.set_context("talk")  # Увеличиваем размер шрифтов

        # Создаем тепловую карту
        sns.heatmap(heatmap_data,
                    cmap='plasma',  # Красивая цветовая схема
                    ax=ax,
                    cbar_kws={'label': 'Количество кластеров', 'shrink': 0.8},
                    xticklabels=[f"{x:.2f}" for x in a2_values],
                    yticklabels=[f"{y:.2f}" for y in a3_values],
                    linewidths=0.1,  # Тонкие линии между ячейками
                    linecolor='white',  # Цвет линий
                    )

        # Настраиваем подписи
        ax.set_title(f'Распределение по оси {getChar(i)}', fontsize=16, pad=20)
        ax.set_ylabel('Значения параметра a2', fontsize=14)
        ax.set_xlabel('Значения параметра a3', fontsize=14)
        ax.invert_yaxis()

        step_x = 5
        step_y = 5

        ax.set_xticks(range(0, len(a2_values), step_x))
        ax.set_xticklabels([f"{x:.2f}" for x in a2_values[::step_x]], rotation=45)

        ax.set_yticks(range(0, len(a3_values), step_y))
        ax.set_yticklabels([f"{y:.2f}" for y in a3_values[::step_y]], rotation=0)

        # Поворачиваем метки для лучшей читаемости
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

        # Сохраняем с высоким качеством
        full_path = file_path + f"ful_{base_name}{getChar(i)}.png"
        plt.savefig(full_path, dpi=300, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        plt.close()

        print(f"Сохранено: {full_path}")


def getChar(j):
    match j:
        case 0:
            return 'x'
        case 1:
            return 'y'
        case 2:
            return 'z'
    return " "
