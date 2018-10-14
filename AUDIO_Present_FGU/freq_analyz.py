
def get_freq(audio_file,fsam):
    import csv
    import numpy as np
    arr=[]
    with open(audio_file,'r') as fin:
        cin=csv.reader(fin,delimiter=' ')
        for row in cin:
            row=[float(em) for em in row if em != '']
            if row != []:
                arr.append(row)



    result=np.array(arr)
    NSample=2000
    r  =(result.shape[0])-NSample
    rr =result.shape[0]

    yy=result[r:rr, 1] 

    totalN=80000
    yyy=np.pad(yy,(0,totalN-NSample),'constant')

    T=1/fsam
    stop=(totalN-1)*T
    t=np.linspace(0,stop,totalN)




    from scipy import fftpack
    faX=fftpack.fft(yyy)
    Xc=faX*T
    Xcabs=np.abs(Xc)


    freqs=fftpack.fftfreq(totalN,T)
    np.max(Xcabs)


    peak_result=np.where(Xcabs==np.max(Xcabs))
    peak_index=peak_result[0][0]
    print('The frequency is :' ,freqs[peak_index])
