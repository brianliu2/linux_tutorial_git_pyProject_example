# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:11:01 2017

@author: xinliu
"""

import seaborn as sns

def do_I_want_tips_data(str):
    if str == "yes":
        tips = sns.load_dataset("tips")
        return tips
    else:
        print("I don't want the tips dataset")