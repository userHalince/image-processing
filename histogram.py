
import numpy as np

myNumbers = np.random.randint(0,2,10)
myHistogram = {}
myNumbers # siyah beyaz resim olacak

for number in myNumbers:
    if number in myHistogram.keys():
        myHistogram[number]=myHistogram[number]+1
    else:
        myHistogram[number]=1
myNumbers, myHistogram
