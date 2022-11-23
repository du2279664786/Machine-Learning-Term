from itertools import combinations

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()  # 加载数据
y = iris.target  # 标签，有决定意义的标签，来自业务（老天爷）
feat_names = iris.feature_names  # 坐标轴的标记

feats_codes = list(combinations(range(4), 2))  # 组合遍历，python中常用的工具 # 还有一个常用的是Counter

plt.figure(figsize=(15, 12))  # 图的尺寸

pos = 1  # 位置计数器

for feats_code in feats_codes:
    X = iris.data[:, feats_code]  # 为方便画图，仅采用数据的其中两个特征
    ax = plt.subplot(230 + pos)  # 几行，几列，第几个，先按行数
    ax.scatter(X[:, 0], X[:, 1], c=y)  # x, y, 颜色，系统有基本的选择机制，不用写得太细
    ax.set_xlabel(feat_names[feats_code[0]])
    ax.set_ylabel(feat_names[feats_code[1]])
    ax.set_title(feats_code)
    pos += 1


"""
需要关注的点
1、特征和标签的关系：结果和标签是有联系的。
2、二维特征可视化，可视化的常用技巧。
3、底层的数据是numpy
"""
