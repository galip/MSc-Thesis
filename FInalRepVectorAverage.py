import os
from os import walk

import numpy as np
np.set_printoptions(precision=3)

def getRep(path):
    f = open(path, 'r+')
    output = f.read()
    rep = output.split()
    new_rep = []

    for item in rep :
        new_rep.append(float(item))

    f.close()
    return new_rep

count = 0
k = 0
counter = 0
list = []

for dirpath, dirnames, filenames in walk("/home/galip/Desktop/repvector"):

    for f in filenames:

      a = f.partition(".")[0].rsplit("_", 1).__getitem__(0)
      print("a : ", a)

      if a not in  list:

       list.insert(1,a)

       k = 0
       count = 0

       for x in filenames:

        b = x.partition(".")[0].rsplit("_", 1).__getitem__(0)

        if a == b :

         d = getRep(dirpath + "/" + x)
         d = np.array(d)
         k = k + d
         count += 1
         print("b : ", b)

         if count == 3:
          count = 0
          counter += 1
          print (counter)
          name = '/home/galip/Desktop/finalrepvector/' + a + '.txt'
          file = open(name, 'a')
          np.savetxt(name, k/3, delimiter=',')
          file.close()