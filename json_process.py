#coding:utf-8
string='{"status":"1","info":"OK","infocode":"10000","count":"1","geocodes":[{"formatted_address":"四川省成都市青羊区新时代广场","province":"四川省","citycode":"028","city":"成都市","district":"青羊区","township":[],"neighborhood":{"name":[],"type":[]},"building":{"name":[],"type":[]},"adcode":"510105","street":[],"number":[],"location":"104.072410,30.669535","level":"兴趣点"}]}'

import json
json_res = json.loads(string)
print json_res['status']
if json_res['status']=='1':
    formatted_address=json_res['geocodes'][0]['formatted_address']
    location=json_res['geocodes'][0]['location']
    print formatted_address,location
else:
    print json_res['info']
