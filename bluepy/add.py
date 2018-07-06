#! /usr/bin/env python

import os
import pickle
import sys

if __name__ == '__main__':
    newad = sys.argv[1]
    devs = []
    if os.path.isfile('dev.p'):
        print('have some old devices')
        devs = pickle.load(open('dev.p', 'rb'))
    if newad in devs:
        pass
    else:
        devs.append(newad)
    print(devs)
    pickle.dump(devs, open('dev.p', 'w'))
        
        

