import matplotlib.pyplot as plt
import numpy as np

chessPieceDic = {}

def onclick(event):
    global chessPieceDic
    xInt = round(event.xdata)
    yInt = round(event.ydata)
    color = 'black' if event.dblclick else 'white'

    dicKey = str(xInt) + ',' + str(yInt)
    if event.button == 1:
        if dicKey in chessPieceDic:
            removeQizi = chessPieceDic.pop(dicKey)
            removeQizi.remove()
        newQizi, = plt.plot(xInt, yInt, linestyle='solid', color='black', marker='o', markerfacecolor=color, markersize=20, visible=True)
        chessPieceDic[dicKey] = newQizi
    elif event.button == 3:
        print("Right Click.")
        if dicKey in chessPieceDic:
            removeQizi = chessPieceDic.pop(dicKey)
            removeQizi.remove();

    else:
        print("Invalid input")
        return

    print("Show")
    plt.draw()




board_size = 19

fig, ax = plt.subplots(figsize=(10, 10))
plt.locator_params(nbins=19)

for i in range(board_size):
    print("I value: " + str(i))
    xLinewidth = 1
    if i == 0 or i == 18:
        xLinewidth = 2
    ax.plot((1, board_size), (i + 1, i + 1), color='black', linewidth=xLinewidth)
    ax.plot((i + 1, i + 1), (1, board_size), color='black', linewidth=xLinewidth)

ax.set_xticks(np.arange(1, 20, 1))
ax.set_yticks(np.arange(1, 20, 1))
# 隐藏x轴和y轴的数字
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.plot(4, 4, 'ko-')
ax.plot(4, 16, 'ko-')
ax.plot(4, 10, 'ko-')
ax.plot(10, 4, 'ko-')
ax.plot(16, 4, 'ko-')
ax.plot(16, 10, 'ko-')
ax.plot(16, 16, 'ko-')
ax.plot(10, 16, 'ko-')
ax.plot(10, 10, 'ko-')

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.axis('off')

# 方法1.2 - 面向对象风格
ax.set_axis_off()

plt.show()
plt.draw()