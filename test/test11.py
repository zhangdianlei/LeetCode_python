# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/21 09:05
@python version: 

"""

a = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(max(a[7:]))

print(sorted(a))

b = c = sorted(a)

print(a.index(b[7]))

a[a.index(b[7])] = -1

print(a)

print(a.index(b[8]))