
import csv
import numpy as np
arr=[]
with open('out.data','r') as fin:
    cin=csv.reader(fin,delimiter=' ')
    for row in cin:
        row=[float(em) for em in row if em != '']
        if row != []:
            arr.append(row)



result=np.array(arr)
#print(result.shape)
NSample=2000
r  =(result.shape[0])-NSample
rr =result.shape[0]

yy=result[r:rr, 1] 
#

totalN=80000
yyy=np.pad(yy,(0,totalN-NSample),'constant')


T=0.000025
#print('nonzero during ',NSample*T)
stop=(totalN-1)*T
t=np.linspace(0,stop,totalN)


import matplotlib.pyplot as plt

plt.xlim(0,0.01)
plt.plot(t,yyy)


from scipy import fftpack
faX=fftpack.fft(yyy)
Xc=faX*T
Xcabs=np.abs(Xc)
#print(Xcabs.shape)


freqs=fftpack.fftfreq(totalN,T)
plt.plot(freqs,Xcabs)
np.max(Xcabs)


peak_result=np.where(Xcabs==np.max(Xcabs))
peak_index=peak_result[0][0]
#print(peak_index)




print('The frequency is :' ,freqs[peak_index])
