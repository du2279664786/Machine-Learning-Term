# 输入一个数组
# 输出最接近平均值的数

data = [1, 3, 7, 15, 24, 18, 2, 9, 16]

# 方法一，直观的解法(打擂台)
mean_data = sum(data) / len(data)
diff = float('inf')
min_x = None

for ii in data:
    diff_ii = abs(ii - mean_data)
    if diff_ii < diff:
        diff = diff_ii
        min_x = ii

if min_x is not None:
    print('计算有效，结果是：', min_x)


# min(f(x))
# argmin(f(x))
# 方法二，argmin
# x1 = argmin(f(x)) # 自变量为x
# f(x1) = ?

import numpy as np
data2 = np.array(data)
min_x = data2[np.abs(data2 - data2.mean()).argmin()]


# 关于argsort  理解这两句话的业务意义
min_x2 = data2[np.abs(data2 - data2.mean()).argsort()]
data2[data2.argsort()]


# 深入理解1
# 直观解法：比较的是diff，要的是值：
# argmin: arg的是diff，返回的是的值

# 深入理解2
# 体会 index argmin idx 的区别

import numpy as np
data = [1, 3, 7, 15, 24, 18, 2, 9, 16]
print(data[list(np.abs(data - np.mean(data))).index(min(np.abs(data - np.mean(data))))])


import pandas as pd
data = [1, 3, 7, 15, 24, 18, 2, 9, 16]
data = pd.Series(data)
d1 = abs(data-data.mean())
dd = d1.idxmin()
print(data[dd])


import this
