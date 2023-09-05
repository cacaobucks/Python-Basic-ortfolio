%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

# データ
x = np.array([62, 95, 83, 100, 72, 71, 55, 85, 67, 75])
y = np.array([62, 80, 85, 95, 58, 76, 52, 84, 67, 71])

# 近似直線の式の　a と b が入ったndarray 形式のデータを取得
p = np.polyfit(x, y, 1)

# 一次関数の式のオブジェクトを生成
f = np.poly1d(p)

# 散布図と近似直線を描く
plt.scatter(x, y,  c="b", label = "score")
plt.plot(x, f(x),color="red", label = "lsm")
plt.legend(loc = "upper left")
