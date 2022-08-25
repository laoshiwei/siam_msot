#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 14:38:32 2022

@author: atur
"""

import os
import shutil
path = "/home/atur/pysot/experiments/siamrpn_r50_l234_dwxcorr"
for fol in os.listdir(path):
    new_path = path + "/" + fol
    for i in os.listdir(new_path):
        print(i)
        try:
            os.mkdir(new_path + "/color")
        except:
            pass
        if i.endswith(".jpg"):
            shutil.move(new_path+ "/"+i, new_path+ "/color/"+i)
            #print(i)
        #os.mkdir("color")
    
    #print(new_path)
