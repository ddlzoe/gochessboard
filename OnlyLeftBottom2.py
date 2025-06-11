import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.widgets import TextBox

chessPieceDic = {}
num = 1
qNum = ""
textbb = None

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
        newQizi, = plt.plot(xInt, yInt, linestyle='solid', color='black', marker='o', markerfacecolor=color, markersize=44, visible=True)
        chessPieceDic[dicKey] = newQizi
    elif event.button == 3:
        print("Right Click.")
        if dicKey in chessPieceDic:
            removeQizi = chessPieceDic.pop(dicKey)
            removeQizi.remove()

    else:
        print("Invalid input")
        return

    print("Show")
    plt.draw()

def on_key(event):
    global num
    global qNum
    global textbb
    print(f'你按下了: {event.key}')
    if event.key == 'c':
        print("clear")
        qNum = ""
        if textbb is None:
            print("Text Box 引用是空的")
        else:
            textbb.remove()
            textbb = None

        while chessPieceDic:
            key, value = chessPieceDic.popitem()
            value.remove()
    if event.key == 'b':
        folder_path = r"D:\go\吃线子"
        filename = str(num) + ".png"
        num = num + 1
        full_path = os.path.join(folder_path, filename)
        plt.savefig(full_path, bbox_inches='tight')
    if event.key.isdigit():
        qNum = qNum + event.key
        if textbb is None:
            textbb = ax.text(x=1.5,  # x坐标（0-1相对坐标或数据坐标）
                    y=0.5,  # y坐标
                    s=qNum,
                    ha='center',  # 水平对齐（left/center/right）
                    va='center',  # 垂直对齐（top/center/bottom）
                    bbox=dict( facecolor='white', lw=0))
        else:
            textbb.set_text(qNum)
    plt.draw()


board_size = 12

fig, ax = plt.subplots(figsize=(10, 10))
plt.locator_params(nbins=19)

for i in range(board_size):
    print("I value: " + str(i))
    xLinewidth = 1
    if i == 0:
        xLinewidth = 2
    if i == 11:
        xLinewidth = 0
    ax.plot((1, board_size), (i + 1, i + 1), color='black', linewidth=xLinewidth)
    ax.plot((i + 1, i + 1), (1, board_size), color='black', linewidth=xLinewidth)

ax.set_xticks(np.arange(1, 20, 1))
ax.set_yticks(np.arange(1, 20, 1))
# 隐藏x轴和y轴的数字
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.plot(4, 4, 'ko-')
# ax.plot(4, 16, 'ko-')
ax.plot(4, 10, 'ko-')
ax.plot(10, 4, 'ko-')
# ax.plot(16, 4, 'ko-')
# ax.plot(16, 10, 'ko-')
# ax.plot(16, 16, 'ko-')
# ax.plot(10, 16, 'ko-')
ax.plot(10, 10, 'ko-')

cid = fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('key_press_event', on_key)

plt.axis('off')
ax.set_axis_off()



plt.show()
plt.draw()