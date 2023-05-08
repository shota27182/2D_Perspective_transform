import cv2
import matplotlib.pyplot as plt

def on_click(event):
    # マウスクリックイベントで呼び出される関数
    if event.xdata and event.ydata:
        x = int(event.xdata)
        y = int(event.ydata)
        print(f'Image coordinates: x={x}, y={y}')

# 画像を読み込む
image = cv2.imread('input_image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCVはBGRで読み込むため、RGBに変換

# 画像を表示
fig, ax = plt.subplots()
ax.imshow(image)

# マウスクリックイベントに応答するように設定
fig.canvas.mpl_connect('button_press_event', on_click)

# グラフを表示
plt.show()