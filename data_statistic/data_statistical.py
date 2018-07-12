# coding:utf-8
import re

data_list = []
car_list = [[[] for i in range(60)] for j in range(7)]
#print car_list


def get_data():
    import os
    path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    data_file = path + '\\data\\final.csv'
    f = open(data_file, 'r')
    line = f.readline()
    '2018 / 4 / 20, 1, 新城市广场, 1, 9:52, 10:18, 四川省成都市青羊区新城市广场, 104.057651, 30.67383,'
    while line:
        line = f.readline().decode('GBK').encode('utf-8').replace('\n', '')
        if line == '':
            break
        infos = line.split(',')
        dep_time = infos[6]
        if re.search(':', dep_time):  # get the departure  time
            data_list.append(line)
            # print line
    return data_list


def poly_car():
    for line in data_list:
        infos = line.split(',')
        usr_id = infos[0]
        date = infos[1][-2:]
        num = infos[2]
        if num == '':
            num = '1'
        cp_id = infos[4]
        arr_time = infos[5]
        dep_time = infos[6]
        for day in range(0, 7):
            if date == str(20 + day):
                for car_id in range(0, 60):
                    if str(car_id) == cp_id:
                        if len(car_list[day][car_id]) == 0:
                            car_list[day][car_id].append(day)
                            car_list[day][car_id].append(car_id)
                            car_list[day][car_id].append(dep_time)
                            car_list[day][car_id].append([usr_id, num])
                        else:
                            car_list[day][car_id].append([usr_id, num])
    num = [0, 0, 0, 0]
    for i in range(7):
        for j in range(60):
            if len(car_list[i][j]) != 0:
                print car_list[i][j]
                # print len(car_list[i][j])
                car_passenger_count = 0
                for pas in car_list[i][j][3:]:
                    car_passenger_count += int(pas[1])
                print car_passenger_count
                num[car_passenger_count - 1] += 1
    print num


get_data()
poly_car()
