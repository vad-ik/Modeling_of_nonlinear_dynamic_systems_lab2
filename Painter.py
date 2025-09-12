import matplotlib.pyplot as plt
import numpy as np
def draw(X,h,name,mode=False):
    n_points = len(X[0])
    time = np.arange(0, n_points * h, h)  # Правильное время с шагом h

    # Если время получилось длиннее из-за округлений
    if len(time) > n_points:
        time = time[:n_points]

    # Создаем фигуру 2x3
    plt.figure(figsize=(18, 10))

    plt.subplot2grid((2, 3), (0, 0))
    plt.plot(X[0], X[1])  # X vs Y
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.subplot2grid((2, 3), (0, 1))
    plt.plot(X[0], X[2])  # X vs Z
    plt.xlabel('X')
    plt.ylabel('Z')

    plt.subplot2grid((2, 3), (0, 2))
    plt.plot(X[1], X[2])  # Y vs Z
    plt.xlabel('Y')
    plt.ylabel('Z')
    if mode:
        X=X.copy()
        X=np.abs(X)
    plt.subplot2grid((2, 3), (1, 0), colspan=3, rowspan=2)
    if mode:
        plt.semilogy(time, X[0], 'b-', label='X(t)', linewidth=1)
        plt.semilogy(time, X[1], 'r-', label='Y(t)', linewidth=1)
        plt.semilogy(time, X[2], 'g-', label='Z(t)', linewidth=1)
    else:
        plt.plot(time, X[0], 'b-', label='X(t)', linewidth=1)
        plt.plot(time, X[1], 'r-', label='Y(t)', linewidth=1)
        plt.plot(time, X[2], 'g-', label='Z(t)', linewidth=1)
    plt.xlabel('Время')
    plt.ylabel('Значения')
    plt.title('Временные ряды')
    plt.legend()
    plt.grid(True, alpha=0.3)


    plt.suptitle(name)
    plt.tight_layout()
    plt.show()


def draw_3d(X, name):
    """3D визуализация аттрактора"""
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(X[0], X[1], X[2], 'b-', linewidth=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'{name}\n3D траектория')

    plt.show()