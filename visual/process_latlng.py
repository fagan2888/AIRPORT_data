#coding:utf-8
import os
import re
# 只是用来将经纬度数据稍作调整，转变为高德需要的格式
####################################
#  output files for amap data visual
#  this file is  used to visual the point
####################################
path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))

# infile=path+'\\data\\final.csv'
infile = path + '\\data\\oneday.csv'
f = open(infile, 'r')
text = f.read()
full_text = text.decode('GBK').encode('utf-8').split('\n')

# out_file=path+'\\data\\for_visual_GBK.csv'
out_file = path + '\\data\\oneday_visual.csv'

f = open(out_file, 'w')
f.truncate()
f.close()
f = open(out_file, 'a')
i = 0
f.write(full_text[0].decode('utf-8').encode('GBK') + ',latlng,\n')  #
for line in full_text[1:]:  # to ignore the first row
    if line == '':
        break
    latlng = re.findall('\d+\.\d+,\d+\.\d+', line)[0]
    line = line + ',"' + latlng + '",' + '\n'
    f.write(line.decode('utf-8').encode('GBK'))
f.close()
