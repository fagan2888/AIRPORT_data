#coding:utf-8
import os
import re
import requests
import time


path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
infile=path+'\\data\\final.csv'
out_file='out.txt'


def output(string):
    f = open(out_file, 'a')
    f.write(string)
    f.close()


def readfile():
    f = open(infile, 'r')
    text = f.read()
    full_text = text.decode('GBK').encode('utf-8').split('\n')
    f.close()
    return full_text


# let the time changed to minutes
def min_time(atime):
    hour=int(re.findall('\d+(?=:)',atime)[0])
    min=int(re.findall('(?<=:)\d+',atime)[0])
    if hour>=9:
        amin=hour*60+min
    else:
        amin=(hour+24)*60+min
    return amin


full_text = readfile()


def get_termimal_list(date):
    tlist=[]
    for line in full_text[1:]:  # to ignore the first row
        if line == '':
            break
        line_date=line.split(',')[1]
        need_date='2018/4/'+str(date)
        #print line_date,need_date
        if line_date==need_date:
            latlng = re.findall('\d+\.\d+,\d+\.\d+', line)[0]
            no=line.split(',')[0]
            atime = line.split(',')[5]  # arrive time
            amin = min_time(atime)  # use the minutes
            print str(amin-60*9)#+',', #latlng
            tlist.append([no,amin,latlng])
    return tlist




def renew_out_file():
        f = open(out_file, 'w')
        f.truncate()
        f.close()


for date in range(20,21):
    #print '###################'
    #print 'Date  =  ',date
    #print '###################'

    renew_out_file()

    # list=[no,arrive_time, latitude and longitude ]
    termimal_list=get_termimal_list(date)
    malist=len(termimal_list)
    for j in range(malist):  # the distance from airport to terminal
        #print 'From Airport To Point',j
        output('data'+str(date)+','+'A,'+termimal_list[j][0]+','+ ',\n')
