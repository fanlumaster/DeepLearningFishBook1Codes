import numpy as np


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)  # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y


a = np.array([1010, 1000, 990])
# 下面这里会溢出
# print(np.exp(a) / np.sum(np.exp(a)))  # softmax函数的运算
c = np.max(a)  # 1010
print(a - c)
print(np.exp(a - c) / np.sum(np.exp(a - c)))
