
import csv
import numpy as np
arr=[]
with open('test.data','r') as fin:
    cin=csv.reader(fin,delimiter=' ')
    for row in cin:
        print(row)
        new_row=[float(em) for em in row if em != '']
        #if new_row != []:
        print(new_row)
        arr.append(new_row)


print(arr)
result=np.array(arr)
print("We have generated a two-dim array")
print(type(result))
print(result)
#print(result.shape)
#NSample=2000
#r  =(result.shape[0])-NSample
#rr =result.shape[0]

#yy=result[r:rr, 1]
#
#
#totalN=80000
#yyy=np.pad(yy,(0,totalN-NSample),'constant')
