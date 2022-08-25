#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:45:10 2022

@author: atur
"""

import os
import shutil
path = "/home/atur/pysot/experiments/siamrpn_r50_l234_dwxcorr/results/VOT2018/tomp50/baseline"
for fol in os.listdir(path):
    new_path = path + "/" + fol
    print(new_path)
    #base=os. path. basename(folder)
    base = os.path.splitext(fol)[0]
    os.mkdir(path + "/" + base)
    shutil.move(new_path, path+"/"+base+ "/" +fol)
    
