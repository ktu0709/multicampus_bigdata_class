import matplotlib.pyplot as plt
import numpy as np

#<< 그리드를 통해서 각 해상도에 따른 공간 데이터가 어떻게 이산화 되는지를 확인 해보자.  >>
#  정량화 (양자화)  -> 공간의 연속적인 픽셀
def plot_grid(rows, cols, ax):
    for x in range(rows + 1):
        ax.axhline(x, color='black', linewidth=1)
    for y in range(cols + 1):
        ax.axvline(y, color='black', linewidth=1)

resolutions = [(300, 300), (100, 100), (10, 50), (10, 10)]

fig, axes = plt.subplots(1, len(resolutions), figsize=(15, 4))

for ax, (rows, cols) in zip(axes, resolutions):
    plot_grid(rows, cols, ax)
    ax.set_title(f'{rows}x{cols}')

plt.show()
