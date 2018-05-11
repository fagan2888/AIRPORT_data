#  coding:utf-8

############################
#  get the latlng using amap
############################

import requests
import json
import re
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def output(string):
    f=open(output_file_name,'a')
    f.write(string.decode('utf-8').encode('GBK'))
    f.close()


# from Amap get the latitude and longtitude
def get_latlng(address):
    url = 'http://restapi.amap.com/v3/geocode/geo?key=2ce2e4407b3b5479d28515260bbc7f37'
    #address = u'新时代广场'
    url += '&address='+address.decode('utf-8')
    url += u'&city=成都'
    response = requests.get(url).text
    json_res = json.loads(response)
    if json_res['status']=='1':
        try:
            formatted_address=json_res['geocodes'][0]['formatted_address']
            location=json_res['geocodes'][0]['location']
            print formatted_address,location
        except:
            print address,'cannot find the location'
            formatted_address=''
            location=''
        string=address.encode('utf-8')+','+formatted_address.encode('utf-8')+','+location.encode('utf-8')+'\n'
        output(string.encode('utf-8'))
    else:
        print json_res['info']

def get_address_list():

    f=open(infile,'r')
    addr=f.readline()
    while addr :
        addr=f.readline()
        add=addr.replace('\n','')
        m=re.search('#',add)
        if add=='' or m!=None:
            output(add.encode('utf-8')+',,,\n')
        else:
            get_latlng(add)
            #time.sleep(0.1)


infile = 'address.txt'
output_file_name='latlng2.csv'
f=open(output_file_name,'w')
f.truncate()
f.close()
#get_latlng(u'新时代广场')
get_address_list()