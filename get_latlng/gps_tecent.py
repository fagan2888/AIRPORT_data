#  coding:utf-8
import requests
import json
import re
import time
import sys
import traceback

reload(sys)
sys.setdefaultencoding('utf-8')
def output(string):
    f=open(output_file_name,'a')
    f.write(string.decode('utf-8').encode('GBK'))
    f.close()


# from Amap get the latitude and longtitude
def get_latlng(address):
    url = 'http://apis.map.qq.com/ws/geocoder/v1/'
    #address = u'新时代广场'
    url += '?address=成都'+address.decode('utf-8')
    url += '&key=NHUBZ-QJ6CO-BIRWH-SQRAN-AKYFH-PSBEJ'
    response = requests.get(url).text
    json_res = json.loads(response)
    if json_res['status']==0:
        try:
            '''
            {
                "status":0,
                "message":"query ok",
                "result":{
                    "title":"成都迷津青年旅舍",
                    "location":{
                        "lng":104.070462,
                        "lat":30.659517
                    },
                    "address_components":{
                        "province":"四川省",
                        "city":"成都市",
                        "district":"青羊区",
                        "street":"",
                        "street_number":""
                    },
                    "similarity":0.8,
                    "deviation":1000,
                    "reliability":7,
                    "level":11
                }
            }
            '''
            district=json_res['result']['address_components']['district']
            formatted_address=json_res['result']['title']
            location=str(json_res['result']['location']['lng'])+','+str(json_res['result']['location']['lat'])
            simil=str(json_res['result']['similarity'])
            reliability=str(json_res['result']['reliability'])
            print district,formatted_address,location,simil,reliability
        except:
            print traceback.print_exc()
            sys.exit(1)
            print address,'cannot find the location'
            formatted_address=''
            location=''
            simil=''
            reliability=''
        string='成都'+district.encode('utf-8')+formatted_address.encode('utf-8')+','+location.encode('utf-8')+','+simil+','+reliability+'\n'
        output(string.encode('utf-8'))
    else:
        print json_res['message']  # print error message

def get_address_list():

    f=open(infile,'r')
    addr=f.readline()
    while addr :
        addr=f.readline()
        add=addr.replace('\n','')
        m=re.search('#',add)
        if add=='' or m!=None:
            output(add.encode('utf-8')+',,,,,\n')
        else:
            get_latlng(add)
            time.sleep(0.2)


infile = 'address.txt'
output_file_name='latlng_tecent.csv'
f=open(output_file_name,'w')
f.truncate()
f.close()
#get_latlng(u'新时代广场')
get_address_list()