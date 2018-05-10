#coding:utf-8
import os
import re
import requests
import time


path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
infile=path+'\\data\\final.csv'
#out_file=path+'\\get_dist\\dist_resp_out.csv'
out_file='d:dist_info_out.csv'


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
            # print amin, latlng
            tlist.append([no,amin,latlng])
    return tlist


def getroad(start,stop):
    #print 'start=',start,'stop=',stop
    #'http://restapi.amap.com/v3/direction/driving?origin=116.481028,39.989643&destination=116.465302,40.004717&extensions=all&output=xml&key=<用户的key>'
    adist_url = 'http://restapi.amap.com/v3/direction/driving?key=2ce2e4407b3b5479d28515260bbc7f37&extensions=base'
    airport_latlng = '103.955542,30.569893'

    if start=='airport':
        start=airport_latlng
    adist_url += '&origin=' + start
    adist_url += '&destination='+stop
    response = requests.get(adist_url).text
    return response


def renew_out_file():
        f = open(out_file, 'w')
        f.truncate()
        f.close()


for date in range(20,28):
    print '###################'
    print 'Date  =  ',date
    print '###################'

    #renew_out_file()

    # list=[no,arrive_time, latitude and longitude ]
    termimal_list=get_termimal_list(date)
    malist=len(termimal_list)

    for j in range(malist):  # the distance from airport to terminal
        print 'From Airport To Point',j
        info=getroad('airport',termimal_list[j][2])
        output(str(date)+','+'A,'+termimal_list[j][0]+','+info.encode('utf-8') + ',\n')

    for i in range(malist):  # the distance between two point
        for j in range(malist):  # change 'malist' to 'i' use the single way's distance

            timei = termimal_list[i][1]
            timej = termimal_list[j][1]
            start = termimal_list[i][2]
            stop = termimal_list[j][2]
            if abs(timei-timej)<=30 and i != j:
                print 'From Point', i, 'To Point', j
                info = getroad(start,stop)
                output(str(date)+','+termimal_list[i][0]+','+termimal_list[j][0]+','+info.encode('utf-8') + ',\n')