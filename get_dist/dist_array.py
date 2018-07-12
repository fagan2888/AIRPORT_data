import re
import os
import json#用来处理json返回结果

path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))#还是为了获得上级目录
usr_infile = path + '\\data\\final.csv'#订单信息位置
dist_infile = 'dist_info_out_test.csv'#从get_info文件得到的高德返回的数据


# this file is using UTF-8


#读取文件
def readfile():
    f = open(usr_infile, 'r')
    text = f.read()
    full_text = text.split('\n')
    f.close()
    return full_text


# let the time changed to minutes从时间转化为分钟方便处理（前面的文件里出现过了）
def min_time(atime):
    hour = int(re.findall('\d+(?=:)', atime)[0])
    min = int(re.findall('(?<=:)\d+', atime)[0])
    if hour >= 9:
        amin = hour * 60 + min
    else:
        amin = (hour + 24) * 60 + min
    return amin


full_text = readfile()


# 获得订单列表
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

#获得ij两点之间的距离
def get_dist(i, j):
    f = open(dist_infile, 'r')#打开文件
    all_resp = f.readlines()#读取文件
    for one_resp in all_resp:#下面几行都是为了找到需要的部分
        line_date = one_resp[0:2]
        if line_date == str(date):
            point = re.findall('(?<=,)(A|\d+)(?=,)', one_resp)
            start = point[0]
            stop = point[1]
            if start == str(i) and stop == str(j): #如果当前行为我们要找的行（这里的搜索方法效率很低，但是订单少的时候没有影响）
                json_resp = re.findall('\{.*?\}\}', one_resp)[0] #找到符合json标准的那一段字符
                # print json_resp
                jsonobj = json.loads(json_resp)#以json 的方法读取上一句找到的字符
                # print jsonobj
                status = jsonobj['status']#找到status
                if status == '1':  # status为一个网站返回的值，为1则表示成功获得导航数据
                    path = jsonobj['route']['paths'][0]#获得行驶路径
                    distance = path['distance']#获得行驶距离
                    duration = path['duration']#获得行驶时间
                    print distance, duration
                    return int(distance), int(duration)#将其转化为整数形式返回
                else:
                    print jsonobj['info']#如果没能成功获得导航，则打印错误信息


#输出距离矩阵和时间矩阵
def output_array(date, dist_array, dura_array):
    distout_file = str(date) + 'dist_test.csv'#输出文件
    duraout_file = str(date) + 'dura_test.csv'
    open(distout_file, 'w').close()#重置输出文件（清空）
    open(duraout_file, 'w').close()
    f1 = open(distout_file, 'a')
    for line in dist_array:
        f1.write(str(line)[1:-1] + '\n')
    f1.close()

    f2 = open(duraout_file, 'a')
    for line in dura_array:
        f2.write(str(line)[1:-1] + '\n')
    f2.close()


alatlng = '103.955542,30.569893'# 机场的经纬度
#要处理的日期范围，按需修改#############################################
for date in range(22, 23):

    print '###################'
    print 'Date  =  ', date
    print '###################'

    # renew_out_file()

    termimal_list = get_termimal_list(date)
    malist = len(termimal_list)#最大订单数量
    #初始化两个矩阵，将其全部赋0（二维的list如果不用这种方法初始化，有时候赋值结果会出错）
    dist_array = [[0 for i in range(malist + 1)] for j in range(malist + 1)]
    dura_array = [[0 for i in range(malist + 1)] for j in range(malist + 1)]

    # list=[no,arrive_time, latitude and longitude ]

    butt = int(termimal_list[0][0])
    top = int(termimal_list[-1][0]) + 1
    for j in range(butt, top):  # the distance from airport to terminal从机场到订单目的地的距离
        print 'From Airport To Point', j,
        dist, dura = get_dist('A', j)
        dist_array[0][j + 1 - butt] = dist
        dura_array[0][j + 1 - butt] = dura
    for i in range(malist):  # the distance between two point两个订单目的地之间的距离
        for j in range(i):  # 括号内取i因为只计算单向的距离

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
