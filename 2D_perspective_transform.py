import cv2
import numpy as np

# 画像を読み込む
input_image = cv2.imread('input_image.png')

# 入力画像の4つの角の座標を指定する (これらは、実際の画像に基づいて手動で選択するか、自動検出アルゴリズムを使用する必要があります)
input_pts = np.float32([[657, 521], [3199, 543], [96, 2256], [3756, 2239]])

# 出力画像の座標を指定する
output_pts = np.float32([[0, 0], [540, 0], [0, 270], [540, 270]])

# 透視変換行列を計算する
matrix = cv2.getPerspectiveTransform(input_pts, output_pts)

# 透視変換を適用する
output_image = cv2.warpPerspective(input_image, matrix, (540, 270))

# 出力画像を保存する
cv2.imwrite('output_image.jpg', output_image)