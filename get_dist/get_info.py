# coding:utf-8
# 这个文件是为了从高德地图的网站上获得导航信息，当时由于不确定要不要具体路径等数据，所以将所有的网站返回结果都存储了下来
# 这个程序需要与dist_array配合，用来获得行驶时间和距离


import os
import re
import requests
import time

path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))  # 为了获取上级目录（这句从网上copy的）
infile = path + '\\data\\final.csv'  # 输入文件位置
out_file = path + '\\get_dist\\dist_resp_out.csv'  # 输出文件位置


# out_file='d:dist_info_out_test.csv'

# 输出函数，以添加的方式输出字符串
def output(string):
    f = open(out_file, 'a')
    f.write(string)
    f.close()


# 读取文件
def readfile():
    f = open(infile, 'r')
    text = f.read()
    full_text = text.decode('GBK').encode('utf-8').split('\n')  # 改变编码格式
    f.close()
    return full_text


# let the time changed to minutes 将时间从小时转换为分钟
def min_time(atime):
    hour = int(re.findall('\d+(?=:)', atime)[0])
    min = int(re.findall('(?<=:)\d+', atime)[0])
    if hour >= 8:
        amin = hour * 60 + min
    else:
        amin = (hour + 24) * 60 + min
    return amin


full_text = readfile()


# 得到目的地列表
def get_termimal_list(date):
    tlist = []
    for line in full_text[1:]:  # to ignore the first row
        if line == '':
            break
        line_date = line.split(',')[1]  # 当前行的日期
        need_date = '2018/4/' + str(date)  # 当前所需要的日期
        # print line_date,need_date
        if line_date == need_date:  # 如果两者相同
            latlng = re.findall('\d+\.\d+,\d+\.\d+', line)[0]  # 经纬度
            no = line.split(',')[0]  # 乘客ID
            atime = line.split(',')[5]  # arrive time
            amin = min_time(atime)  # use the minutes
            # print amin, latlng
            tlist.append([no, amin, latlng])  # 将其加入到tlist中
    return tlist


# 从网页上得到车辆导航信息
def getroad(start, stop):
    # print 'start=',start,'stop=',stop
    # 'http://restapi.amap.com/v3/direction/driving?origin=116.481028,39.989643&destination=116.465302,40.004717&extensions=all&output=xml&key=<用户的key>'
    adist_url = 'http://restapi.amap.com/v3/direction/driving?key=2ce2e4407b3b5479d28515260bbc7f37&extensions=base'  # 请求的地址
    airport_latlng = '103.955542,30.569893'  # 机场的经纬度

    if start == 'airport':
        start = airport_latlng
    adist_url += '&origin=' + start  # 请求地址中加入起点信息
    adist_url += '&destination=' + stop  # 请求地址中加入终点信息
    response = requests.get(adist_url).text
    return response


# 只是为了把文件清空一下
def renew_out_file():
    f = open(out_file, 'w')
    f.truncate()
    f.close()


# 主函数
for date in range(22, 23):
    print '###################'
    print 'Date  =  ', date
    print '###################'
    out_file = 'dist_info_out_test.csv'
    renew_out_file()  # 清空一下输出文件

    # list=[no,arrive_time, latitude and longitude ]

    termimal_list = get_termimal_list(date)  # 从现有文件中获得目的地列表
    malist = len(termimal_list)  # 获得当天的订单数量
    for j in range(malist):  # the distance from airport to terminal从机场到订单目的地的距离
        print 'From Airport To Point', j
        info = getroad('airport', termimal_list[j][2])
        output(str(date) + ',' + 'A,' + termimal_list[j][0] + ',' + info.encode('utf-8') + ',\n')

    for i in range(malist):  # the distance between two point不同订单目的地之间的距离
        for j in range(malist):  # change 'malist' to 'i' use the single way's distance可以把括号中的malist改为i，即只获取单边的距离

            timei = termimal_list[i][1]  # 订单i的到达时间
            timej = termimal_list[j][1]  # 订单j的到达时间
            start = termimal_list[i][2]  # 起始点坐标
            stop = termimal_list[j][2]  # 终点坐标
            if abs(timei - timej) <= 30 and i != j:  # 做一个验证，超过时间约束的去掉，以及起点和终点不能是同一个点
                print 'From Point', i, 'To Point', j
                info = getroad(start, stop)
                output(str(date) + ',' + termimal_list[i][0] + ',' + termimal_list[j][0] + ',' + info.encode(
                    'utf-8') + ',\n')
