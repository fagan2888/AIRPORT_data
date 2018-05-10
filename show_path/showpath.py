import os
import re

path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
infile=path+'\\data\\oneday.csv'
outfile=path+'\\data\\carpath.csv'
open(outfile,'w').close()

data_list=[]
def readfile():
    f=open(infile,'r')
    lines=f.readlines()
    for line in lines[1:]:
        factors=line.split(',')
        no=factors[0]
        cno=factors[4]
        lng=factors[7]
        lat=factors[8].replace('\n','')
        if cno !='':
            #cno=int(cno)-1 # the car No start from 1
            data_list.append([no,cno,lng,lat])
            #print no,cno,lng,lat


def carpath():
    maxcno=int(data_list[-1][1])
    print 'max car No = ',maxcno
    car_list = [[] for i in range(maxcno)]
    for cno in range(1,maxcno+1):
        for line in data_list:
            no=line[0]
            lng=line[2]
            lat=line[3]
            if line [1]==str(cno):
                car_list[cno-1].append([no,lng,lat])
            else:
                pass
    return car_list

def output(string):
    f=open(outfile,'a')
    f.write(string.decode('utf-8').encode('GBK'))
    f.close()


def pathfile(carlist):
    airlat='30.569893'
    airlng='103.955542'
    output('carno,start,terminal,latlng\n')

    for ocar in carlist:
        ocar[0:0]=[['A',airlng,airlat]]
        for i in range(len(ocar)-1):
            p0=ocar[i]  # start passenger
            p1=ocar[i+1]
            outlist=[str(carlist.index(ocar)+1),p0[0],p1[0],'"['+p0[1]+','+p0[2]+'],['+p1[1]+','+p1[2]+']"']
            string=','.join(outlist)+'\n'
            print string,
            output(string.encode('utf-8'))


readfile()
carlist = carpath()
print carlist
pathfile(carlist)