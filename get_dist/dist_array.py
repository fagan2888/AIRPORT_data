import re
import os
import json

path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
usr_infile = path + '\\data\\final.csv'
dist_infile = 'dist_info_out.csv'


# this file is using UTF-8


def readfile():
    f = open(usr_infile, 'r')
    text = f.read()
    full_text = text.split('\n')
    f.close()
    return full_text


# let the time changed to minutes
def min_time(atime):
    hour = int(re.findall('\d+(?=:)', atime)[0])
    min = int(re.findall('(?<=:)\d+', atime)[0])
    if hour >= 9:
        amin = hour * 60 + min
    else:
        amin = (hour + 24) * 60 + min
    return amin


full_text = readfile()


def get_termimal_list(date):
    tlist = []
    for line in full_text[1:]:  # to ignore the first row
        if line == '':
            break
        line_date = line.split(',')[1]
        need_date = '2018/4/' + str(date)
        # print line_date,need_date
        if line_date == need_date:
            latlng = re.findall('\d+\.\d+,\d+\.\d+', line)[0]
            no = line.split(',')[0]
            atime = line.split(',')[5]  # arrive time
            amin = min_time(atime)  # use the minutes
            print no, amin, latlng
            tlist.append([no, amin, latlng])
    return tlist


def get_dist(i, j):
    f = open(dist_infile, 'r')
    all_resp = f.readlines()
    for one_resp in all_resp:
        line_date = one_resp[0:2]
        if line_date == str(date):
            point = re.findall('(?<=,)(A|\d+)(?=,)', one_resp)
            start = point[0]
            stop = point[1]
            if start == str(i) and stop == str(j):
                json_resp = re.findall('\{.*?\}\}', one_resp)[0]
                # print json_resp
                jsonobj = json.loads(json_resp)
                # print jsonobj
                status = jsonobj['status']
                if status == '1':
                    path = jsonobj['route']['paths'][0]
                    distance = path['distance']
                    duration = path['duration']
                    print distance, duration
                    return int(distance), int(duration)
                else:
                    print jsonobj['info']


def output_array(date, dist_array, dura_array):
    distout_file = str(date) + 'dist.csv'
    duraout_file = str(date) + 'dura.csv'
    open(distout_file, 'w').close()
    open(duraout_file, 'w').close()
    f1 = open(distout_file, 'a')
    for line in dist_array:
        f1.write(str(line)[1:-1] + '\n')
    f1.close()

    f2 = open(duraout_file, 'a')
    for line in dura_array:
        f2.write(str(line)[1:-1] + '\n')
    f2.close()


alatlng = '103.955542,30.569893'
for date in range(20, 28):

    print '###################'
    print 'Date  =  ', date
    print '###################'

    # renew_out_file()

    termimal_list = get_termimal_list(date)
    malist = len(termimal_list)

    dist_array = [[0 for i in range(malist + 1)] for j in range(malist + 1)]
    dura_array = [[0 for i in range(malist + 1)] for j in range(malist + 1)]

    # list=[no,arrive_time, latitude and longitude ]

    butt = int(termimal_list[0][0])
    top = int(termimal_list[-1][0]) + 1
    for j in range(butt, top):  # the distance from airport to terminal
        print 'From Airport To Point', j,
        dist, dura = get_dist('A', j)
        dist_array[0][j + 1 - butt] = dist
        dura_array[0][j + 1 - butt] = dura
    for i in range(malist):  # the distance between two point
        for j in range(i):  # change 'malist' to 'i' use the single way's distance

            timei = termimal_list[i][1]
            timej = termimal_list[j][1]
            start = termimal_list[i][2]
            stop = termimal_list[j][2]
            if abs(timei - timej) <= 30 and i != j:
                print 'From Point', i + butt, 'To Point', j + butt,
                dist, dura = get_dist(i + butt, j + butt)
                dist_array[i + 1][j + 1] = dist
                dura_array[i + 1][j + 1] = dura
    for i in range(malist + 1):
        print dist_array[i]
    output_array(date, dist_array, dura_array)
