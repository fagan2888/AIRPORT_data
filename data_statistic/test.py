# encoding:utf-8
import sys
import os

file_name = 'all.csv'

path= os.path.dirname(os.path.abspath("__file__"))
path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))

f = open(path+'\data\\'+file_name)

print f.readline()
f.close()