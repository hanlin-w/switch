#! /usr/bin/env python

import os
import pickle
import sys

if __name__ == '__main__':
    newad = sys.argv[1]
    if os.path.isfile('dev.p'):
        devs = pickle.load(open('dev.p', 'rb'))
    else:
        print('error')
        quit()
    if newad in devs:
        devs.remove(newad)
        print('delete ' + newad)
    pickle.dump(devs, open('dev.p', 'w'))
        
        

