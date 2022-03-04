# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 17:38:10 2022

@author: Nithyashri
"""

import sounddevice as sd
import numpy as np
duration=1.0
fs=10000
sa=261 
re=294
ga=330  
ma=349  
pa=392  
dha=440  
ni=494  
sa1=515

s1=(np.sin(2*np.pi*np.arange(fs*duration)*sa/fs)).astype(np.float32)
s2=(np.sin(2*np.pi*np.arange(fs*duration)*re/fs)).astype(np.float32)
s3=(np.sin(2*np.pi*np.arange(fs*duration)*ga/fs)).astype(np.float32)
s4=(np.sin(2*np.pi*np.arange(fs*duration)*ma/fs)).astype(np.float32)
s5=(np.sin(2*np.pi*np.arange(fs*duration)*pa/fs)).astype(np.float32)
s6=(np.sin(2*np.pi*np.arange(fs*duration)*dha/fs)).astype(np.float32)
s7=(np.sin(2*np.pi*np.arange(fs*duration)*ni/fs)).astype(np.float32)
s8=(np.sin(2*np.pi*np.arange(fs*duration)*sa1/fs)).astype(np.float32)


s=np.hstack((s1,s2,s3,s4,s5,s6,s7,s8))
sd.play(s,fs)

