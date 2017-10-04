# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:49:26 2017

@author: xinliu
"""

import numpy as np
import matplotlib.pyplot as plt
import sub_fn_a
import seaborn as sns
x = np.random.randn(1000, 1)

print("Do you want to load tips dataset?")
request = input()
data_tip = sub_fn_a.do_I_want_tips_data(request)
if not data_tip is None:
    sns.regplot(x = "total_bill", y = "tip", data = data_tip)
else:
    print("show histogram for random variables")
    plt.hist(x)
    plt.show()