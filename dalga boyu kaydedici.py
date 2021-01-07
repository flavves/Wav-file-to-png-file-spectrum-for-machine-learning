# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 00:40:51 2021

@author: yazılım
"""



"""

Spektogram kaydetmesi TOPLU

"""
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import random
from scipy.io import wavfile
from sklearn.preprocessing import scale
import librosa.display
import librosa
import matplotlib.pyplot as plt
import os

sampling_rate=44100
sayac=1
while 1:
    if sayac < 2000:
            
        dosya_konum="we/dataset/not/2 ("+str(sayac)+").wav"
        data, sr = librosa.load(dosya_konum, sr=sampling_rate, mono=True)
        data = scale(data)
        
        melspec = librosa.feature.melspectrogram(y=data, sr=sr, n_mels=128)
            # Convert to log scale (dB) using the peak power (max) as reference
                # per suggestion from Librbosa: https://librosa.github.io/librosa/generated/librosa.feature.melspectrogram.html
        log_melspec = librosa.power_to_db(melspec, ref=np.max)  
        librosa.display.specshow(log_melspec, sr=sr)
            
            # create saving directory
        directory = 'we/dataset/notcough_foto/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        foto_ad="a"+str(sayac)    
        plt.savefig(directory + '/' + (foto_ad) + '.png')
        sayac=sayac+1
        print("oldu")
        print(sayac)
    else:
        print("hata")
        

"""

Spektogram kaydetmesi Tekil

"""
dosya=input("dosya adı girin: ")
dosya_konum="we/dataset/not/"+dosya+".wav"
data, sr = librosa.load(dosya_konum, sr=sampling_rate, mono=True)
data = scale(data)
        
melspec = librosa.feature.melspectrogram(y=data, sr=sr, n_mels=128)
           
log_melspec = librosa.power_to_db(melspec, ref=np.max)  
librosa.display.specshow(log_melspec, sr=sr)
            
# kayıt yolu
directory = 'we/dataset/'
if not os.path.exists(directory):
    os.makedirs(directory)
foto_ad="deneme"+str(sayac)    
plt.savefig(directory + '/' + (foto_ad) + '.png')