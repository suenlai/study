# -*- coding=utf-8 

from pylab import *


def plotCircle(before, M=matrix([[1, 0], [0, 1]])):
    '''before: 变换前的矩阵
    M： 变换矩阵,默认为单位矩阵
    返回变换之后的矩阵
    '''
    eclMat = M * before  # M 变换
    eclX = array(eclMat[0]).reshape(-1)
    eclY = array(eclMat[1]).reshape(-1)
    axis('equal')
    axis([-3, 3, -3, 3])
    grid(True)
    plot(eclX[:25], eclY[:25], 'c', linewidth=3)
    plot(eclX[25:50], eclY[25:50], 'm', linewidth=3)
    plot(eclX[50:75], eclY[50:75], 'y', linewidth=3)
    plot(eclX[75:100], eclY[75:100], 'k', linewidth=3)
    show()
    return eclMat


ang = linspace(0, 2*pi, 100)

x = cos(ang)
y = sin(ang)
cirMat = matrix([x, y]) # 2 × 100 的圆圈矩阵

# 画最开始的图形——圆
plotCircle(cirMat)

# 画变换之后的椭圆
M = matrix([[2, 1], [1, 2]]) # 2 × 2 的变换矩阵
clMat = plotCircle(cirMat, M)

# 将 M 矩阵进行 svd 分解
U, s, V = np.linalg.svd(M, full_matrices=True)
S = np.diag(s)

# SVD 矩阵对圆的变换
plotCircle(cirMat)
Tran1 = plotCircle(cirMat, V)
Tran2 = plotCircle(Tran1, S)
Tran3 = plotCircle(Tran2, U)